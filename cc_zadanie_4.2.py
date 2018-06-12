# opis
# Zmieniajac parametry 1 (szerokosc) i 2 (wysokosc) polecenia 'setBlock', zbuduj piaskowa ściane (RED_SAND)
# Startujac z pozycji 0 0 0. 
# Sciana powinna miec wysokosc 20 elementow i szerokosc 100

from mine import Minecraft, block

mc = Minecraft()


for wysokosc in range(100):
    mc.setBlock(0, wysokosc, 0, block.RED_SAND)
