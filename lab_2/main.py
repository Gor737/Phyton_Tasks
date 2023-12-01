from math import gcd

class Fraction:
    def init(self, numerator, denominator):
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common

    def str(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        new_numerator = (
            self.numerator * other.denominator + other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def sub(self, other):
        new_numerator = (
            self.numerator * other.denominator - other.numerator * self.denominator
        )
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def mul(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def truediv(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


# Example.
fraction1 = Fraction(3, 1)
fraction2 = Fraction(4, 7)

result_add = fraction1 + fraction2
print(f"Addition: {result_add}")

result_sub = fraction1 - fraction2
print(f"Subtraction: {result_sub}")

result_mul = fraction1 * fraction2
print(f"Multiplication: {result_mul}")

result_div = fraction1 / fraction2
print(f"Division: {result_div}")
