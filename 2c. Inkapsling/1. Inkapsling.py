"""   Hantera Bankkonto   """

class Bankkonto:
    def __init__ (self, namn, saldo):
        self.__namn = namn #privat attribut
        self.__saldo = saldo #privat attribut

    def visa_saldo(self): #getter metod
        return self.__saldo
    
    def sätta_in(self, pengar): #setter metod
        self.__saldo += int(pengar)
        return self.__saldo

    def ta_ut(self, pengar): #setter metod
        if int(self.__saldo) < int(pengar):
            return "Du kan ej ta ut mer än du har i saldo."
        else:
            self.__saldo -= int(pengar)
            return self.__sald
        


random = Bankkonto("Carlos", 20)

print(random.visa_saldo()) #tillåt tillgång till privat attribut först
print(random.sätta_in(10))
print(random.ta_ut(40))

