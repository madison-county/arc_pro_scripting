import arcpy

# Create a Describe object from the feature class
feature_class = arcpy.GetParameterAsText(0)
desc = arcpy.Describe(feature_class)

# Print some feature class properties
print("%-22s %s %s" % ("Feature type", ":", str(desc.featureType)))
print("%-22s %s %s" % ("Shape type", ":", str(desc.shapeType)))
print("%-22s %s %s" % ("Spatial Index", ":", str(desc.hasSpatialIndex)))

if desc.hasOID:
    print("%-22s %s %s" % ("OIDFieldName", ":", str(desc.OIDFieldName)))

#arcpy.AddMessage()
# Print the names and types of all fields in the table
for field in desc.fields:
    arcpy.AddMessage("%-22s %s %s" % (field.name, ":", field.type))
