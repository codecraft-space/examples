# polecenie "setBlock"
# Zbuduj wieze skladajaca sie z 5 blokow,
# w ktorej 1 blok znajduje sie punkcie (x, y, z)
# Z materialu TNT (dynamit) i wysadz wszystko w powietrze (pochodnia redstone)

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

minecraft.setBlock(x, y, z, block.TNT)
minecraft.setBlock(x, y + 1, z, block.TNT)
minecraft.setBlock(x, y + 2, z, block.TNT)
minecraft.setBlock(x, y + 3, z, block.TNT)
minecraft.setBlock(x, y + 4, z, block.TNT)
