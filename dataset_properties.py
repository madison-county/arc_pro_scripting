import arcpy

# Create a Describe object using GetParameterAsText()
inFC = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(inFC)

# Print dataset properties
arcpy.AddMessage(("Dataset Type: {0}".format(desc.datasetType)))
arcpy.AddMessage(("Extent:\n  XMin: {0}, XMax: {1}, YMin: {2}, YMax{3}".format(
    desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax)))
arcpy.AddMessage(("MExtent: {0}".format(desc.MExtent)))
arcpy.AddMessage(("ZExtent: {0}".format(desc.ZExtent)))

arcpy.AddMessage(("Spatial reference name: {0}:".format(desc.spatialReference.name)))
