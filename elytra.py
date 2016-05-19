from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random

x = 43
y = 256
z = 765
mc.player.setTilePos(x, y, z)
