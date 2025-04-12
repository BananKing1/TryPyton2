"""
Skapa en abstrakt klass Operation. Den ska ha en metod utför som tar två tal som argument. Denna metod 
kommer att implementeras i varje subklass.
"""

class Operation:
    def excute(self, tal1, tal2):
        self.tal1 = tal1
        self.tal2 = tal2

class Addition(Operation):
    def excute(tal1, tal2):
        return int(tal1 + tal2)

class Subtraction(Operation):
    def execute(tal1, tal2):
        return int(tal1 - tal2)

class Multiply(Operation):
    def execute(tal1, tal2):
        return int(tal1 * tal2)

class Division(Operation):
    def execute(tal1, tal2):
        return int(tal1 / tal2)

add = Addition
print(add.excute(10, 5))

subtract = Subtraction
print(subtract.execute(10, 5))

multiply = Multiply
print(multiply.execute(10, 5))

division = Division
print(division.execute(10, 5))
