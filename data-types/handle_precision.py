pi = 3.141592654

print(pi)

# rounding the number

formatted_pi_str = f'{pi:.4f}'

print(formatted_pi_str)
print(type(formatted_pi_str))

formatted_pi_int = round(pi, 4)

print(formatted_pi_int)
print(type(formatted_pi_int))

# precision error

precision_error = 0.1 + 0.2

print(precision_error)
print(type(precision_error))

from decimal import Decimal

precision_error = Decimal('0.1') + Decimal('0.2')

print(precision_error)
print(type(precision_error))