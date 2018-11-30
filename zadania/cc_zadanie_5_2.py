# opis (funkcje)
# za pomocą funkcji slup, możesz zbudować słup
# napisz funkcję sciana, która wykorzysta funkcje slup, zeby zbudowac sciane

from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

def slup(slup_x, slup_y, slup_z, wysokosc):
    for i in range(wysokosc):
        minecraft.setBlock(slup_x, slup_y + i, slup_z, block.BRICK_BLOCK)

# def sciana(sciana_x, sciana_y, sciana_z, wysokosc, dlugosc):
#    ...
#    ...

slup(x, y, z, 10)
# sciana(x, y, z, 10, 10)