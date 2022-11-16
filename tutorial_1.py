# https://geospatialtraining.com/create-a-script-tool-in-arcgis-pro-from-a-python-script/
# https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/describing-data.htm

import arcpy

# Create a Describe object from the feature class
desc = arcpy.Describe(r"../../geoPandas/datasets/partial_roads_test_shp/partial_road_centerlines_test.shp")

print("%-22s %s %s" % ("Feature type", ":", str(desc.featureType)))
print("%-22s %s %s" % ("Shape type", ":", str(desc.shapeType)))
print("%-22s %s %s" % ("Spatial Index", ":", str(desc.hasSpatialIndex)))

if desc.hasOID:
    print("%-22s %s %s" % ("OIDFieldName", ":", str(desc.OIDFieldName)))

print()

for field in desc.fields:
    print("%-22s %s %s" % (field.name, ":", field.type))
