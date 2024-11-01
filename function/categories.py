# no return type with no parameter
def no_return_type_with_no_parameter():
    print('No return type and no parameter')

# return type with no parameter
def return_type_with_no_parameter():
    return 'Return type and no parameter'

# no return type with parameter
def no_return_type_with_parameter(name):
    print(f'No return type and parameter: {name}')

# return type with parameter
def return_type_with_parameter(name):
    return f'Return type and parameter: {name}'

no_return_type_with_no_parameter()

print(return_type_with_no_parameter())

no_return_type_with_parameter('Python')

print(return_type_with_parameter('Python'))