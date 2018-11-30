# opis
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock', zbuduj ceglane schody (BRICK_BLOCK)
# 1 ) Startujac z pozycji (x, y, z).
# 2 ) Dodaj na osi X kolejny blok aby wypelnic schody.
# Schody powinny miec wysokosc 100 elementow

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

for i in range(100):
    minecraft.setBlock(x + i, y + i, z, block.BRICK_BLOCK)
    minecraft.setBlock(x + i + 1, y + i, z, block.BRICK_BLOCK)
