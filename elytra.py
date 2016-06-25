from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Go to y = 100 or above to fly!")

while True:
  flying = False
  stop = False
  
  pos = mc.player.getPos()
  
  x = pos.x
  y = pos.y
  z = pos.z

  if y >= 100 and flying == False:
    flying = True
    
    mc.postToChat("Now flying!")
    
    mc.player.getPos()
  
    x = pos.x
    y = 512
    z = pos.y
  
    mc.player.setTilePos(x, y, z)
    
    mc.player.getPos()
    
    if y >= 100 and flying == True and stop == False:
      flying = False
      
      stop = true
      
      mc.postToChat("Go to y = 100 or above to fly again!")
