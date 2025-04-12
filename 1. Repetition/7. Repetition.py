"""
I denna uppgift behöver vi använda principen att lägga in dictionaries i en lista. Detta kommer vi gå 
igenom i genomgången tillämpningar av dictionaries. Fundera gärna innan om ni kan komma på hur vi kan 
lösa detta.

a) Skapa ett program där du skall skriva in deltagare till en golftävling. Menyn kan se ut som följande:
1. Mata in deltagare
2. Visa alla deltagare
3. Sök efter deltagare
4. Avsluta

Varje deltagare skall ha ett namn samt handicap (Dessa är siffror mellan 0-52). Dessa matas in under
“Mata in deltagare” och sparas i en lista som du sedan använder dig av för att visa alla eller söka 
efter deltagare.
"""

Deltagare = []

while True:
    print("Vad vill du göra?")
    print("[A] Tillägg deltagare")
    print("[B] Sök deltagare")
    print("[C] Visa alla deltagare")
    svar = input("Svar: ")
    
    if svar == 'A' or svar == 'a':
        Deltagare.append(input("Ange en deltagare: "))

    elif svar == 'B' or svar == 'b':
        sökning = input("Vem letar du efter? ")
        for deltagare in Deltagare:
            if deltagare == sökning:
                print(sökning, "finns med i listan. ")
            else:
                print(sökning, "finnns inte med i listan. ")

    elif svar == 'C' or svar == 'c':
        print(Deltagare)

    else:
        print("Så får du inte göra, försök igen.")
