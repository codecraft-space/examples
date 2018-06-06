# opis
# Na czacie Minecraft wyswietl liczby od 0 do 5. Sprawdz zadanie pierwsze aby zobaczyc jak wypisywac na czacie.
from mine import Minecraft, block

mc = Minecraft()


for numer in range(5):
    mc.postToChat(str(numer))
