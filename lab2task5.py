scores = [67, 82, 45, 91, 76, 88, 54]


maximum = scores[0]


for score in scores:
    if score > maximum:
        maximum = score


print(f"Maximum score: {maximum}")
