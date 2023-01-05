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
    # Potential to add additional FIELDS
        # Have or not have an ALIAS
        # AKA_1 == AKA 1 (with additional characters if needed)
    fields = [
        #field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain}
		("Label", "String", None, None, None, None, "NULLABLE", None, None),
		("Link_Base", "String", None, None, None, None, "NULLABLE", None, None),
		("Link_Part", "String", None, None, None, None, "NULLABLE", None, None),
		("Link", "String", None, None, None, None, "NULLABLE", None, None),
		("FULLROADNA", "String", None, None, None, "Full Road Name", "NULLABLE", None, None),
		("AKA", "String", None, None, None, None, "NULLABLE", None, None),
		("AKA_1", "String", None, None, None, None, "NULLABLE", None, None),
		("AKA_2", "String", None, None, None, None, "NULLABLE", None, None),
		("AKA_3", "String", None, None, None, None, "NULLABLE", None, None),
		("Feature_Na", "String", None, None, None, "Feature Name", "NULLABLE", None, None),
		("Book", "Double", None, None, None, None, "NULLABLE", None, None),
		("Feature_No", "String", None, None, None, None, "NULLABLE", None, None),
		("Township", "Double", None, None, None, None, "NULLABLE", None, None),
		("T_Directio", "String", None, None, None, "Township Direction", "NULLABLE", None, None),
		("Range", "Double", None, None, None, None, "NULLABLE", None, None),
		("R_Directio", "String", None, None, None, "Range Direction", "NULLABLE", None, None),
		("Section", "String", None, None, None, None, "NULLABLE", None, None),
		("TRS_Label", "String", None, None, None, "TRS Label", "NULLABLE", None, None),
		("Feature_Ty", "String", None, None, None, None, "NULLABLE", None, None),
		("County_Roa", "String", None, None, None, "County Road", "NULLABLE", None, None),
		("Town_Roads", "String", None, None, None, "Town Road", "NULLABLE", None, None),
		("Easement_W", "String", None, None, None, "Easement Width", "NULLABLE", None, None),
		("Map_Name", "String", None, None, None, None, "NULLABLE", None, None),
		("Surveyor", "String", None, None, None, None, "NULLABLE", None, None),
		("Map_Source", "String", None, None, None, "Map Source", "NULLABLE", None, None),
		("Map_Date", "Date", None, None, None, "Map Date", "NULLABLE", None, None),
		("Region_Are", "String", None, None, None, "Region/Area", "NULLABLE", None, None),
		("Ref_Doc_1", "String", None, None, None, None, "NULLABLE", None, None),
		("Ref_Text_1", "String",  None,  None, 3000, None, "NULLABLE", None, None),
		("URL_1", "String", None, None, None, None, "NULLABLE", None, None),
		("Ref_Doc_2", "String", None, None, None, None, "NULLABLE", None, None),
		("Ref_Text_2", "String",  None,  None, 3000, None, "NULLABLE", None, None),
		("URL_2", "String", None, None, None, None, "NULLABLE", None, None),
		("Notes", "String", None, None, None, None, "NULLABLE", None, None),
		("Comments", "String",  None,  None, 3000, None, "NULLABLE", None, None),
		("Townsite1", "String", None, None, None, None, "NULLABLE", None, None),
		("Map_ID", "String", None, None, None, None, "NULLABLE", None, None),
		("Other_No", "String", None, None, None, None, "NULLABLE", None, None),
		("Status", "String", None, None, None, None, "NULLABLE", None, None),
		("Shape_Length", "Double", None, None, None, None, "NULLABLE", None, None),
		("Shape_Area", "Double", None, None, None, None, "NULLABLE", None, None)
    ]

# Auto-Generated add field to feature class with size of 3000
# arcpy.management.AddField("testClass2", "className", "TEXT", None, None, 3000, '', "NULLABLE", "NON_REQUIRED", '')

    for features in feature_class_list:
        for field in fields:
            #if "Ref_Text_1" in field[0]:
                #arcpy.AddMessage("{} found".format(field[0]))
                #arcpy.management.AddField(features, field[0], field[1], None, None, 3000)
            arcpy.AddField_management(*(features,) + field)