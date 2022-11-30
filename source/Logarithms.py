BLANK = ''

class Logarithm():
    def __init__(self, base=10, number=10, quantity=1):
        self.base = base
        self.number = number
        self.quantity = quantity
        if not self.quantity:
            return 0

    def __str__(self):
            return f'{self.quantity if self.quantity != 1 else BLANK}log{self.base}({self.number})'
        
    def __add__(self, other):
        if self.base == other.base:
            return Logarithm(base=self.base, number=self.number*other.number)

    def __sub__(self, other):
        if self.base == other.base:
            return Logarithm(base=self.base, number=self.number/other.number)
    