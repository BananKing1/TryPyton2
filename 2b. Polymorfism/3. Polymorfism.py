"""
Skapa en klass Kalkylator med en metod utför_operation. Denna metod ska ta tre parametrar: 
de två talen och en instans av en av Operation-subklasserna. Den ska sedan kalla på utför-metoden för
den passerade operationen.
"""
class Operation:
    def __init__(self, tal1, tal2):
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


class Kalkylator:
      def execute_operation(self, tal1, tal2, operation):
            return operation.execute(tal1, tal2)
    
    
kalkylator = Kalkylator()
print(kalkylator.execute_operation(2, 2, Multiply(2, 2)))