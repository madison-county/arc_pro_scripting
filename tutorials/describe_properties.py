# https://pro.arcgis.com/en/pro-app/latest/arcpy/functions/describe-object-properties.htm
import arcpy
import ctypes

# Describe a feature class using arcpy.Describe()
inFC = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(inFC)

#desc = arcpy.Describe("C:/Users/jboyk/map_stuff/test_project_1/Cemeteries.shp")

MessageBox = ctypes.windll.user32.MessageBoxW

# Print some Describe() object properties
try:
    if hasattr(desc, "dataElementType"):
        arcpy.AddMessage("Data Type:            " + desc.dataElementType)
    if hasattr(desc, "datasetType"):
        arcpy.AddMessage("Dataset Type:         " + desc.datasetType)
    if hasattr(desc, "extension"):
        arcpy.AddMessage("File Type:            " + desc.extension)
    if hasattr(desc, "path"):
        arcpy.AddMessage("File Path:            " + desc.path)
except arcpy.ExecuteError:
    #arcpy.AddMessage("Something went wrong")
    arcpy.AddMessage(arcpy.GetMessages())
    MessageBox(None, arcpy.GetMessages(), "Window Title", 0)

# Examine children and print their name and dataType
for child in desc.children:
    arcpy.AddMessage("Children")
    arcpy.AddMessage("\t%s = %s" % (child.name, child.dataType))