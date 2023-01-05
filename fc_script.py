# http://geospatialtraining.com/populating-a-feature-class-in-arcgis-pro-using-an-insert-cursor-in-arcpy/
# https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm
# https://pro.arcgis.com/en/pro-app/latest/arcpy/classes/field.htm

import arcpy
import ctypes

# Create a new feature class
arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")
message_box = ctypes.windll.user32.MessageBoxW

STATIC_PATH = (r"C:/Users/jboyk/map_stuff/test_project_2/test_project_2.gdb")
# Get the dataset name from Parameter(0) in ArcGIS
feature_class_name = arcpy.GetParameterAsText(0)
# Get user entered path, if it exists
base_path = arcpy.GetParameterAsText(1)
# If file_path does not exist, create file_path (Check for path validity)
file_path = base_path or STATIC_PATH

def class_creation(file_path, feature_class_name):
    point_fc = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_point'), "POINT", spatial_reference=4326)
    polyline_fc = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_polyline'), "POLYLINE", spatial_reference=4326)
    polygon_fc = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_polygon'), "POLYGON", spatial_reference=4326)
    return point_fc, polyline_fc, polygon_fc

if len(feature_class_name) > 13:
    err = "Error: 13 character limit max for inputs"
    arcpy.AddMessage(err)
    arcpy.AddError(err)
    message_box(None, err, "Character limit error", 0)
else:
    if file_path != STATIC_PATH:
        file_path = arcpy.management.CreateFileGDB(base_path, feature_class_name + ".gdb")
        arcpy.AddMessage("Manual file location supplied - Creating gdb at {}".format(file_path))
    point_fc, polyline_fc, polygon_fc = class_creation(file_path, feature_class_name)
    feature_class_list = [point_fc, polyline_fc, polygon_fc]

    # Set field variables
    fields = [
        ("Link_Base", "String"),
        ("Link_Part", "String"),
        ("Link", "String"),
        ("FULLROADNA", "String"),
        ("AKA", "String"),
        ("AKA_1", "String"),
        ("AKA_2", "String"),
        ("AKA_3", "String"),
        ("Feature_Na", "String"),
        ("Book", "Double"),
        ("Feature_No", "String"),
        ("Township", "Double"),
        ("T_Directio", "String"),
        ("Range", "Double"),
        ("R_Directio", "String"),
        ("Section", "String"),
        ("Feature_Ty", "String"),
        ("County_Roa", "String"),
        ("Town_Roads", "String"),
        ("Easement_W", "String"),
        ("Map_Name", "String"),
        ("Surveyor", "String"),
        ("Map_Source", "String"),
        ("Map_Date", "Date"),
        ("Region_Are", "String"),
        ("Ref_Doc_1", "String"),
        # Increase size to 3000
        ("Ref_Text_1", "String"),
        ("URL_1", "String"),
        ("Ref_Doc_2", "String"),
        # Increase size to 3000
        ("Ref_Text_2", "String"),
        ("URL_2", "String"),
        ("Notes", "String"),
        # Increase size to 3000
        ("Comments", "String", 3000),
        ("Townsite1", "String"),
        ("Map_ID", "String"),
        ("Other_No", "String"),
        ("Status", "String"),
        ("Shape_Length", "Double"),
        ("Shape_Area", "Double")
    ]

    for features in feature_class_list:
        for field in fields:
            if "Ref_Text_1" in field[0]:
                arcpy.AddMessage("{} found".format(field[0]))
            arcpy.AddField_management(*(features,) + field)