""" Unit-tests for wcsdiff module """

from __future__ import absolute_import, division, print_function

import os
from astropy.io import fits

from .. import wcsdiff
from ...tests import data

#-- Pull datafile from repository
DATA_PATH = os.path.split(os.path.abspath(data.__file__))[0]
TEST_FILE = os.path.join(DATA_PATH, 'j94f05bgq_flt.fits')


def test_is_wcs_identical():
    """Simple unittest for checking identical wcs"""
    assert wcsdiff.is_wcs_identical(TEST_FILE,
                                    TEST_FILE,
                                    ('SCI', 1),
                                    ('SCI', 1)), "Found difference from identical file"

def test_get_rootname():
    """Simple unittest for parsing rootname"""
    assert wcsdiff.get_rootname(TEST_FILE) == 'j94f05bgq', 'Rootname parsed incorrectly'

def test_get_extname_extnum():
    """Simple unittest for getting extentsion number"""
    with fits.open(TEST_FILE) as hdu:
        assert wcsdiff.get_extname_extnum(hdu[1]) == ('SCI', 1), 'extension parsed incorrectly'
