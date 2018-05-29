# opis
# Zmieniajac 3 paramter polecenia 'setBlock', zbuduj szklane schody (GLASS) schody startujac z pozycji 0 0 0. 

from mine import *

mc = Minecraft()

mc.setBlock(0, 0, 0, block.GLASS)
mc.setBlock(0, 1, 1, block.GLASS)
mc.setBlock(0, 2, 2, block.GLASS)
mc.setBlock(0, 3, 3, block.GLASS)
mc.setBlock(0, 4, 4, block.GLASS)