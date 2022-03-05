from Vsvpack import *
path=r"C:\examples"
path2=r"C:\examples\lokalsave"
saveFile=vsvpack()
object1="Object.cube.ID.1"
saveFile.new(path,"lokalsave",False)
saveFile.add(path2,object1,"x:"+"y:"+"z")
test=saveFile.read(path2,object1)
print(test)

