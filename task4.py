numbers = [4, 7, 2, 9, 12, 5, 8, 3]

result = sum(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, numbers)
    )
)

print(result)
