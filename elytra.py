from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat("Go to y = 100 or above to fly!")

while True:
  
  mc.player.getPos()

  if y >= 100:
    mc.player.getPos()
  
    x = pos.x
    y = 512
    z = pos.y
  
    mc.player.setTilePos(x, y, z)
    
    break
