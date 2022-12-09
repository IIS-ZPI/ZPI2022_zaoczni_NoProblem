from Arithmetic import *

# Main class for arithmetic operations

print('NAZWA_GRUPY No Problem, GROUP LEADER ID DanielWap, DEVELOPER ID Hubertius, DEVELOPER ID 229258, DEVELOPER ID ppatyk, DEVOPS ID WiktorKwasniak')

first_value = int(input('Enter first value: '))
second_value = int(input('Enter second value: '))
operation = input('Choose your operation: ')

operations = {
    '+': AddOperator().add(first_value, second_value), #dodawanie
    '-': DiffOperator().diff(first_value, second_value), #roznica
    '*': MultiplyOperator().multiply(first_value, second_value), #mnozenie
    '/': DivisionOperator().divide(first_value, second_value), #dzielenie
    'a': AbsOperator().abs(first_value, second_value) #abs
}

print(operations.get(operation, 'Unknown operation'))