#!/usr/bin/env python
# coding: utf-8

# In[333]:


import geopandas as gpd
import pandas as pd
class Pandas2Shp:
    '''
    longitude: Pandas series or dataframe column or numpy array or python list. It should contain longitude
    latitude: Pandas series or dataframe column or numpy array or python list. It should contain latitude
    output_path: Directory where you want to save the shape file.
    file_name: File name to be kept for shape file in the given output path.
    '''
    def __init__(self,longitude,latitude,output_path,file_name):
        self.longitude=longitude
        self.latitude=latitude
        self.output_path=output_path
        self.file_name=file_name

    def getShp(self):
        pd_data=pd.DataFrame({'Lon':self.longitude,'Lat':self.latitude})
        gdf_data=gpd.GeoDataFrame(pd_data,geometry=gpd.points_from_xy(pd_data['Lon'],pd_data['Lat']))
        ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'
        # Save the file as an ESRI Shapefile
        gdf_data.to_file(filename = str(self.output_path)+str(self.file_name)+'.shp', driver = 'ESRI Shapefile', crs = ESRI_WKT)

        print('Files generated and saved successully')


if __name__=="__main__":
    longitude=[-14.394,-9.03,-25.171,-6.712000000000001,-7.932,-8.445,-8.47,-9.355,-7.48,-7.888999999999999,-31.131,-7.966,-28.03,-28.715999999999998,-27.093000000000004,-8.887,-9.036,-25.698,-28.44,-8.584]
    latitude=[-7.968999999999999,38.883,36.971,41.868,38.079,41.586999999999996,40.157,38.725,40.265,38.533,39.455,37.014,39.092,38.52,38.764,39.830999999999996,38.704,37.741,38.554,37.149]
    output_path='/home/azim/Downloads/Grad/'
    file_name='airports'

    myObj=Pandas2Shp(longitude,latitude,output_path,file_name)
    myObj.getShp()

