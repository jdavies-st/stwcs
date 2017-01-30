************
Installation
************

STWCS is distributed through the `Anaconda <https://anaconda.org>`_ package
manager. Specifically, it lives within Space Telescope Science Institute's
`AstroConda <https://astroconda.readthedocs.io/>`_ channel.

If you do not have Anaconda, please follow the `instructions here
<https://www.continuum.io/downloads>`_ to install it, or scroll down for
manual installation of STWCS.


Install via Anaconda
--------------------

If you have AstroConda setup, then all you have to do to install STWCS is
simply type the following at any Bash terminal prompt::

    $ conda install stwcs

If you do not have AstroConda setup, then you can install STWCS by
specifying the channel in your install command::

    $ conda install --channel http://ssb.stsci.edu/astroconda stwcs


Install via source
------------------

STWCS can also be installed manually from the source code.
At your terminal, you may either clone the repository directly and then
install::

    $ git clone https://github.com/spacetelescope/stwcs.git
    $ cd stwcs
    $ python setup.py install
