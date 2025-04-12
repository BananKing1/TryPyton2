"""
Definiera en klass Person som beskriver en person. 
Varje person ska ha ett namn, en adress och 
ett telefonnummer. Låt slutligen programmet skriva 
ut informationen i Person-objektet
"""

class Person:
    def __init__(self, namn, adress, telefonummer):
        self.namn = namn
        self.adress = adress
        self.telefonummer = telefonummer

    def __str__(self):
        return f"Namn: {self.namn}, Adress: {self.adress}, Telefonummer: {self.telefonummer}"
    

Person1 = Person("namn1", "adress1", 123456789)

print(Person1)