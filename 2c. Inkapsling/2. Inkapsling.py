"""   Studerande Hantering( ͡° ͜ʖ ͡°)   """

class Studerande:
    def __init__(self, namn,ålder, betyg = None):
        self.__namn = namn
        self.__ålder = ålder
        if betyg == None:
            self.__betyg = []
        else:
            self.__betyg = betyg

    def lägg_till_betyg(self, betyg):
        for i in range(17):
            try:
                betyg = int(input("Ange betyg: "))
                if 0 <= betyg <= 100:
                    self.__betyg.append(betyg)
                else:
                    print("Du måste ange ett poäng mellan 0-100")
            except ValueError:
                print("Inte godkänts, försök igen.")

    def få_medelbetyg(self):
        return sum(self.__betyg) / len(self.__betyg)
            
    def set_info(self, namn, ålder):
        namn = input("Ange namn: ")
        while True:
            try:
                ålder = int(input("Ange ålder: "))
                int(ålder)
                if ålder < 0:
                    print("Du kan inte ange något under 0 ålder. ")
                else:
                    self.__namn = namn
                    self.__ålder = ålder
                    break
            except ValueError:
                    print("Du måste ange ett tal, försök igen( ͡° ͜ʖ ͡°).")            

    def få_info(self):
        return self.__namn, self.__ålder, self.__betyg


class Studerandehantering:    
    def __init__(self, studerande = None):
            if studerande == None:
                self.__studerande = []
            else:
                self.__studerande = studerande    
    
    def lägga_till_studerande(self, studerande):
        self.__studerande.append(studerande)

    def ta_bort_studerande(self, namn):
        self.__studerande = [s for s in self.__studerande if s.få_info()[0] != namn]

    def hitta_studerande_med_högsta_medelbetyg(self):
        return max(self.__studerande, key=lambda s: s.få_medelbetyg(), default=None)
    

Student1 = Studerande("student1", 0)


"""
Student1.set_info("namn", "ålder")
print(Student1.få_info())

Student1.lägg_till_betyg("betyg")
print(Student1.få_info())
print(Student1.få_medelbetyg("betyg"))
"""
