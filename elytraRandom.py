from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

x = random.randint(1, 10000)
y = random.randint(256, 512)
z = random.randint(1, 10000)

mc.player.setTilePos(x, y, z)
