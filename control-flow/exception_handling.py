# try...catch...finally
first = 10
second = 0

try:
    print(first / second)
except ZeroDivisionError as e:
    print(e)
finally:
    print('Finished')

# raise
def divide(first, second):
    if second == 0:
        raise ZeroDivisionError('DIVISION BY ZERO')
    return first / second

try:
    div = divide(first, second)
    print(div)
except ZeroDivisionError as e:
    print(e)
finally:
    print('Finished')