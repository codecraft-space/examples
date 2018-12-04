# opis
# Wyswietlenie napisu "Hello world!" na czacie
from mine import Minecraft, block

mc = Minecraft()

a = 50
mc.setBlocks(-a, 0, -a, a, a, a, block.AIR)
mc.setBlocks(-a, -5, -a, a, -1, a, block.GRASS)
