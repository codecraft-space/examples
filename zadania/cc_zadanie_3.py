# petle (loops)
# Na czacie Minecraft wyswietl liczby od 0 do 5. Sprawdz zadanie pierwsze aby zobaczyc jak wypisywac na czacie.

from mine import Minecraft

minecraft = Minecraft()

for numer in range(5):
    minecraft.postToChat(str(numer))