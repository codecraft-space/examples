# opis (funkcje)
from mine import Minecraft, block

mc = Minecraft()


def klocek_nad_ziema(wyskosc):
    mc.setBlock(0, wyskosc, 0, block.BRICK_BLOCK)
    mc.setBlock(0, wyskosc + 1, 0, block.BRICK_BLOCK)
    mc.setBlock(0, wyskosc + 2, 0, block.BRICK_BLOCK)


klocek_nad_ziema(5)
klocek_nad_ziema(10)
klocek_nad_ziema(15)
