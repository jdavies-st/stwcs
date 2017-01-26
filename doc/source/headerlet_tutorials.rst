Using Headerlets
****************

Creating Headerlets
-------------------
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

Headerlets can also be written straight to an output file:

>>> from stwcs.wcsutil import headerlet
>>>

Locating and Viewing Headerlets
-------------------------------


Manipulating Headerlets
-----------------------
