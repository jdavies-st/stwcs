from astropy.io import fits
try:
    import stwcs
    from stwcs import wcsutil
except:
    stwcs = None

from stsci.tools import fileutil

OPUS_WCSKEYS = ['OCRVAL1','OCRVAL2','OCRPIX1','OCRPIX2',
                'OCD1_1','OCD1_2','OCD2_1','OCD2_2',
                'OCTYPE1','OCTYPE2']


def archive_prefix_OPUS_WCS(fobj,extname='SCI'):
    """ Identifies WCS keywords which were generated by OPUS and archived
        using a prefix of 'O' for all 'SCI' extensions in the file

        Parameters
        ----------
        fobj: string or fits.HDUList
            Filename or fits object of a file

    """
    if stwcs is None:
        print '====================='
        print 'The STWCS package is needed to convert an old-style OPUS WCS to an alternate WCS'
        print '====================='
        raise ImportError


    closefits = False
    if isinstance(fobj,str):
        # A filename was provided as input
        fobj = fits.open(fobj,mode='update')
        closefits=True

    # Define the header
    ext = ('sci',1)
    hdr = fobj[ext].header

    numextn = fileutil.countExtn(fobj)
    extlist = []
    for e in xrange(1,numextn+1):
        extlist.append(('sci',e))

    # Insure that the 'O' alternate WCS is present
    if 'O' not in wcsutil.wcskeys(hdr):
        # if not, archive the Primary WCS as the default OPUS WCS
        wcsutil.archiveWCS(fobj,extlist, wcskey='O', wcsname='OPUS')

    # find out how many SCI extensions are in the image
    numextn = fileutil.countExtn(fobj,extname=extname)
    if numextn == 0:
        extname = 'PRIMARY'

    # create HSTWCS object from PRIMARY WCS
    wcsobj = wcsutil.HSTWCS(fobj,ext=ext,wcskey='O')
    # get list of WCS keywords
    wcskeys = wcsobj.wcs2header().keys()

    # For each SCI extension...
    for e in xrange(1,numextn+1):
        # Now, look for any WCS keywords with a prefix of 'O'
        for key in wcskeys:
            okey = 'O'+key[:7]
            hdr = fobj[(extname,e)].header
            if okey in hdr:
                # Update alternate WCS keyword with prefix-O OPUS keyword value
                hdr[key] = hdr[okey]

    if closefits:
        fobj.close()

def create_prefix_OPUS_WCS(fobj,extname='SCI'):
    """ Creates alternate WCS with a prefix of 'O' for OPUS generated WCS values
        to work with old MultiDrizzle.

        Parameters
        ----------
        fobj: string or fits.HDUList
            Filename or fits object of a file

        Raises
        ------
        IOError:
            if input FITS object was not opened in 'update' mode

    """
    # List of O-prefix keywords to create
    owcskeys = OPUS_WCSKEYS

    closefits = False
    if isinstance(fobj,str):
        # A filename was provided as input
        fobj = fits.open(fobj,mode='update')
        closefits=True
    else:
        # check to make sure this FITS obj has been opened in update mode
        if fobj.fileinfo(0)['filemode'] != 'update':
            print 'File not opened with "mode=update". Quitting...'
            raise IOError

    # check for existance of O-prefix WCS
    if owcskeys[0] not in fobj['sci',1].header:

        # find out how many SCI extensions are in the image
        numextn = fileutil.countExtn(fobj,extname=extname)
        if numextn == 0:
            extname = ''
        for extn in xrange(1,numextn+1):
            hdr = fobj[(extname,extn)].header
            for okey in owcskeys:
                hdr[okey] = hdr[okey[1:]+'O']

    # Close FITS image if we had to open it...
    if closefits:
        fobj.close()
