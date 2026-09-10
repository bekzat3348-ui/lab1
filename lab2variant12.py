a = int(input("Enter start number (a): "))
b = int(input("Enter end number (b): "))


start = min(a, b)
end = max(a, b)


total_sum = 0


for num in range(start, end + 1):
    total_sum += num


print(f"Sum of integers from {start} to {end} is: {total_sum}")
