#
#  Copyright (c) 2011-2014 Exxeleron GmbH
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os
import sys

from distutils.core import setup

from qpython import __version__

try:
    import numpy as np

    include_dirs = [np.get_include()]
except ImportError:
    include_dirs = []

try:
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
else:
    use_cython = True

if use_cython:
    ext_modules = cythonize('qpython/fastutils.pyx')
else:
    ext_modules = []


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if len(sys.argv) > 0 and sys.argv[len(sys.argv) - 1].startswith('version='):
    __version__ = sys.argv[len(sys.argv) - 1][8:] # NOQA
    del (sys.argv[len(sys.argv) - 1])


setup(name='qPython',
      version=__version__,
      description='kdb+ interfacing library for Python',
      long_description=read('README.rst'),

      author='big xyt GmbH',
      author_email='info@big-xyt.com',
      url='http://github.com/bigxyt/qPython',
      license='Apache License Version 2.0',

      ext_modules=ext_modules,
      include_dirs=include_dirs,

      keywords=['kdb+', 'q'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Financial and Insurance Industry',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12'
          'Topic :: Database :: Front-Ends',
          'Topic :: Scientific/Engineering',
          'Topic :: Software Development',
      ],
      packages=['qpython'],
      package_data={'qpython': ['fastutils.pyx']},
      data_files=[('', ['LICENSE', 'CHANGELOG.txt', 'README.rst', 'requirements.txt'])]
      )
