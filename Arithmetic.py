# addition
class AddOperator:
    def add(self, first_value, second_value):
        return first_value + second_value


# multiplication
class MultiplyOperator:
    def multiply(self, first_value, second_value):
        return first_value * second_value


# subtraction
class DiffOperator:
    def diff(self, first_value: float, second_value: float) -> float:
        return first_value - second_value


# division
class DivisionOperator:
    def divide(self, first_value, second_value):
        if second_value == 0:
            raise Exception("Nie dziel przez zero!")
        else:
            return first_value/second_value
