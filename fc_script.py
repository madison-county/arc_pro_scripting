# http://geospatialtraining.com/populating-a-feature-class-in-arcgis-pro-using-an-insert-cursor-in-arcpy/
import arcpy
import ctypes

# Create a new feature class
arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")
message_box = ctypes.windll.user32.MessageBoxW

feature_class_name = arcpy.GetParameterAsText(0)
file_path = (arcpy.GetParameterAsText(1)) or (r"C:/Users/jboyk/map_stuff/")

if len(feature_class_name) > 13:
    err = "Error: 13 character limit max for inputs"
    arcpy.AddMessage(err)
    arcpy.AddError(err)
    message_box(None, err, "Character limit error", 0)
else:
    point_shp = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_point'), "POINT", spatial_reference=4326)
    polyline_shp = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_polyline'), "POLYLINE", spatial_reference=4326)
    polygon_shp = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_polygon'), "POLYGON", spatial_reference=4326)

    feature_class_list = [point_shp, polyline_shp, polygon_shp]

    # Set field variables
    fields = [
        ("Country", "Text"),
        ("State", "Text"),
        ("Town", "Text"),
        ("Township", "Text")
    ]

    for features in feature_class_list:
        for field in fields:
            arcpy.AddField_management(*(features,) + field)