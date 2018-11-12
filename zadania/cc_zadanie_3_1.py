# petle (loops)
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock',
# zbuduj piaskowa wieze (RED_SAND)
# Startujac z pozycji (x, y, z).
# Wieza powinna miec wysokosc 100 elementow

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

for wysokosc in range(100):
    minecraft.setBlock(x, y + wysokosc, z, block.RED_SAND)
