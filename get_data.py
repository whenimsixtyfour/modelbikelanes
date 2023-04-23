# city of chicago data portal bike routes data:
# https://data.cityofchicago.org/Transportation/Bike-Routes/3w5d-sru8
# will need to decide on data type

# getting OSM data from Open Streets using osmnx
# note: must active via conda active ox
import osmnx as ox
import geopandas 

# get geodata for chicago and test case (lincoln square)
lsq_name = "Lincoln Square, Chicago, IL"
chi_name = 'Chicago, IL'
lsq = ox.geocode_to_gdf(lsq_name)
lsq_geom = ox.geometries_from_place(lsq)

