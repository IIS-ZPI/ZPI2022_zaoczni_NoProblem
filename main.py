from Arithmetic import *

# Main class for arithmetic operations

print('NAZWA_GRUPY No Problem, GROUP LEADER ID DanielWap, DEVELOPER ID Hubertius, DEVELOPER ID 229258, DEVELOPER ID ppatyk, DEVOPS ID WiktorKwasniak')

first_value = int(input('Enter first value: '))
second_value = int(input('Enter second value: '))
operation = input('Choose your operation: ')

#dictionary of possible operations, current options:
#    * addition
#    * substraction
#    * multiplication
#    * division
operations = {
    '+': AddOperator().add(first_value, second_value),
    '-': DiffOperator().diff(first_value, second_value),
    '*': MultiplyOperator().multiply(first_value, second_value),
    '/': DivisionOperator().divide(first_value, second_value)
}

print(operations.get(operation, 'Unknown operation'))