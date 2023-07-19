import os
import sys
import arcpy
inpath = arcpy.GetParameterAsText(0)
outgdb = arcpy.GetParameterAsText(1)

arcpy.env.workspace=inpath
workspaces = arcpy.ListWorkspaces("*", "FileGDB")
for j, workspace in enumerate(workspaces):
    print('processing: ' + workspace)
    arcpy.env.workspace = workspace
    featureclasses = arcpy.ListFeatureClasses()
    for i, fc in enumerate(featureclasses):
        output = os.path.join(outgdb, os.path.splitext(fc)[0])
        arcpy.Append_management(fc, output)
print('Finished.')