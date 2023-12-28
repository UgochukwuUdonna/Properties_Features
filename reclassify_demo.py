# reclassify demo

# Created by: Ugochukwu Udonna Okonkwo
# Created on: 3-27-2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    arcpy.env.overwriteOutput = True
    input_raster = r'C:\EsriPress\Python\Data\Colorado\elevation'
    if arcpy.CheckExtension('spatial') == 'Available':
        arcpy.CheckOutExtension('spatial')
        # RemapRange (remapTable)
        remap_range = arcpy.sa.RemapRange( [ [0,2000,1], [2000,3000,2], [3000,4000,3] ] )
        # Reclassify(in_raster, reclass_field, remap, {missing_values})
        out_raster = arcpy.sa.Reclassify(input_raster, 'Value', remap_range)
        print ('Saving raster object...')
        out_raster.save(r'c:\temp\reclass_demo.img')
        arcpy.CheckInExtension('spatial')
    else:
        print ('Spatial Analyst extension not present.')
except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])

    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    print (msgs)
    print (pymsg)

    arcpy.AddMessage(arcpy.GetMessages(1))
    print (arcpy.GetMessages(1))
