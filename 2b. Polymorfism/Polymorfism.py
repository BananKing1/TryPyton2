"""
Skapa en abstrakt klass Operation. Den ska ha en metod utför som tar två tal som argument. Denna metod 
kommer att implementeras i varje subklass.
"""

class Operation: #super klass
    def excute(self, tal1, tal2):
        self.tal1 = tal1
        self.tal2 = tal2

class Addition(Operation): #sub klass
    def execute(self, tal1, tal2):
        return int(tal1 + tal2)

class Subtraction(Operation): #sub klass
    def execute(self, tal1, tal2):
        return int(tal1 - tal2)

class Multiply(Operation): #sub klass
    def execute(self, tal1, tal2):
        return int(tal1 * tal2)

class Division(Operation): #sub klass
    def execute(self, tal1, tal2):
        return int(tal1 / tal2)

class Kalkylator:
    def execute_operation(self, operation, tal1, tal2):
        return operation.execute(tal1, tal2)
        

def main():
    addition = Addition()
    subtract = Subtraction()
    multiply = Multiply()
    division = Division()
    kalkylator = Kalkylator()

    print("Addition:", kalkylator.execute_operation(addition, 10, 5))
    print("Subtraktion", kalkylator.execute_operation(subtract, 10, 5))
    print("Multiplikation", kalkylator.execute_operation(multiply, 10, 5))
    print("Division", kalkylator.execute_operation(division, 10, 5))


main()