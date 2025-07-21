from encodings import undefined

operatorSum = "+"
operatorMultiplication = "*"


def calculate(operator, *args):
    if operator == operatorSum:
        return sum(args)

    if operator == operatorMultiplication:
        mult = 1
        for number in args:
            mult = mult * number

        return mult

    return None


print(calculate(operatorSum, 5, 5, 5))
print(calculate(operatorMultiplication, 5, 5, 5))
