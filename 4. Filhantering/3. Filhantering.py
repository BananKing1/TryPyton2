lista = [] #skapa lista

with open("TELE.txt", 'r') as f: #öppnar fil
    for rad in f:
        rad = rad.strip() #tar bort extra radbrytningar
        if rad:
            lista.append(rad) #lagrar innehållet i listan

print("\n---TELEFONLISTA---\n") #rubrik

count = len(lista) #antal element i listan
a = (-1) #sätt värden
b = 0 #sätt värden

for i in range(count): #skriver ut listan
    print(lista[a+i], lista[b+i], end = '\n') #skriver element (0+1) och (1+1) med ny rad varje upprepning
    f.close() #stäng fil (klar)
