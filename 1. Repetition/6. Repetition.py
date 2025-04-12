def Rubrik():
    print('Medelvärde av 3 tal')

def medelvärde(tal1, tal2, tal3):
    medel = (tal1 + tal2 + tal3) / 3
    return medel

def main():
    Rubrik()  # Anropa bara Rubrik utan print

    tal1 = int(input("Ange tal 1: "))
    tal2 = int(input("Ange tal 2: "))
    tal3 = int(input("Ange tal 3: "))

    print("Medelvärde: ", medelvärde(tal1, tal2, tal3))

main()
