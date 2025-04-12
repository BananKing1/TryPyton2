filnamn = input("Ange filnamn: ") + ".txt" # Ange 'filnamn.txt'

while True: # evighets loop tills break
    try:
        f = open(filnamn, 'r')  # Öppna filen i läsläge ('r')
        lista = f.readlines()  # Ange innehållet i listan
        
        for n, rader in enumerate(lista):  # Använd enumerate för numrering
            print(n, rader.strip()) # Skriv ut radnumret och innehållet utan extra radbrytning
            input() #inväntar att användaren trycker enter
        
        f.close() # Stäng filen
        print("\nNu är alla rader utskriven!") # medelande att raderna är utskrivna
        break  # bryt loopen
    except FileNotFoundError:
        print("Filen finns inte. Ange ett korrekt filnamn.") # medelande om filen inte finns
        filnamn = input("Ange filnamn: ") + ".txt"  # Be om nytt filnamn
