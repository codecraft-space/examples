# opis (funkcje)
from mine import Minecraft, block

minecraft = Minecraft()


def klocek_nad_ziema(wyskosc):
    minecraft.setBlock(0, wyskosc, 0, block.BRICK_BLOCK)


klocek_nad_ziema(5)
klocek_nad_ziema(10)
klocek_nad_ziema(15)
