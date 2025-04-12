filnamn = input("Ange filnamn: ") + ".txt" # Ange 'filnamn.txt'

while True: # evighets loop tills break
    try:
        f = open(filnamn, 'r')  # Öppna filen i läsläge ('r')
        lista = f.readlines()  # Ange innehållet i listan
        
        for rader in lista: #läser ut alla rader i listan
            print(rader)
        
        f.close() # Stäng filen
        print("\nNu är alla rader utskriven!") # medelande att raderna är utskrivna
        break  # bryt loopen
    except FileNotFoundError:
        print("Filen finns inte. Ange ett korrekt filnamn.") # medelande om filen inte finns
        filnamn = input("Ange filnamn: ") + ".txt"  # Be om nytt filnamn
