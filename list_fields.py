## Slim Results
fields = arcpy.ListFields(fc)
for field in fields:
    print("{0}, is a type of ,{1}, with a length of ,{2}"
          .format(field.name, field.type, field.length))

## Detailed Results
# Short CSV Expression
fields = arcpy.ListFields(fc)
print('name; aliasName; domain; editable; isNullable; required; length; type; scale; precision;')
for field in fields:
    print("{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9};"
    .format(field.name, field.aliasName, field.domain, field.editable, field.isNullable, field.required, field.length, field.type, field.scale, field.precision,))

## Long Expression
fields = arcpy.ListFields(fc)
for field in fields:
    print("{0}  is the name of the field. {1} is the alias name of the field. {2} is the name of the associated domain. {3} is True, if the field is editable. {4} is True, if the field is nullable. {5} is True, if the field is required. {6} is the field's length. {7} is SmallInteger, Integer, Single, Double, String, Date, OID, Geometry, BLOB. {8} is the field's scale. {9} is the field's precision."
              .format(field.name, field.aliasName, field.domain, field.editable, field.isNullable, field.required, field.length, field.type, field.scale, field.precision,))

## Updated Expression
# Short CSV Expression https://pro.arcgis.com/en/pro-app/latest/arcpy/classes/field.htm
fc = *Set to dataset path or name*
fields = arcpy.ListFields(fc)
print('name; aliasName; type; isNullable; domain; editable; required; length; scale; precision; defaultValue; ')
for field in fields:
        print("{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}; {8}; {9}; {10};"
    .format(field.name, field.aliasName, field.type, field.isNullable, field.domain, field.editable, field.required, field.length, field.scale, field.precision, field.defaultValue,))
