print("\nObs! Tom stränga avslutar programmet. \n")

while True:
    namn = input("Ange namn: ")
    nummer = input("Ange nummer: ")

    if not namn or not nummer:  # Om någon av dem är tom, avsluta loopen
        print("\nProgrammet avslutas. ")
        f.close()
        break

    with open('TELE.txt', 'a') as f:  # Använder 'with open' för att hantera filen
        f.write(f"Namn: {namn}\n")
        f.write(f"Telefonnummer: {nummer}\n")

    print("\nKontakt sparad!")  # Bekräftelse för användaren
    input() #inväntar att användaren trycker enter
