# opis (funkcje)
from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

def klocek_nad_ziema(wyskosc):
    minecraft.setBlock(x, y + wyskosc, z, block.BRICK_BLOCK)


klocek_nad_ziema(5)
klocek_nad_ziema(10)
klocek_nad_ziema(15)
