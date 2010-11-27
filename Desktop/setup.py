"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

# Copyright(C) 2010.  Free Stream Media Corp.  Released under the terms of
# GNU General Public License version 2.0.
# See http://www.gnu.org/licenses/gpl-2.0.html
import sys
import os


DATA_FILES = ['flingo.png', 'flingo.conf']

if sys.platform == 'darwin':
    from setuptools import setup, extension
    APP = ['flingo.py']
    OPTIONS = {'argv_emulation': True, 'iconfile': 'flingo.icns', 'includes': ['sip', 'PyQt4']}
    REC = ['py2app', 'Twisted']  #, 'qt4reactor']
    setup(
        app=APP,
    	data_files=DATA_FILES,
    	options={'py2app':OPTIONS},
    	setup_requires=REC,
    )
else:
    # I get "invalid argument" when I include "bundle_files" : 1 with
    # ms_data as defined using the glob. It doesn't matter whether setup
    # is importaed from distutils.core or setuptools.
    #from distutils.core import setup
    from setuptools import setup, extension
    import py2exe
    from glob import glob
    path = os.path.join(os.getcwd(), r'Microsoft.VC90.CRT')
    ms_data = DATA_FILES + [("Microsoft.VC90.CRT", glob(path + r'\*.*'))]
    #ms_data = DATA_FILES  + ["msvcr90.dll", "msvcp90.dll", "msvcm90.dll", "Manifest.manifest",]
    print "ms_data=", ms_data
    OPTIONS = {"includes" : ["sip", "PyQt4"], "packages" : ["twisted", "qt4reactor"], "bundle_files": 1}

    # The next line compiles, but doesn't bundle an appropriate runtime with the exe.
    #OPTIONS = {"includes" : ["sip", "PyQt4"], "packages" : ["twisted", "qt4reactor"]}
    REC = ["py2exe"]
 
    setup(
        windows=[{"script": "flingo.py", "icon_resources": [(0, "flingo.ico")]}],
        data_files=ms_data,
        options={"py2exe" : OPTIONS},
        zipfile=None,
    )

    print "end of setup.py"

