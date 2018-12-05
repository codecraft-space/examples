# polecenie "setBlock"
# Uzycie funkcji `mc.setBlock(x, y, z, material)` tak,
# zeby rozstawic 5 roznych materialow w pozycjach:
# 1) (x, y, z) z materialem block.GLASS
# 2) (x, y + 10, z) z materialem block.WOOD
# 3) (x, y, z + 10) z materialem  block.MELON
# 4) (x, y + 10, z + 10) z materialem block.GOLD_BLOCK
# 5) W dowolnym miejscu, z dowolnym materialem. Znajdz i zaprezentuj
from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

minecraft.setBlock(x, y, z, block.GLASS)
minecraft.setBlock(x, y + 10, z, block.WOOD)
minecraft.setBlock(x, y, z + 10, block.MELON)
minecraft.setBlock(x + 10, y + 10, z + 10, block.GOLD_BLOCK)
