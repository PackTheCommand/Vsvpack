from Vsvpack import *
#from Vsvpack import absoluteScriptFolderPath

#--definitions
filrabsolute=absoluteScriptFolderPath()
saveFile=vsvpack()

#get Script path
usableFilePath=filrabsolute.get(__file__)

#difine File(-setings)
file_name="example_file"
path2=usableFilePath+"\\"+file_name
example_variable="Variable_Name2"


#creating file
saveFile.new(usableFilePath,file_name,True)
#writing Variable to file
saveFile.add(path2,example_variable,"x:"+"y:"+"z")
#reading from file
test=saveFile.read(path2,example_variable)
#removing Variable from file
saveFile.remove(path2,example_variable)
#result:
print(test)

