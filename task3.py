class NumberCollection:
    def __init__(self, numbers):
        self._numbers = list(numbers)

    def get_even_numbers(self):
        return [n for n in self._numbers if n % 2 == 0]

    def sum_even_squares(self):
        total = 0
        for number in self._numbers:
            if number % 2 == 0:
                total += number ** 2
        return total

collection = NumberCollection([4, 7, 2, 9, 12, 5, 8, 3])
print(collection.get_even_numbers())
print(collection.sum_even_squares())
