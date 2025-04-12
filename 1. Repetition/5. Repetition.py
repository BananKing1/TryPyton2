"""
Använd metoden .rjust() för att i ett Pythonprogram skriva ut en snygg tabell över alla tal från 1 till 10 med deras kvadrater och kuber. 
(Gör om varje tal för utskrift till en sträng med str() först). 
"""

#huvud tabell
tal = str("tal")
kvadrat = str("kvadrat")
kub = str("kub")

#utskriv huvud tabell
print(tal.rjust(10), kvadrat.rjust(10), kub.rjust(10))

#loop för varje ny rad
for i in range(1, 11):
    
    #räkna + mellan rumm
    tal2 = str(i).rjust(10)
    kvadrat2 = str(i**2).rjust(10)
    kub2 = str(i**3).rjust(10)

    #utskriv
    print(tal2, kvadrat2, kub2)