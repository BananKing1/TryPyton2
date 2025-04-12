"""
Skapa tre subklasser: Addition, Subtraktion, och Multiplicering.
Varje klass ska implementera utför-metoden för att utföra den lämpliga matematiska operationen.
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