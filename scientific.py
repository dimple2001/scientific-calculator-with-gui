import math

class ScientificCalculator:
    @staticmethod
    def sqrt(x):
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(x)

    @staticmethod
    def factorial(x):
        if x < 0 or x != int(x):
            raise ValueError("Factorial is only defined for positive integers")
        return math.factorial(int(x))

    @staticmethod
    def sin(x):
        return math.sin(math.radians(x))

    @staticmethod
    def cos(x):
        return math.cos(math.radians(x))

    @staticmethod
    def tan(x):
        return math.tan(math.radians(x))

    @staticmethod
    def log(x):
        if x <= 0:
            raise ValueError("Logarithm only defined for positive numbers")
        return math.log10(x)

    @staticmethod
    def ln(x):
        if x <= 0:
            raise ValueError("Natural log only defined for positive numbers")
        return math.log(x)
