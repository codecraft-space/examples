# opis (funkcje + petle)
from mine import Minecraft, block

minecraft = Minecraft()

x = minecraft.player.getPos().x
y = minecraft.player.getPos().y
z = minecraft.player.getPos().z

def kupa_z_dynamitem(start):
    minecraft.setBlock(x + start, y, z, block.TNT)
    minecraft.setBlock(x + start + 1, y, z, block.TNT)
    minecraft.setBlock(x + start + 2, y, z, block.TNT)
    minecraft.setBlock(x + start + 3, y, z, block.REDSTONE_TORCH_ACTIVE)


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
