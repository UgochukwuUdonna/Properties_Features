# Name:      Raster Properties Demo Band Names
# Purpose:  To show how to retrieve properties from raster files.
#               This demo is similar to the Properties Demo script but in this
#               script we are extracting the names of the bands in the raster
#               files instead of manually typing their names.
# Created:     3-24-2023

print ("Importing modules...")
import arcpy, sys, traceback
try:
    seed_path = r"C:\EsriPress\Python\Data\Colorado"
    arcpy.env.workspace = seed_path
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
            arcpy.env.workspace = arcpy.env.workspace + "\\" + a_raster
            bands = arcpy.ListRasters() # GET LIST OF RASTER BANDS
            for a_band in bands:

                print (f"Band name: {a_band}")
                band_desc = arcpy.Describe(a_band)
                print ("\t" + a_band + " pixel type: " + band_desc.pixelType)
                print ("\t" + a_band + " cell height: " + str(band_desc.meanCellHeight))
                print ("\t" + a_band + " cell width: " + str(band_desc.meanCellWidth))
                print ("\t" + a_band + " table type: " + str(band_desc.tableType))

            arcpy.env.workspace = seed_path

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
