from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

mc.postToChat("Go to y = 100 or above to fly!")

if y >= 100:
  x = random.randint(1, 10000)
  y = random.randint(256, 512)
  z = random.randint(1, 10000)

  mc.player.setTilePos(x, y, z)
