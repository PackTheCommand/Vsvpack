from Vsvpack import *
#get Script path
path1=absoluteScriptFolderPath().get(__file__)

saveFile=vsvpack(path1,"I_am_a_SaveFile")
#create File
saveFile.new(False)
#Add save value
saveFile.add("Test","TestValue")
#read Variable Value
print(saveFile.read("Test"))
#remove saveValue
saveFile.remove("Test")
# to destroy (make unusable) you can use(but you shouldn't): saveFile.aVoidValue()

