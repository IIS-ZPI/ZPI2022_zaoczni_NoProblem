# addition
class AddOperator:
    def add(self, first_value, second_value):
        return first_value + second_value


#Wiktor's class
# multiplication
class MultiplyOperator:
    def multiply(self, first_value, second_value):
        return first_value * second_value


#Wojtek's class
# subtraction
class DiffOperator:
    def diff(self, first_value: float, second_value: float) -> float:
        return first_value - second_value


#Pawel's class
# division
class DivisionOperator:
    def divide(self, first_value, second_value):
        if second_value == 0:
            raise Exception("Nie dziel przez zero!")
        else:
            return first_value/second_value


class AbsOperator:
    def abs (self,a,b):
        if a<0:
            a = a*(-1)
        if b<0:
            b= b*(-1)
        return(a,b)
