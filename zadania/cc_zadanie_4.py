# opis
# Zmieniajac drugi (wysokosc) parametr polecenia 'setBlock', zbuduj piaskowa konstrukcje z (BRICK_BLOCK)
# Startujac z pozycji (x, y, z).
# Wieza powinna:
# 1) miec wysokosc 20 elementow
# 2) co 5 blok powinnien byc dynamietem (TNT)

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

for i in range(20):
    if i == 5:
        minecraft.setBlock(x, y + i, z, block.BRICK_BLOCK)
    else:
        minecraft.setBlock(x, y + i, z, block.TNT)
