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
        return f"Namn: {self.namn}, Adress: {self.adress}, Spel: {self.spel}"


#skapa objekt av klassen Spel
spel1 = Spel("Minecraft", 200, 7)
spel2 = Spel("Fortnite", 300, 12)


#skapa objekt av klassen Spelbutik
spelbutik1 = Spelbutik("Spelbutik1", "Gatan 1", [spel1, spel2])
spelbutik2 = Spelbutik("Spelbutik2", "Gatan 2", [spel1, spel2])

#skapa en lista med alla spelbutiker
spelbutiker = [spelbutik1, spelbutik2]


#skriv ut alla spelbutiker
for spelbutik in spelbutiker:
    print(spelbutik)

for spel in spelbutik.spel:
    print(spel)
print("")