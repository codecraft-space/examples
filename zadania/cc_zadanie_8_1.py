# opis
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock', zbuduj ceglane schody (BRICK_BLOCK)
# Startujac z pozycji 0 0 0.
# Schody powinny miec wysokosc 100 elementow

from mine import Minecraft, block

mc = Minecraft()

for i in range(100):
    mc.setBlock(i, i, 0, block.BRICK_BLOCK)
    mc.setBlock(i + 1, i, 0, block.BRICK_BLOCK)
