"""     Car uppgiften     """

class Car(): #klass namn Car
    wheels = 4 #statiskt attribut (något alla car har gemensamt)
    car_count = 0 #räkna bilnummer


    def __init__(self, model, price): #self anger sig själv
        self.model = model #modell
        self.price = price #pris

        Car.car_count += 1 #lägg till 1 för varje bil
        self.car_number = Car.car_count #instansattribut

    """
    def present_car(self, price):
        return "This car is of model {m}, costs {p}$ and is car number {nr} of {tot}.".format(
            m = self.model, p = self.price, nr = self.car_number, tot = self.car_count)


    @staticmethod
    def calculate_price_reduction(price):
        return int(price * 0.66)

    def reduce_price(self):
        self.price = self.calculate_price_reduction(self.price)
        return "Priset för {m} är nu {p}.".format(m=self.model, p=self.price)
    

    def __add__(self, other):
        if isinstance(other, Car): #pris tillägg för angett bilar
            return self.price + other.price
        if isinstance(other, int): #pris tillägg för ett angett pris
            return self.price + other
        raise ValueError(f"Car doesn't support addition with object of type {type(other)}") #in case of error

    def __iadd__(self, other):
        self.price += other.price #gammalt pris blir summan av gamla och den andra bilens pris 
        return self
    """

    def __str__(self):
        return f"Car of model {self.model}, costs {self.price}$." #utnyttja f-sträng

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        if float(new_price) / float(self.price) > 0.7:
            self.price = new_price
            print(f"New price is {self.price}")
        else:
            raise ValueError("New price is too low. You can max lower it with 30%")


class SellSystem():
    def set_temporary_sale(self, new_price, time, numberplate):
        self.cars[numberplate].price = new_price
        self.sale_end_date = time


#ange info om bilen i klassen Car
bmw = Car("BMW", 100000) #skapat bmw objekt av class Car
volvo = Car("Volvo", 150000) #skapat objekt av class Car

"""
#utskrift
print(bmw.model) #modell
print(volvo.model) #modell
print(volvo.wheels) #hjul
print(bmw.wheels) #hjul

print(volvo.present_car())

print(Car.calculate_price_reduction(200000)) #reducerat pris på angett pris (200 000)
print(bmw.reduce_price()) #reducerat pris på BMW
print(bmw.calculate_price_reduction(200000)) #reducerat pris för angett BMW pris (200 000)
print(bmw.present_car(bmw))


#tilläg pris av BMW til Volvo
print( bmw + volvo )
print( volvo + bmw )
print(volvo.__add__(bmw))
print( bmw + 10000) #BWM och angett pris

bmw = bmw.__iadd__(volvo)
print(bmw.price)

bmw = Car("X2", 10000)
print(bmw)
"""

car = Car("volvo v40", 40000)

print(car.price)
print(car.get_price())
car.set_price(35000)
car.set_price(10000)