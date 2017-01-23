from __future__ import absolute_import, division, print_function

from astropy.io import fits

from .. import hstwcs

def test_default_wcsname():
    valid_idcnames = ['root_idc.fits',
                      '/user/gsame/root_idc.fits',
                      'root',
                      'root_idc']

    for name in valid_idcnames:
        assert hstwcs.build_default_wcsname(name) == 'IDC_root'

def test_radesys():
    phdr = fits.PrimaryHDU().header
    phdr['refframe'] = 'icrs'
    assert hstwcs.determine_refframe(phdr) == 'ICRS'
    phdr['refframe'] = 'gsc1'
    assert hstwcs.determine_refframe(phdr) == 'FK5'
    phdr['refframe'] = 'other'
    assert hstwcs.determine_refframe(phdr) is None
    phdr['refframe'] = ' '
    assert hstwcs.determine_refframe(phdr) is None
