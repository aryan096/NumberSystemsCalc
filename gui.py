import tkinter as tk


class Layout(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.binary_var = tk.StringVar()
        self.octal_var = tk.StringVar()
        self.decimal_var = tk.StringVar()
        self.hexadecimal_var = tk.StringVar()
        self.create_widgets()




    def create_widgets(self):

        # Labels
        self.binary_label = tk.Message(self, width=80, text="Binary: ")
        self.binary_label.grid(row=0, column=0, sticky="W")
        self.octal_label = tk.Message(self, width=80, text="Octal: ")
        self.octal_label.grid(row=1, column=0, sticky="W")
        self.decimal_label = tk.Message(self, width=80, text="Decimal: ")
        self.decimal_label.grid(row=2, column=0, sticky="W")
        self.hexadecimal_label = tk.Message(self, width=90, text="Hexadecimal: ")
        self.hexadecimal_label.grid(row=3, column=0, sticky="W")

        # Entry Fields for binary, octal, decimal, hexadecimal
        self.binary_entry = tk.Entry(self, textvariable = self.binary_var, width = 30, justify = "center")
        self.binary_entry.grid(row=0, column=1)
        self.octal_entry = tk.Entry(self, textvariable = self.octal_var, width = 30, justify = "center")
        self.octal_entry.grid(row=1, column=1)
        self.decimal_entry = tk.Entry(self, textvariable = self.decimal_var, width = 30, justify = "center")
        self.decimal_entry.grid(row=2, column=1)
        self.hexadecimal_entry = tk.Entry(self, textvariable = self.hexadecimal_var, width = 30, justify = "center")
        self.hexadecimal_entry.grid(row=3, column=1)

        # Calculate Button
        self.calc_button = tk.Button(self, text = "Calculate", width=40)
        self.calc_button.grid(row=4, columnspan=2)