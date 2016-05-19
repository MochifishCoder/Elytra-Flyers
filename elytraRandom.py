from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

x = random.randint(1, 10000)
y = random.randint(80, 256)
z = random.randint(1, 10000)

mc.player.setTilePos(x, y, z)
