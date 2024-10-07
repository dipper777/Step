class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, num1, num2, op):
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero!")
            result = num1 / num2
        self.history.append(f"{num1} {op} {num2} = {result}")
        return result

    def get_history(self):
        return self.histroy

    def clear_history(self):
        self.history = []

# Example usage:
calc = Calculator()

#5
print(calc.calculate(2, 3, '+'))
#3
print(calc.calculate(5, 2, '-'))
#20
print(calc.calculate(4, 5, '*'))
#5
print(calc.calculate(10, 2, '/'))
print(calc.get_history())