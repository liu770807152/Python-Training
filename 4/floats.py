from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)

x = 1024
print(bin(x), oct(x), hex(x), sep=', ')
print(int('a', 16))

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b == Decimal('6.3'))
a = '1.23456'
print(Decimal(a).quantize(Decimal('0.001'), rounding="ROUND_HALF_UP"))