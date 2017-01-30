Headerlets (`stwcs.wcsutil.headerlet`)
======================================

The 'headerlet' serves as a mechanism for encapsulating WCS information
for a single pointing so that it can be used to update the WCS solution of
an image. The concept of a 'headerlet' seeks to provide a solution where
only the WCS solution for an image that has been aligned to an astrometric
catalog can be archived and retrieved for use in updating copies of
that image's WCS information without getting the image data again.
Multiple 'headerlets' could even be provided with each representing the
alignment of an image to a different astrometric solution, giving the end
user the option to get the solution that would allow them to best align
their images with external data of interest to them.  These benefits
can only be realized with the proper definition of a 'headerlet' and
the procedures used to define them and apply them to data.

The headerlet object needs to be as compact as possible while providing
an unambigious and self-consistent WCS solution for an image while
requiring a minimum level of software necessary to apply the headerlet
to an image.

Headerlet File Structure
-------------------------
This new object complete with the NPOLFILE and the D2IMFILE extensions
derived from the full FITS file fully describes the WCS of each chip
and serves without further modification as the definition of the
`headerlet`. The listing of the FITS extensions for a `headerlet` for
the sample ACS/WFC exposure after writing it out to a file would then be::

    EXT#  FITSNAME      FILENAME              EXTVE DIMENS       BITPI OBJECT

    0     j8hw27c4q     j8hw27c4q_hdr.fits                       16
    1       IMAGE       D2IMARR               1     4096         -32
    2       IMAGE       WCSDVARR              1     64x32        -32
    3       IMAGE       WCSDVARR              2     64x32        -32
    4       IMAGE       WCSDVARR              3     64x32        -32
    5       IMAGE       WCSDVARR              4     64x32        -32
    6       IMAGE       SIPWCS                1                  8
    7       IMAGE       SIPWCS                2                  8

This file now fully describes the WCS solution for this image, complete with all the distortion information used to originally define the solution. No further reference files or computations would be needed when this `headerlet` gets used to update an image.

The primary header must have 4 required keywords:

-  `HDRNAME`  - a unique name for the headerlet
-  `DESTIM`   - target image filename (the ROOTNAME keyword of the original archive filename)
-  `WCSNAME`  - the value of WCSNAME<key> copied from the WCS which was used to create the headerlet
-  `SIPNAME`  - the name of reference file which contained the original distortion model coefficients. A blank value or 'N/A' will indicate no SIP model was provided or applied. A value of 'UNKNOWN' indicates a SIP model of unknown origin.
-  `NPOLFILE` - the name of the NPOLFILE, the reference file which contained the original non-polynomial corrections. The same rules used for SIPNAME apply here as well.
-  `D2IMFILE` - the name of the D2IMFILE, the reference file which contained the detector to image correction (such as column width correction calibrations). The same rules used for SIPNAME apply here as well.
-  `DISTNAME` - a concatenation of SIPNAME, NPOLFILE, and D2IMFILE used as a quick reference for the distortion models included with this headerlet.
-  `UPWCSVER` - version of STWCS used to create the WCS of the original image
-  `PYWCSVER` - version of PyWCS used to create the WCS of the original image


Manipulating Headerlets
-----------------------

Creating Headerlets
~~~~~~~~~~~~~~~~~~~
Headerlets can be created from existing FITS files for saving separately,
modification, or even applying to other files.  The `create_headerlet` function
will pull the WCS information from the given FITS files into a Headerlet object.

>>> from stwcs.wcsutil import headerlet
>>> hdrlet = headerlet.create_headerlet('jcoy02c8q_flt.fits')
>>> hdrlet.info()
    HDRNAME  WCSNAME        DISTNAME                                 AUTHOR  DATE                 SIPNAME              NPOLFILE                 D2IMFILE                 DESCRIP
    OPUS     IDC_0461802dj  jcoy02c8q_0461802dj-02c1450rj-02c1450oj          2017-01-25T13:28:36  jcoy02c8q_0461802dj  jref$02c1450rj_npl.fits  jref$02c1450oj_d2i.fits

This resulting headerlet object can then be written to an output file if needed.

>>> hdrlet.tofile('out_hlet.fits')

Attaching a Headerlet to a file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A file with no headerlets, but valid WCSs, can be seen below.

>>> from astropy.io import fits
>>> with fits.open('jcoy02c8q_flt.fits') as hdu:
...     print(hdu.info())
Filename: jcoy02c8q_flt.fits
No.    Name         Type      Cards   Dimensions   Format
  0  PRIMARY     PrimaryHDU     256   ()
  1  SCI         ImageHDU       200   (4096, 2048)   float32
  2  ERR         ImageHDU        56   (4096, 2048)   float32
  3  DQ          ImageHDU        48   (4096, 2048)   int16
  4  SCI         ImageHDU       198   (4096, 2048)   float32
  5  ERR         ImageHDU        56   (4096, 2048)   float32
  6  DQ          ImageHDU        48   (4096, 2048)   int16
  7  D2IMARR     ImageHDU        15   (64, 32)   float32
  8  D2IMARR     ImageHDU        15   (64, 32)   float32
  9  D2IMARR     ImageHDU        15   (64, 32)   float32
 10  D2IMARR     ImageHDU        15   (64, 32)   float32
 11  WCSDVARR    ImageHDU        15   (64, 32)   float32
 12  WCSDVARR    ImageHDU        15   (64, 32)   float32
 13  WCSDVARR    ImageHDU        15   (64, 32)   float32
 14  WCSDVARR    ImageHDU        15   (64, 32)   float32
 15  WCSCORR     BinTableHDU     59   14R x 24C   [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]

A headerlet can be appended to the HDU easily:

>>> # Using an already created headerlet object from the above examples
>>> hdrlet.apply_as_primary('jcoy02c8q_flt.fits')

After which, the headerlet can be seen in the file structure.

>>> from astropy.io import fits
>>> with fits.open('jcoy02c8q_flt.fits') as hdu:
...     print(hdu.info())
Filename: jcoy02c8q_flt.fits
No.    Name         Type      Cards   Dimensions   Format
  0  PRIMARY     PrimaryHDU     256   ()
  1  SCI         ImageHDU       228   (4096, 2048)   float32
  2  ERR         ImageHDU        56   (4096, 2048)   float32
  3  DQ          ImageHDU        48   (4096, 2048)   int16
  4  SCI         ImageHDU       224   (4096, 2048)   float32
  5  ERR         ImageHDU        56   (4096, 2048)   float32
  6  DQ          ImageHDU        48   (4096, 2048)   int16
  7  WCSCORR     BinTableHDU     59   14R x 24C   [40A, I, A, 24A, 24A, 24A, 24A, D, D, D, D, D, D, D, D, 24A, 24A, D, D, D, D, J, 40A, 128A]
  8  WCSDVARR    ImageHDU        15   (64, 32)   float32
  9  WCSDVARR    ImageHDU        15   (64, 32)   float32
 10  D2IMARR     ImageHDU        15   (64, 32)   float32
 11  D2IMARR     ImageHDU        15   (64, 32)   float32
 12  WCSDVARR    ImageHDU        15   (64, 32)   float32
 13  WCSDVARR    ImageHDU        15   (64, 32)   float32
 14  D2IMARR     ImageHDU        15   (64, 32)   float32
 15  D2IMARR     ImageHDU        15   (64, 32)   float32
 16  HDRLET      HeaderletHDU     26   ()

Locating and Viewing Headerlets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>>> hdu = fits.open('jcoy02c8q_flt.fits')
>>> # the strict=False parameter is needed to return all found headerlets
>>> headerlet.find_headerlet_HDUs(hdu, strict=False)
[16]

Printing a human-readable summary of headerlets is also available.

>>> headerlet.headerlet_summary('jcoy02c8q_flt.fits')
EXTN    HDRNAME        WCSNAME        DISTNAME                                 AUTHOR  DATE                 SIPNAME              NPOLFILE                 D2IMFILE                 DESCRIP
16      IDC_0461802dj  IDC_0461802dj  jcoy02c8q_0461802dj-02c1450rj-02c1450oj          2017-01-30T15:07:31  jcoy02c8q_0461802dj  jref$02c1450rj_npl.fits  jref$02c1450oj_d2i.fits

Headerlet Deletion
~~~~~~~~~~~~~~~~~~
Headerlets can be removed from files with available utility functions, either
by name or by number.

>>> headerlet.delete_headerlet('jcoy02c8q_flt.fits', hdrext=16)
Deleting Headerlet from  jcoy02c8q_flt.fits
_delete_single_headerlet CRITICAL: Deleted headerlet from extension(s) [16]

>>> headerlet.delete_headerlet('jcoy02c8q_flt.fits', hdrname='IDC_0461802dj')
Deleting Headerlet from  jcoy02c8q_flt.fits
_delete_single_headerlet CRITICAL: Deleted headerlet from extension(s) [16]

Selecting primary and alternate

Reference API
-------------

.. automodapi:: stwcs.wcsutil.headerlet
  :no-heading:
