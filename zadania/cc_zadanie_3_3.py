# opis
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock', zbuduj ceglane schody (BRICK_BLOCK)
# 1 ) Startujac z pozycji 0 0 0.
# 2 ) Dodaj na osi X kolejny blok aby wypelnic schody. 
# Schody powinny miec wysokosc 100 elementow

from mine import Minecraft, block

minecraft = Minecraft()

for i in range(100):
    minecraft.setBlock(i, i, 0, block.BRICK_BLOCK)
    minecraft.setBlock(i + 1, i, 0, block.BRICK_BLOCK)
