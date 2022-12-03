from Arithmetic import *

print(
    'NAZWA_GRUPY No Problem, GROUP LEADER ID DanielWap, DEVELOPER ID Hubertius, DEVELOPER ID 229258, DEVELOPER ID ppatyk, DEVOPS ID WiktorKwasniak')

first_value = int(input('Enter first value: '))
second_value = int(input('Enter second value: '))
operation = input('Choose your operation: ')

if operation == '+':
    x = AddOperator()
    print(x.add(first_value, second_value))
elif operation == '-':
    oper = DiffOperator()
    print(oper.diff(first_value, second_value))
elif operation == '*':
    pass
elif operation == '/':
    x = DivisionOperator()
    try:
        print(x.divide(first_value, second_value))
    except Exception as inst:
        print(inst)
