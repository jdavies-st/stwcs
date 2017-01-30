Hubble Space Telescope WCS  (`stwcs.wcsutil.hstwcs`)
====================================================

Create an HSTWCS Object
--------------------------

HSTWCS objects can be created from HST FITS files and FITS objects in a number
of ways.

- Create an HSTWCS object using a fits HDUList and an extension number

  >>> # Open the FITS file
  >>> fobj = pyfits.open('ibkh02niq_flt.fits.fits')

  >>> # Create the WCS object
  >>> w = wcsutil.HSTWCS(fobj, 3)
  >>> print(w)
  WCS Keywords
  Number of WCS axes: 2
  CTYPE : 'RA---TAN'  'DEC--TAN'
  CRVAL : 201.70107421450001  -47.486053921109999
  CRPIX : 2048.0  1026.0
  CD1_1 CD1_2  : -9.4733176588311993e-06  -6.3094306881446999e-06
  CD2_1 CD2_2  : -5.7245500173206999e-06  9.0919670419474908e-06
  NAXIS : 4096  2051


- Create an HSTWCS object using a qualified file name.

  >>> w = wcsutil.HSTWCS('j9irw4b1q_flt.fits[sci,1]')

- Create an HSTWCS object using a file name and an extension number.

  >>> w = wcsutil.HSTWCS('j9irw4b1q_flt.fits', ext=2)

- Create an HSTWCS object from WCS with key 'O'.

  >>> w = wcsutil.HSTWCS('j9irw4b1q_flt.fits', ext=2, wcskey='O')


A blank HSTWCS object can also be created by passing no arguments to the `HSTWCS`
function.

  >>> w = wcsutil.HSTWCS()
  >>> print(w)
  WCS Keywords
  Number of WCS axes: 2
  CTYPE : ''  ''
  CRVAL : 0.0  0.0
  CRPIX : 0.0  0.0
  CD1_1 CD1_2  : 1.0  0.0
  CD2_1 CD2_2  : 0.0  1.0
  NAXIS : None  None


Coordinate Transformation Examples
----------------------------------
All coordinate transformation functions accept input coordinates
as 2D numpy arrays or 2 sequences of X and Y coordinates.

  >>> inpix = np.array([[1., 2.], [1, 3], [1 ,4], [1, 5]])

or

  >>> X = [1.,1.,1.,1.]
  >>> Y = np.array([2.,3.,4.,5.])

.. note::
  In addition, all transformation functions require an `origin` parameter
  which specifies if the coordinates are 0 or 1 based.  I.e. is the first
  pixel of the image indexed at (0,0) or (1, 1)?
    - in FITS and Fortran, coordinates start from 1.
    - In Python and C, coordinates start from 0.

The complete detector to sky transformation can be applied with a single command
'all_pix2world'.  Note that the returned array(s) depend on how the input
coordinates were supplied.

  >>> outpix = w.all_pix2world(inpix, 1)
  >>> print(outpix)
  array([[ 201.73932919,  -47.48363958],
         [ 201.73931984,  -47.48363049],
         [ 201.7393105 ,  -47.4836214 ],
         [ 201.73930116,  -47.48361231]])


  >>> outpix = w.all_pix2world(X, Y, 1)
  >>> print(outpix)
  [array([ 201.73932919,  201.73931984,  201.7393105 ,  201.73930116]),
   array([-47.48363958, -47.48363049, -47.4836214 , -47.48361231])]

The same transformation can be done by applying each of the separate steps
in sequence.

1. Apply the detector image corrections
2. Apply the SIP polynomial distortion
3. Apply the non-polynomial distortion from the lookup table
4. Compute the undistorted coordinates
5. Transform to world coordinates

  >>> dpx = w.det2im(inpix, 1)
  >>> spx = w.sip_pix2foc(dpx, 1)
  >>> lutpx = w.p4_pix2foc(dpx, 1)

  >>> # The undistorted coordinates are the sum of the input coordinates with
  >>> # the deltas for the distortion corrections.
  >>> fpix = dpx + (spx-dpx) +(lutpx-dpx)

  >>> # Finally the transformation from undistorted to world coordinates is done
  >>> # by applying the linear WCS.
  >>> wpix = w.wcs_pix2world(fpix, 1)


REFERENCE/API
-------------
.. py:module:: stwcs.wcsutil.hstwcs
.. autoclass:: stwcs.wcsutil.hstwcs.HSTWCS
  :members:
  :inherited-members:
  :undoc-members:
  :show-inheritance:
