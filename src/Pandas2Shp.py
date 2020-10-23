import geopandas as gpd
import pandas as pd

def df_to_gdf(df:pd.DataFrame, x_col:str='longitude', y_col:str='latitude', crs=4326):
    """
    Converts from a Pandas DataFrame to a GeoPandas GeoDataFrame,
    This is then saved to the specified filepath

    Parameters
    ----------
    df
        Dataframe containing the passed 
        x_col and y_col as columns
    x_col
        Name of the x coordinate column
    y_col
        Name of the y coordinate column
    crs
        Coordinate reference system, must
        be able to be understood by GeoPandas

    Returns
    -------
    gdf
        GeoDataFrame containing the original 
        data with an additional column containing
        the geometries of the passed points
        
    """
    
    geometry = gpd.points_from_xy(df[x_col], df[y_col])
    gdf = gpd.GeoDataFrame(df_city_lon_lats, crs=crs, geometry=geometry)
    
    return gdf

def pandas_to_shp(df:pd.DataFrame, filepath:str, x_col:str='longitude', y_col:str='latitude', crs=4326):
    """
    Converts from a Pandas DataFrame to a GeoPandas GeoDataFrame,
    This is then saved to the specified filepath

    Parameters
    ----------
    df
        Dataframe containing the passed 
        x_col and y_col as columns
    filepath
        filepath where the resulting 
        shapefile will be saved
    x_col
        Name of the x coordinate column
    y_col
        Name of the y coordinate column
    crs
        Coordinate reference system, must
        be able to be understood by GeoPandas

    Returns
    -------
    gdf
        GeoDataFrame containing the original 
        data with an additional column containing
        the geometries of the passed points
        
    """
    
    gdf = df_to_gdf(df, x_col=x_col, y_col=y_col, crs=crs)
    gdf.to_file(filepath)
    
    return gdf

if __name__=="__main__":
    longitude=[-14.394,-9.03,-25.171,-6.712000000000001,-7.932,-8.445,-8.47,-9.355,-7.48,-7.888999999999999,-31.131,-7.966,-28.03,-28.715999999999998,-27.093000000000004,-8.887,-9.036,-25.698,-28.44,-8.584]
    latitude=[-7.968999999999999,38.883,36.971,41.868,38.079,41.586999999999996,40.157,38.725,40.265,38.533,39.455,37.014,39.092,38.52,38.764,39.830999999999996,38.704,37.741,38.554,37.149]

    df = pd.DataFrame({'latitude':latitude, 'longitude':longitude})
    gdf = pandas_to_shp(df, 'locations.shp')
