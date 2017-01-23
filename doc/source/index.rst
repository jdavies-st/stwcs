.. STWCS documentation master file, created by
   sphinx-quickstart on Thu Sep 23 09:18:47 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

STWCS
=====
(**S**\ pace **T**\ elescope **W**\ orld **C**\ oordinate **S**\ ystem)

This package provides support for WCS based distortion models and coordinate
transformation. It relies on the `Astropy WCS <http://docs.astropy.org/en/stable/wcs/>`_ package (based on WCSLIB).

It consists of two main modules, ``updatewcs`` and ``wcsutil``. ``updatewcs``
performs corrections to the basic WCS and includes
other distortion infomation in the science files as header keywords or file extensions.
``wcsutil`` provides an HSTWCS object which extends ``astropy.wcs`` object and provides HST instrument
specific information as well as methods for coordinate tarnsformaiton. ``wcsutil`` also provides
functions for manipulating alternate WCS descriptions in the headers.

Contents:
=========

.. toctree::
   :maxdepth: 2

   wcsutil
   updatewcs
   headerlet
   full_api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
