class Hp:
    def __init__(self):
        self.__result = 0

    def add(self, value):
        self.__result += value

    def subtract(self, value):
        self.__result -= value

    def get_result(self):
        return self.__result

ob = Hp()

ob.add(10)
ob.subtract(3)

result = ob.get_result()

print(f"The result is: {result}")

