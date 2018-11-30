# polecenie "setBlock"
# Uzycie funkcji `mc.setBlock(x, y, z, material)` tak,
# zeby postawic blok (block.GLASS) w punkcie (x, y, z),
# czyli tam gdzie stoi gracz

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

minecraft.setBlock(x, y, z, block.GLASS)
