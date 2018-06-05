# opis
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock', zbuduj piaskowa wieze (RED_SAND)
# Startujac z pozycji 0 0 0. 
# Wieza powinna miec wysokosc 500 elementow

from mine import Minecraft, block

mc = Minecraft()


for wysokosc in range(500):
    mc.setBlock(0, wysokosc, 0, block.RED_SAND)
