from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

# flying flag
flying = False
start = 0

mc.postToChat("Go to y = 80 or above to fly!")
# main loop (infinite)
while True:

    # get the player's position
    pos = mc.player.getPos()

    x = pos.x
    y = pos.y
    z = pos.z

    # should we enable flying?
    if flying == False and y >= 80:
        mc.postToChat("Now Flying! Go to y = 80 or below to stop!")
        flying = True
        # remember when we started flying
        start = time.time()

    # are we flying?
    if flying == True:
        # is it time to move the player?
        if time.time() - start > 15:
            x = random.randint(1, 10000)
            y = random.randint(256, 1024)
            z = random.randint(1, 10000)
            mc.player.setTilePos(x, y, z)

            # reset the timer
            start = time.time()

        # time to stop flying?
        elif y <= 80:
            mc.postToChat("No Longer Flying! Go to y = 80 or above to fly again!")
            flying = False

