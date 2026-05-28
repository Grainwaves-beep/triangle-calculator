import math
import tkinter as tk

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + b <= c or a + c <= b or b + c <= a:
            result_label.config(text="Not a valid triangle")
            return

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        result_label.config(text=f"Area: {area}")

    except ValueError:
        result_label.config(text="Enter valid numbers")


# window
root = tk.Tk()
root.title("Triangle Area Calculator")

# inputs
tk.Label(root, text="Side a").pack()
entry_a = tk.Entry(root)
entry_a.pack()

tk.Label(root, text="Side b").pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Side c").pack()
entry_c = tk.Entry(root)
entry_c.pack()

# button
tk.Button(root, text="Calculate Area", command=calculate).pack()

# result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()