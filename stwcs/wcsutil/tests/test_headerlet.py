""" Unit-tests for headerlet module """

from __future__ import absolute_import, division, print_function

import os
from astropy.io import fits

from .. import headerlet
from ...tests import data

#-- Pull datafile from repository
DATA_PATH = os.path.split(os.path.abspath(data.__file__))[0]
TEST_FILE = os.path.join(DATA_PATH, 'j94f05bgq_flt.fits')

class TestIsParBlank():
    def test_valid(self):
        """Test what should be valid strings"""
        valid_pars = ['', ' ', 'INDEF', "None", None]

        for parameter in valid_pars:
            assert headerlet.is_par_blank(parameter) == True


    def test_invalid(self):
        """Test some of what should be invalid strings"""

        invalid_pars = [1, 4.5, 'Python', 'FITS']

        for parameter in invalid_pars:
            assert headerlet.is_par_blank(parameter) == False

def test_headerlet_summary():
    """Simply test that it doesn't fail"""

    headerlet.headerlet_summary(TEST_FILE)
