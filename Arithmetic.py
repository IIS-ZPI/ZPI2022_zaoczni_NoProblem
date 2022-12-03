class AddOperator():
    def add(self, first_value, second_value):
        return first_value + second_value


class DivisionOperator():
    def divide(self, first_value, second_value):
        if (second_value == 0):
            raise Exception("Nie dziel przez zero!")
        else:
            return first_value/second_value
