
price = float(input("Item price: "))
quantity = int(input("Quantity: "))
discount_percent = float(input("Discount (%): "))


total_raw = price * quantity
discount_amount = total_raw * (discount_percent / 100)
final_price = total_raw - discount_amount


print(f"\nTotal price without discount: {total_raw:.2f}")
print(f"Discount amount: {discount_amount:.2f}")
print(f"Total due: {final_price:.2f}")
