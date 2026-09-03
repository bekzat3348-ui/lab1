import tkinter as tk

numbers = [4, 7, 2, 9, 12, 5, 8, 3]

def calculate():
    result = sum(n ** 2 for n in numbers if n % 2 == 0)
    result_label.config(text=f"result: {result}")

root = tk.Tk()
root.title("programs paradigms")

result_label = tk.Label(root, text="press the button")
result_label.pack(padx=20, pady=10)

button = tk.Button(root, text="calculate", command=calculate)
button.pack(padx=20, pady=10)

root.mainloop()
