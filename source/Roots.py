BLANK = ''

class Root():
    def __init__(self, degree=2, number=1, quantity=1):
        self.degree = degree
        self.number = number
        self.quantity = quantity
    
    def __str__(self):
        #return f'{self.number}^(1/{self.degree})'
        if self.quantity != 1:
            return f'{self.quantity}Roots({self.degree}, {self.number})'
        else:
            return f'Root({self.degree}, {self.number})'

    def __add__(self, other):
        if self.degree == other.degree and self.number == self.number:
            return Root(degree=self.degree, number=self.number, quantity=self.quantity+other.quantity)
    
    def __sub__(self, other):
        if self.degree == other.degree and self.number == self.number:
            return Root(degree=self.degree, number=self.number, quantity=self.quantity-other.quantity)

    def __mul__(self, other):
        if self.degree == other.degree:
            return Root(degree=self.degree, number=self.number*other.number, quantity=self.quantity*other.quantity)
    
    def __truediv__(self, other):
        if self.degree == other.degree:
            return Root(degree=self.degree, number=self.number/other.number, quantity=self.quantity/other.quantity)