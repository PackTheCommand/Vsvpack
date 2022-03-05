from Vsvpack import *

file_name="example_file"
path=r"C:\<examples_path>"    #<examples_path> requiers a real path

path2=r"C:\<example_path>"+"\\"+file_name     #<examples_path> requiers a real path
example_variable="Variable_Name"

saveFile=vsvpack()

saveFile.new(path,file_name,True)

saveFile.add(path2,example_variable,"x:"+"y:"+"z")

test=saveFile.read(path2,example_variable)

#result:
print(test)

