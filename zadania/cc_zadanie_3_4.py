# petle (loops)
# Zmieniajac 2 (wysokosc) parametr polecenia 'setBlock',
# zbuduj piaskowa sciane (RED_SAND)
# Startujac z pozycji 0 0 0.
# Sciana powinna miec wysokosc 100 elementow, oraz szerokosc 50 elemento

from mine import Minecraft, block

mc = Minecraft()


for wysokosc in range(100):
    for szerokosc in range(100):
        mc.setBlock(szerokosc, wysokosc, 0, block.RED_SAND)
