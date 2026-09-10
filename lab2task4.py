numbers = [12, -5, 8, -3, 21, 0, 14, -7]


total_sum = 0
pos_sum = 0
pos_count = 0
neg_count = 0
zero_count = 0


for num in numbers:
    total_sum += num
    
    if num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1


print(f"Total sum of all numbers: {total_sum}")
print(f"Sum of positive numbers: {pos_sum}")
print(f"Count of positive numbers: {pos_count}")
print(f"Count of negative numbers: {neg_count}")
print(f"Count of zeros: {zero_count}")
