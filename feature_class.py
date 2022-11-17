# http://geospatialtraining.com/populating-a-feature-class-in-arcgis-pro-using-an-insert-cursor-in-arcpy/

import arcpy

# Create a new feature class
arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")

new_shapefile = arcpy.CreateFeatureclass_management("C:/Users/jboyk/map_stuff/test_project_2/",
                                                    "points_with_cursor.shp", "POINT", spatial_reference=4326)

# Reference lat/lon, city and country data
rows = [('USA', 'MT', 'Alder', (-112.099540, 45.300630)),
        ('USA', 'MT', 'Virginia City', (-111.94277158600016, 45.293917252358185)),
        ('USA', 'MT', 'Nevada City', (-111.96754142356147, 45.30679129973908)),
        ('USA', 'MT', 'Laurin', (-112.11830673649942, 45.35272213584768))]

# Set fieldname variables
fields = [
    ("Country", "Text"),
    ("State", "Text"),
    ("Town", "Text")
]

for field in fields:
    arcpy.AddField_management(*(new_shapefile,) + field)

# Use insert cursor to insert all fields for each row
with arcpy.da.InsertCursor(new_shapefile, ['Country', 'State', 'Town', 'SHAPE@XY']) as insert_cursor:
    for row in rows:
        insert_cursor.insertRow(row)