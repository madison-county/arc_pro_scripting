import arcpy
import ctypes

arcpy.env.workspace = (r"C:/Users/jboyk/map_stuff/test_project_2")
message_box = ctypes.windll.user32.MessageBoxW

feature_class_name = arcpy.GetParameterAsText(0)

arcpy.conversion.ExportFeatures("MCMT_Plat_Map", r"C:\Users\jboyk\map_stuff\test_project_2\test_project_2.gdb\MCMT_Plat_Map_ExportFeatures", 
                                "Book = 4", 
                                "NOT_USE_ALIAS", 
                                'Label "Label" true true false 255 Text 0 0,First,#,MCMT_Plat_Map,Label,0,255; \
                                Book "Book" true true false 0 Double 0 0,First,#,MCMT_Plat_Map,Book,-1,-1; \
                                File_Date "File_Date" true true false 50 Text 0 0,First,#,MCMT_Plat_Map,File_Date,0,50; \
                                Township "Township" true true false 50 Text 0 0,First,#,MCMT_Plat_Map,Township,0,50; \
                                T_Directio "T_Directio" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,T_Directio,0,254; \
                                Range "Range" true true false 50 Text 0 0,First,#,MCMT_Plat_Map,Range,0,50; \
                                R_Directio "R_Directio" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,R_Directio,0,254; \
                                Section_s_ "Section_s_" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,Section_s_,0,254; \
                                Subdivisio "Subdivisio" true true false 254 Text 0 0,First,#,MCMT_Plat_Map,Subdivisio,0,254', 
                                None)
