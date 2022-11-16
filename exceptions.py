# https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/error-handling-with-python.htm
# https://community.esri.com/t5/python-questions/using-arcpy-try-except-statement/td-p/258384
# https://gis.stackexchange.com/questions/40489/adding-popup-message-box-before-tool-execution-with-arcpy-and-arcmap

import arcpy
import sys
import ctypes

MessageBox = ctypes.windll.user32.MessageBoxW

try:
    # Proper use of the Buffer_analysis() tool
    #arcpy.Buffer_analysis("C:/Users/jboyk/map_stuff/test_project_1/Cemeteries.shp", "C:/Users/jboyk/map_stuff/test_project_1/Cemeteries_buffer.shp", 10)

    # Improper use of the Buffer_analysis() tool - Intentional Fail for the exception clause
    arcpy.Buffer_analysis("C:/Users/jboyk/map_stuff/test_project_1/Cemeteries.shp", "C:/Users/jboyk/map_stuff/test_project_1/Cemeteries_buffer.shp")

except Exception:
    e = sys.exc_info()[1]
    print(e.args[0])

    # If using this code within a script tool, AddError() can be used to return messages
    # back to a script tool. If not, AddError() will have no effect.
    arcpy.AddMessage("Error Encountered: ")
    arcpy.AddError(e.args[0])
    MessageBox(None, (e.args[0]), "Exception Caught", 0)
