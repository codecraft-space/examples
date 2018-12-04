# opis (funkcje + petle)
from mine import Minecraft, block

minecraft = Minecraft()


def kupa_z_dynamitem(start):
    minecraft.setBlock(start, 0, 0, block.TNT)
    minecraft.setBlock(start + 1, 0, 0, block.TNT)
    minecraft.setBlock(start + 2, 0, 0, block.TNT)
    minecraft.setBlock(start + 3, 0, 0, block.REDSTONE_TORCH_ACTIVE)


for i in range(100):
    if i == 0:
        kupa_z_dynamitem(i)
    elif i == 10:
        kupa_z_dynamitem(i)
    elif i == 20:
        kupa_z_dynamitem(i)
    elif i == 30:
        kupa_z_dynamitem(i)
    elif i == 40:
        kupa_z_dynamitem(i)
    elif i == 50:
        kupa_z_dynamitem(i)
    elif i == 60:
        kupa_z_dynamitem(i)
    elif i == 70:
        kupa_z_dynamitem(i)
    elif i == 80:
        kupa_z_dynamitem(i)
    elif i == 90:
        kupa_z_dynamitem(i)
