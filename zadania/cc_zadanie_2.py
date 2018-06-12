# polecenie "setBlock"
# Uzycie funkcji `mc.setBlock(x, y, z, material)` tak,
# zeby postawic blok (block.GLASS) w centrum swiata (0, 0, 0)

from mine import Minecraft, block

minecraft = Minecraft()

minecraft.setBlock(0, 0, 0, block.GLASS)
