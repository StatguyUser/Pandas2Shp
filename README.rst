What is it?
===========

Pandas2Shp module create shape file using latitude and longitude information from pandas columns or python list. Shape file are needed for geo-spatial data analysis.

Input parameters
================

  - **longitude** Pandas series or dataframe column or numpy array or python list.
  - **latitude** Pandas series or dataframe column or numpy array or python list.
  - **output_path** Directory where you want to save the shape file.
  - **file_name** File name to be kept for shape file in the given output path.

How to use is it?
=================

```python

from Pandas2Shp import Pandas2Shp

long=[-14.394,-9.03,-25.171,-6.712000000000001,-7.932,-8.445,-8.47,-9.355,-7.48,-7.888999999999999,-31.131,-7.966,-28.03,-28.715999999999998,-27.093000000000004,-8.887,-9.036,-25.698,-28.44,-8.584]
lat=[-7.968999999999999,38.883,36.971,41.868,38.079,41.586999999999996,40.157,38.725,40.265,38.533,39.455,37.014,39.092,38.52,38.764,39.830999999999996,38.704,37.741,38.554,37.149]
output_path='/home/user/airport/'
file_name='airports'

myObj=Pandas2Shp(longitude,latitude,output_path,file_name)
myObj.getShp()

```

Where to get it?
================

`pip install Pandas2Shp`

Dependencies
============

 - [geopandas](https://geopandas.org/)
 - [pandas](https://pandas.pydata.org/)

