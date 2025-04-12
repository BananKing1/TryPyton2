"""
Olika sorters djur kan beskrivas med hjälp av klasser och arv. Definiera några olika djur. Utgå från en 
superklass Djur och låt de olika djuren vara subklasser till denna. Använd mellanliggande klasser som t.ex.  
Däggdjur, Kräldjur, Fågel etc. Låt klassen Djur ha en metod läte som beskriver hur ett djur låter. 
Implementera denna metod i de olika subklasserna. 

Deklarera sedan en lista med djur och skriv satser för att löpa igenom listan och låta alla djur i den ge 
ifrån sig ett läte. 
"""
# Superklass
class Djur:
    def läte(self):
        raise NotImplementedError("Denna metod ska implementeras i subklassen.")

# Mellanklasser
class Däggdjur(Djur):
    pass

class Kräldjur(Djur):
    pass

class Fågel(Djur):
    pass

# Specifika djurklasser
class Hund(Däggdjur):
    def läte(self):
        return "Voff!"

class Katt(Däggdjur):
    def läte(self):
        return "Mjau!"

class Orm(Kräldjur):
    def läte(self):
        return "Sss!"

class Uggla(Fågel):
    def läte(self):
        return "Ho-ho!"

# Skapa en lista med djur
djur_lista = [Hund(), Katt(), Orm(), Uggla()]

# Låt alla djur ge ifrån sig sitt läte
for djur in djur_lista:
    print(djur.läte())
