from setuptools import setup, find_packages

long_description = '''
XC_loc: open-source python package built on obspy to locate seismic signals
using envelope cross correlation and a grid search
'''

setup(
  name = 'XC_loc',
  packages = find_packages(),
  version = '1.0',
  license='LGPL',
  description = 'XC_loc - envelope cross-correlation location method',   # Give a short description about your library
  long_description = long_description,
  author = 'Aaron Wech',
  author_email = 'awech@usgs.gov',
  url = 'https://github.com/awech/XC_loc',
  download_url = 'https://github.com/awech/XC_loc/archive/v1.0.tar.gz',    # I explain this later on
  keywords = ['envelope cross correlation', 'seimsology', 'tremor'],
  install_requires=[
          'obspy',
          'numpy',
          'scipy',
          'matplotlib',
          'cartopy',
          'sklearn',
          'utm',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: GNU Library or Lesser General Public',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)