numbers = [12, -5, 0, -8, 3, -1, 7]
count = 0
for num in numbers:
    if num < 0:
        count += 1

print(f"Number of negative elements: {count}")