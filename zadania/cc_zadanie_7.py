# opis
# Zmieniajac drugi (wysokosc) parametr polecenia 'setBlock', zbuduj piaskowa konstrukcje z (BRICK_BLOCK)
# Startujac z pozycji 0 0 0.
# Wieza powinna:
# 1) miec wysokosc 20 elementow
# 2) co 5 blok powinnien byc dynamietem (TNT)

from mine import Minecraft, block

mc = Minecraft()

for i in range(20):
    if i == 5:
        mc.setBlock(0, i, 0, block.BRICK_BLOCK)
    else:
        mc.setBlock(0, i, 0, block.TNT)

