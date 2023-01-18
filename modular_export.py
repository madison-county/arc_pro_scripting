import arcpy
import ctypes

arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")
message_box = ctypes.windll.user32.MessageBoxW

feature_class_name = arcpy.GetParameterAsText(0)
selection_field = arcpy.GetParameterAsText(1)
field_value = arcpy.GetParameterAsText(2)

def trim_and_export(feature_class_name, selection_field, field_value):
    arcpy.management.CalculateField("{}".format(feature_class_name), "Legal_Loc", '"S " + !Section_s_! + "; T " + !Township! + " " + !T_Directio! + "; R " + !Range!  + " " +  !R_Directio!', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

    new_export = arcpy.conversion.ExportFeatures(feature_class_name, r"C:/Users/jboyk/map_stuff/test_project_2/shp_files/{}_export".format(feature_class_name), 
                                    "{} = {}".format(selection_field, field_value), 
                                    "NOT_USE_ALIAS", 
                                    'Label "Label" true true false 255 Text 0 0,First,#,{},Label,0,255; \
                                    Book "Book" true true false 0 Double 0 0,First,#,{},Book,-1,-1; \
                                    File_Date "File_Date" true true false 50 Text 0 0,First,#,{},File_Date,0,50; \
                                    Legal_Loc "Legal_Loc" true true false 50 Text 0 0, First,#,{},Legal_Loc,0,50; \
                                    Subdivisio "Subdivisio" true true false 254 Text 0 0,First,#,{},Subdivisio,0,254'.format(feature_class_name, 
                                        feature_class_name, 
                                        feature_class_name, 
                                        feature_class_name, 
                                        feature_class_name), 
                                    None)
    message_box(None, "New Shapefile Trimmed and Created", 0)
    return new_export

new_feature = trim_and_export(feature_class_name, selection_field, field_value)

arcpy.AddMessage(new_feature)