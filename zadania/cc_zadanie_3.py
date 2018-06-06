# opis
# Zbuduj wieze skladajaca sie z 5 blokow, w ktorej 1 blok znajduje sie punkcie [0,0,0] 
# Z materialu TNT (dynamit) i wysadz wszystko w powietrze (pochodnia redstone)

from mine import Minecraft, block

mc = Minecraft()

mc.setBlock(0, 0, 0, block.TNT)
mc.setBlock(0, 1, 0, block.TNT)
mc.setBlock(0, 2, 0, block.TNT)
mc.setBlock(0, 3, 0, block.TNT)
mc.setBlock(0, 4, 0, block.TNT)