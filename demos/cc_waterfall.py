from mine import Minecraft, block

world = Minecraft()

for i in range(10):
    for j in range(10):
        for k in range(10):
            if(i == 9 and j == 8 and k == 9):
                world.setBlock(i, j, k, block.AIR)
            elif(i == 9 and j == 9 and k == 9):
                world.setBlock(i, j, k, block.TNT)
            else:
                world.setBlock(i, j, k, block.WOOD)

for i in range(8):
    for j in range(9):
        for k in range(8):
            world.setBlock(i+1, j+1, k+1, block.WATER)
