#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# setup.py - distutils configuration for pygoocanvas


'''Python Bindings for the GooCanvas library.

PyGooCanvas is a set of bindings for the GooCanvas library.'''


import os
import sys
import glob

from distutils.command.build import build
from distutils.core import setup


# Check for windows platform
if sys.platform != 'win32':
    msg =  '*' * 68 + '\n'
    msg += '* Building PyGTK using distutils is only supported on windows. *\n'
    msg += '* To build PyGTK in a supported way, read the INSTALL file.    *\n'
    msg += '*' * 68
    raise SystemExit(msg)

# Check for python version
MIN_PYTHON_VERSION = (2, 6, 0)

if sys.version_info[:3] < MIN_PYTHON_VERSION:
    raise SystemExit('ERROR: Python %s or higher is required, %s found.' % (
                         '.'.join(map(str,MIN_PYTHON_VERSION)),
                         '.'.join(map(str,sys.version_info[:3]))))

# Check for pygobject (dsextras)
try:
    from dsextras import GLOBAL_MACROS, GLOBAL_INC, get_m4_define, getoutput, \
                         have_pkgconfig, pkgc_version_check, pkgc_get_defs_dir, \
                         PkgConfigExtension, Template, TemplateExtension, \
                         BuildExt, InstallLib, InstallData
except ImportError:
    raise SystemExit('ERROR: Could not import dsextras module: '
                     'Make sure you have installed pygobject.')

# Check for pkgconfig
if not have_pkgconfig():
    raise SystemExit('ERROR: Could not find pkg-config: '
                     'Please check your PATH environment variable.')

PYGTK_SUFFIX = '2.0'
PYGTK_SUFFIX_LONG = 'gtk-' + PYGTK_SUFFIX
PYGTK_DEFS_DIR = pkgc_get_defs_dir('pygtk-%s' % PYGTK_SUFFIX)

GOOCANVAS_REQUIRED = get_m4_define('goocanvas_required_version')
PYCAIRO_REQUIRED   = get_m4_define('pycairo_required_version')
PYGOBJECT_REQUIRED = get_m4_define('pygobject_required_version')
PYGTK_REQUIRED     = get_m4_define('pygtk_required_version')

MAJOR_VERSION = int(get_m4_define('pygoocanvas_major_version'))
MINOR_VERSION = int(get_m4_define('pygoocanvas_minor_version'))
MICRO_VERSION = int(get_m4_define('pygoocanvas_micro_version'))
VERSION = '%d.%d.%d' % (MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

GLOBAL_INC += ['.']
GLOBAL_MACROS += [('PYGOOCANVAS_MAJOR_VERSION', MAJOR_VERSION),
                  ('PYGOOCANVAS_MINOR_VERSION', MINOR_VERSION),
                  ('PYGOOCANVAS_MICRO_VERSION', MICRO_VERSION),
                  ('VERSION', '\\"%s\\"' % VERSION),
                  ('PLATFORM_WIN32', 1),
                  ('HAVE_BIND_TEXTDOMAIN_CODESET', 1)]

CONFIG_FILE    = 'config.h'
DEFS_DIR       = os.path.join('share', 'pygtk', PYGTK_SUFFIX, 'defs')
HTML_DIR       = os.path.join('share', 'gtk-doc', 'html', 'pygoocanvas')


data_files = []
ext_modules = []
py_modules = []
packages = []


class PyGooCanvasInstallData(InstallData):
    def run(self):
        self.add_template_option('VERSION', VERSION)
        self.prepare()

        # Install templates
        self.install_templates()

        InstallData.run(self)

    def install_templates(self):
        self.install_template('pygoocanvas.pc.in',
                              os.path.join(self.install_dir, 'lib','pkgconfig'))


class PyGooCanvasBuild(build):
    def run(self):
        self.createconfigfile()
        build.run(self)

    def createconfigfile(self):
        with open(CONFIG_FILE, 'w') as fo:
            fo.write ('// Configuration header created by setup.py - do not edit\n' \
                      '#ifndef _CONFIG_H\n' \
                      '#define _CONFIG_H 1\n' \
                      '\n' \
                      '#define PYGOOCANVAS_VERSION_MAJOR %s\n' \
                      '#define PYGOOCANVAS_VERSION_MINOR %s\n' \
                      '#define PYGOOCANVAS_VERSION_MICRO %s\n' \
                      '#define VERSION "%s"\n' \
                      '\n' \
                      '#endif // _CONFIG_H\n' % (MAJOR_VERSION,
                                                 MINOR_VERSION,
                                                 MICRO_VERSION,
                                                 VERSION))


goocanvas = TemplateExtension(name='goocanvas',
                              pkc_name=('pycairo',
                                        'pygobject-%s' % PYGTK_SUFFIX,
                                        'pygtk-%s' % PYGTK_SUFFIX,
                                        'goocanvas'),
                              pkc_version=(PYCAIRO_REQUIRED,
                                           PYGOBJECT_REQUIRED,
                                           PYGTK_REQUIRED,
                                           GOOCANVAS_REQUIRED),
                              defs='goocanvas.defs',
                              register=(os.path.join(PYGTK_DEFS_DIR, 'gdk-types.defs').replace('\\', '/'),
                                        os.path.join(PYGTK_DEFS_DIR, 'pango-types.defs').replace('\\', '/'),
                                        os.path.join(PYGTK_DEFS_DIR, 'gtk-types.defs').replace('\\', '/')),
                              override='goocanvas.override',
                              sources=['goocanvasmodule.c', 'goocanvas.c'],
                              load_types='arg-types.py',
                              py_ssize_t_clean=True)

if goocanvas.can_build():
    ext_modules.append(goocanvas)
    data_files.append((DEFS_DIR, ('goocanvas.defs',)))
    data_files.append((HTML_DIR, glob.glob('docs/html/*.html')))
else:
    raise SystemExit('ERROR: Nothing to do, goocanvas could not be built and is essential.')

doclines = __doc__.split('\n')
options = {'bdist_wininst': {'install_script': 'pygoocanvas_postinstall.py'}}

setup(name='pygoocanvas',
      url='http://live.gnome.org/PyGoocanvas',
      version=VERSION,
      license='LGPL',
      platforms=['MS Windows'],
      maintainer='Gian Mario Tagliaretti',
      maintainer_email='gianmt@gnome.org',
      description = doclines[0],
      long_description = '\n'.join(doclines[2:]),
      provides = 'pygoocanvas',
      requires = ['pycairo (>=%s)' % PYCAIRO_REQUIRED,
                  'pygobject (>=%s)' % PYGOBJECT_REQUIRED,
                  'pygtk (>=%s)' % PYGTK_REQUIRED],
      py_modules=py_modules,
      packages=packages,
      ext_modules=ext_modules,
      data_files=data_files,
      scripts = ['pygoocanvas_postinstall.py'],
      options=options,
      cmdclass={'install_data': PyGooCanvasInstallData,
                'build_ext': BuildExt,
                'build': PyGooCanvasBuild})
