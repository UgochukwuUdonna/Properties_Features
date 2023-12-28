# Name:      Raster Properties Demo
# Purpose:  To show how to retrieve properties from raster files.
# Created:     3-24-2021

print ("Importing modules...")
import arcpy, sys, traceback
try:
    arcpy.env.workspace = r"C:\EsriPress\Python\Data\Colorado"
    # ListRasters ({wild_card}, {raster_type})
    rasters_list = arcpy.ListRasters()
    for a_raster in rasters_list:
        print ("***********************************")
        print ("Raster file: " + a_raster)
        desc = arcpy.Describe(a_raster)
        if desc.dataType == "RasterDataset":
            print ("Permanent raster dataset: "  + str(desc.permanent))
            print ("Compression type: " + desc.compressionType)
            print ("Format: " + desc.format)
            print ("Sensor type: " + desc.sensorType)
            spatref = desc.spatialReference
            print ("Linear units: " + spatref.linearUnitName)
            print ("No. of bands: " + str(desc.bandCount))
            if desc.bandCount == 1:
                print ("\tBand 1 pixel type: " + desc.pixelType)
                print ("\tCell height: " + str(desc.meanCellHeight))
                print ("\tCell width: " + str(desc.meanCellWidth))
            if desc.bandCount == 3:
                band1_desc = arcpy.Describe(a_raster + "\\Layer_1")
                print ("\tBand 1 pixel type: " + band1_desc.pixelType)
                print ("\tBand 1 cell height: " + str(band1_desc.meanCellHeight))
                print ("\tBand 1 cell width: " + str(band1_desc.meanCellWidth))
                print ("\tBand 1 table type: " + band1_desc.tableType)
                band2_desc = arcpy.Describe(a_raster + "\\Layer_2")
                print ("\tBand 2 pixel type: " + band2_desc.pixelType)
                print ("\tBand 2 table type: " + band2_desc.tableType)
                band3_desc = arcpy.Describe(a_raster + "\\Layer_3")
                print ("\tBand 3 pixel type: " + band3_desc.pixelType)
                print ("\tBand 3 table type: " + band3_desc.tableType)
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
