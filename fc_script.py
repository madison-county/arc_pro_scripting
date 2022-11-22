# http://geospatialtraining.com/populating-a-feature-class-in-arcgis-pro-using-an-insert-cursor-in-arcpy/
import arcpy
import ctypes

# Create a new feature class
arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")
message_box = ctypes.windll.user32.MessageBoxW

feature_class_name = arcpy.GetParameterAsText(0)
file_path = (arcpy.GetParameterAsText(1)) or (r"C:/Users/jboyk/map_stuff/test_project_2/test_project_2.gdb")

if len(feature_class_name) > 13:
    err = "Error: 13 character limit max for inputs"
    arcpy.AddMessage(err)
    arcpy.AddError(err)
    message_box(None, err, "Character limit error", 0)
else:
    point_fc = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_point'), "POINT", spatial_reference=4326)
    polyline_fc = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_polyline'), "POLYLINE", spatial_reference=4326)
    polygon_fc = arcpy.CreateFeatureclass_management(file_path, (feature_class_name + '_polygon'), "POLYGON", spatial_reference=4326)

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
        ("Ref_Text_1", "String"),
        ("URL_1", "String"),
        ("Ref_Doc_2", "String"),
        ("Ref_Text_2", "String"),
        ("URL_2", "String"),
        ("Notes", "String"),
        ("Comments", "String"),
        ("Townsite1", "String"),
        ("Map_ID", "String"),
        ("Other_No", "String"),
        ("Status", "String"),
        ("Shape_Length", "Double"),
        ("Shape_Area", "Double")
    ]

    for features in feature_class_list:
        for field in fields:
            arcpy.AddField_management(*(features,) + field)