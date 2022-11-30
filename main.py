from source.Fractions import Fraction
from source.Logarithms import Logarithm
from source.Roots import Root

def main():

    a = Fraction(7, 10)
    b = Fraction(6, 10)
    print(a, b)
    c = a*b
    d = a/b
    e = a+b
    f = a-b
    print(c, d, e, f)
    l = Logarithm(10, 100)
    g = Logarithm(10, 1000)
    print(g,l, g-l)
    r = Root(2, 3, 2)
    q = Root(2, 6, 5)

    print(r, q, r*q, r/q)

if __name__ == '__main__':
    main()
