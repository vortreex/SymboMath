class Fraction():
    def __init__(self, nominator=0, denominator=1):
        self.nominator = nominator
        self.denominator = denominator
        if self.denominator == 0:
            raise ZeroDivisionError

    def __str__(self) -> str:
        return f'{self.nominator}/{self.denominator}'

    def __nonzero__(self) -> bool:
        if self.nominator > 0:
            return True
        else:
            return False
    
    def __add__(self, other):
        num1 = Fraction(self.nominator * other.denominator, self.denominator * other.denominator)
        num2 = Fraction(other.nominator * self.denominator, other.denominator * self.denominator)
        return Fraction(num1.nominator + num2.nominator, num1.denominator)

    def __sub__(self, other):
        num1 = Fraction(self.nominator * other.denominator, self.denominator * other.denominator)
        num2 = Fraction(other.nominator * self.denominator, other.denominator * self.denominator)
        return Fraction(num1.nominator - num2.nominator, num1.denominator)

    def __mul__(self, other):
        return Fraction(self.nominator * other.nominator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.nominator * other.denominator, self.denominator * other.nominator)




    