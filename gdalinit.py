# __init__ for osgeo package.
import os
import sys

# making the osgeo package version the same as the gdal version:
from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gdal', [dirname(__file__)])
        except ImportError:
            import _gdal
            return _gdal
        if fp is not None:
            try:
                _mod = imp.load_module('_gdal', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gdal = swig_import_helper()
    del swig_import_helper
else:
    import _gdal

__version__ = _gdal.__version__ = _gdal.VersionInfo("RELEASE_NAME")

# Set gdal and proj data directories.
try:
    _here = os.path.dirname(__file__)
    if _here not in os.environ['PATH']:
        os.environ['PATH'] = _here + ';' + os.environ['PATH']
    if 'GDAL_DATA' not in os.environ:
        os.environ['GDAL_DATA'] = os.path.join(_here, 'data', 'gdal')
    if 'PROJ_LIB' not in os.environ:
        os.environ['PROJ_LIB'] = os.path.join(_here, 'data', 'proj')
    if 'GDAL_DRIVER_PATH' not in os.environ:
        pass
        # uncomment the next line to enable plugins
        #os.environ['GDAL_DRIVER_PATH'] = os.path.join(_here, 'gdalplugins')
    os.add_dll_directory(_here)
except Exception:
    pass
