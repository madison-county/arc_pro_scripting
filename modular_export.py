import arcpy
import ctypes

arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")
message_box = ctypes.windll.user32.MessageBoxW

feature_class_name = arcpy.GetParameterAsText(0)
selection_field = arcpy.GetParameterAsText(1)
field_value = arcpy.GetParameterAsText(2)

def trim_and_export(feature_class_name, selection_field, field_value):
    new_export = arcpy.management.CalculateField("{}".format(feature_class_name), "Legal_Loc", '"S " + !Section_s_! + "; T " + !Township! + " " + !T_Directio! + "; R " + !Range!  + " " +  !R_Directio!', "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")

    new_export = arcpy.conversion.ExportFeatures(feature_class_name, r"C:/Users/jboyk/map_stuff/test_project_2/shp_files/{}_export".format(feature_class_name), 
                                    "{} = {}".format(selection_field, field_value), 
                                    "NOT_USE_ALIAS", 
                                    'Label "Label" true true false 255 Text 0 0,First,#,MCMT_Plat_Map,Label,0,255; \
                                    Book "Book" true true false 0 Double 0 0,First,#,MCMT_Plat_Map,Book,-1,-1; \
                                    File_Date "File_Date" true true false 50 Text 0 0,First,#,MCMT_Plat_Map,File_Date,0,50; \
                                    Legal_Loc "Legal_Loc" true true false 50 Text 0 0, First,#,MCMT_Plat_Map,Legal_Loc,0,50; \
                                    Subdivisio "Subdivisio" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,Subdivisio,0,254', 
                                    #Township "Township" true true false 50 Text 0 0,First,#,MCMT_Plat_Map,Township,0,50; \
                                    #T_Directio "T_Directio" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,T_Directio,0,254; \
                                    #Range "Range" true true false 50 Text 0 0,First,#,MCMT_Plat_Map,Range,0,50; \
                                    #R_Directio "R_Directio" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,R_Directio,0,254; \
                                    #Section_s_ "Section_s_" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,Section_s_,0,254; \
                                    None)
    return new_export

new_feature = trim_and_export(feature_class_name, selection_field, field_value)

arcpy.AddMessage(new_feature)