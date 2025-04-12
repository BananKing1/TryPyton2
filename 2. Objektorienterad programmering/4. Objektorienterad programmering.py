"""
Studera följande kod. Ändra gärna och experimentera och se vad som händer. 
"""

class Spel ():
    def __init__(self, namn, pris, ålder):
        self.namn = namn
        self.pris = pris
        self.ålder = ålder
    def __str__(self):
        return f"Namn: {self.namn}, Pris: {self.pris}, Ålder: {self.ålder}"
 
class Spelbutik (): 
    def __init__(self, namn, adress, spel):
        self.namn = namn
        self.adress = adress
        self.spel = spel
    def __str__(self):
        spel_str = "\n".join([str(s) for s in self.spel])
        return f"Butik Namn: {self.namn}, Adress: {self.adress}\nSpel:{spel_str}"

#skapa objekt
spel1 = Spel("Minecraft", 200, 7)
spel2 = Spel("Fortnite", 300, 12)
spel3 = Spel("PUBG", 400, 16)
spel4 = Spel("League of Legends", 500, 18)
 
#skapa lista
spel = [spel1, spel2, spel3, spel4]
 
#skapa objekt
butik1 = Spelbutik("Gamestop", "Stockholm", spel)
butik2 = Spelbutik("Game", "Göteborg", spel)
butik3 = Spelbutik("Game", "Malmö", spel)
 
print(butik1)
print(butik2)
print(butik3)
 
print (spel1)
print (spel2)
print (spel3)
print (spel4)