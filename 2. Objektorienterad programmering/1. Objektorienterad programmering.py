"""
Definiera en klass Bok som beskriver en bok. Varje bok ha en titel, författare, 
ett sidantal och ett pris. 
Skriv sedan ett program i vilket du skapar två objekt av klassen Bok.
Det ena objektet ska initieras så att det
beskriver en bok som du vill och det andra ska beskriva någon annan av dina böcker. 
Låt slutligen programmet skriva ut informationen i Bok-objektet
"""

class Bok:
    def __init__(self, titel, författare, sidantal, pris):
        self.titel = titel
        self.författare = författare
        self.sidantal = sidantal
        self.pris = pris

    def __str__(self):
        return f"Titel: {self.titel}, Författare: {self.författare}, Sidantal: {self.sidantal}, Pris: {self.pris}"

Bok1 = Bok("titel1", "författare1", 100, 100)
Bok2 = Bok("titel2", "författare2", 200, 200)

print(Bok2)