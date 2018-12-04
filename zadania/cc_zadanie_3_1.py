# petle (loops)
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock',
# zbuduj piaskowa wieze (RED_SAND)
# Startujac z pozycji 0 0 0.
# Wieza powinna miec wysokosc 100 elementow

from mine import Minecraft, block

minecraft = Minecraft()


for wysokosc in range(100):
    minecraft.setBlock(0, wysokosc, 0, block.RED_SAND)
