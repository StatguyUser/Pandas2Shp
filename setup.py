from setuptools import setup
import os
import sys

if sys.version_info[0] < 3:
    with open('README.rst') as f:
        long_description = f.read()
else:
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()


setup(
    name='Pandas2Shp',
    version='0.0.2',
    description='Create shp file for geo-spatial analysis from longitude and latitude',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author='StatguyUser',
    url='https://github.com/StatguyUser/Pandas2Shp',
    install_requires=['geopandas','pandas'],
    download_url='https://github.com/StatguyUser/Pandas2Shp.git',
    py_modules=["Pandas2Shp"],
    package_dir={'':'src'},
)
