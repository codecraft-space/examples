# opis
# Wyswietlenie napisu "Hello world!" na czacie
from mine import Minecraft, block

mc = Minecraft()

mc.setBlocks(-50, 0, -50, 50, 50, 50, block.AIR)
mc.setBlocks(-50, -5, -50, 50, -1, 50, block.GRASS)
