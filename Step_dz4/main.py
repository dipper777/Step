import random

class Cypher:
    def __init__(self, number):
        self.__number = number

    def __encapsulate(self):
        operation = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)

        if operation == '+':
            self.__number += operand

        elif operation == '-':
            self.__number -= operand

        elif operation == '*':
            self.__number *= operand

        elif operation == '/':
            self.__number /= operand

    def get_result(self):

        self.__encapsulate()

        return self.__number

# Використання об'єкта

number = int(input("Введіть число: "))
cypher = Cypher(number)
result = cypher.get_result()
print("Результ: ", result)