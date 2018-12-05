# petle (loops)
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock',
# zbuduj piaskowa sciane (RED_SAND)
# Startujac z pozycji (x, y, z).
# Sciana powinna miec wysokosc 100 elementow, oraz szerokosc 50 elemento

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

for wysokosc in range(100):
    for szerokosc in range(100):
        minecraft.setBlock(x + szerokosc, y + wysokosc, z, block.RED_SAND)
