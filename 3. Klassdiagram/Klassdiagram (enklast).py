class Att_göra():
    uppgifter = list()

    def __innit__(self):
        self.uppgifter = list()

    def lägg_till_uppgift(self, beskrivning):
        self.uppgifter.append(beskrivning)
        self.uppgifter.append(False)
    
    def ta_bort_uppgift(self, beskrivning):
        self.uppgifter.remove(beskrivning)
    
    def hämta_alla_uppgifter(self):
        print(self.uppgifter)



class Uppgift(Att_göra):
        def ___innit___(self, beskrivning, är_färdig):
            self.beskrivning = beskrivning
            self.är_färdig = False

        def markera_som_färdig(self, beskrivning, är_färdig):
            self.är_färdig = True
            
            return 

        


ToDo = Att_göra()
ToDo.lägg_till_uppgift("äta")
ToDo.lägg_till_uppgift("sova")
ToDo.lägg_till_uppgift("gå till skolan")

ToDo.ta_bort_uppgift("sova")

ToDo.hämta_alla_uppgifter()

Status = Uppgift()
Status.markera_som_färdig('sova', True)