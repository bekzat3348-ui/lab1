def is_even(number):
    return number % 2 == 0

def square(number):
    return number ** 2

def sum_even_squares(values):
    total = 0
    for number in values:
        if is_even(number):
            total += square(number)
    return total

numbers = [4, 7, 2, 9, 12, 5, 8, 3]
print(sum_even_squares(numbers))
