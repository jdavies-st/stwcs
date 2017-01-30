.. _altwcs:

Alternative WCS
===============
The functions in this module manage alternate WCS's in a header.


Viewing alternate WCSs
----------------------

>>> from astropy.io import fits
>>> with fits.open('jcoy02cbq_flt.fits') as hdu:
...     print(hdu.info())
Filename: jcoy02c8q_flt.fits
No.    Name         Type      Cards   Dimensions   Format
  0  PRIMARY     PrimaryHDU     256   ()
  1  SCI         ImageHDU       384   (4096, 2048)   float32
  2  ERR         ImageHDU        56   (4096, 2048)   float32
  3  DQ          ImageHDU        48   (4096, 2048)   int16
  4  SCI         ImageHDU       374   (4096, 2048)   float32
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

>>> from stwcs.wcsutil import altwcs
>>> altwcs.wcsnames('jcoy02cbq_flt.fits', ext=1)
{' ': 'IDC_0461802dj', 'O': 'OPUS'}

Archiving the primary WCS as an Alternate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

>>> altwcs.wcskeys('jcoy02cbq_flt.fits')
['O']

>>> altwcs.archiveWCS('jcoy02cbq_flt.fits', ext=('sci', 1), wcskey='B')
>>> altwcs.wcskeys('jcoy02cbq_flt.fits', ext=1)
['O', 'B']

This alternatice WCS can then be deleted.

>>> altwcs.deleteWCS('jcoy02cbq_flt.fits', ext=('sci', 1), wcskey='B')
['O']

Reference API
-------------

.. automodapi:: stwcs.wcsutil.altwcs
  :no-heading:
