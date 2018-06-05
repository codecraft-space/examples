# opis
# Uzycie funkcji `mc.setBlock(x, y, z, material)` tak, 
# zeby rozstawic 5 roznych materialow w pozycjach:
# 1) 0, 0, 0 z materialem block.GLASS
# 2) 0, 10, 0 z materialem block.WOOD
# 3) 0, 0, 10 z materialem  block.MELON
# 4) 0, 10, 10 z materialem block.GOLD_BLOCK
# 5) W dowolnym miejscu, z dowolnym materialem. Znajdz i zaprezentuj

from mine import Minecraft, block

mc = Minecraft()

mc.setBlock(0, 0, 0, block.GLASS)
mc.setBlock(0, 10, 0, block.WOOD)
mc.setBlock(0, 0, 10, block.MELON)
mc.setBlock(10, 10, 10, block.GOLD_BLOCK)
