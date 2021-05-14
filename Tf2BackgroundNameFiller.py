import shutil
import os


source = input("Enter target vtf file name: ")
os.rename(source,"1.vtf")
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
createFolder('./TEMP/')
#-------------------------------------------------------------
shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","backgrond_2fort_widescreen.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_2fort.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_gravelpit.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_gravelpit_widescreen.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_mvm.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_mvm_widescreen.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_upward.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_upward_widescreen.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_xmas2011.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","background_xmas2011_widescreen.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","title_fullmoon.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","title_fullmoon_widescreen.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","title_team_halloween.vtf")

shutil.copy("1.vtf","./TEMP//")
os.rename("./TEMP/1.vtf","title_team_halloween_widescreen.vtf")







