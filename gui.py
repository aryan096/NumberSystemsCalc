import tkinter as tk
from operations import binary_hex, binary_octal, octal_binary, decimal_binary, hex_binary


class Layout(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.binary_var = tk.StringVar()
        self.octal_var = tk.StringVar()
        self.decimal_var = tk.StringVar()
        self.hexadecimal_var = tk.StringVar()
        self.current_type = 0
        self.create_widgets()

    def create_widgets(self):

        # Labels
        self.binary_label = tk.Message(self, width=80, text="Binary: ")
        self.binary_label.grid(row=0, column=0, sticky="W")
        self.octal_label = tk.Message(self, width=80, text="Octal: ")
        self.octal_label.grid(row=1, column=0, sticky="W")
        self.decimal_label = tk.Message(self, width=80, text="Decimal: ")
        self.decimal_label.grid(row=2, column=0, sticky="W")
        self.hexadecimal_label = tk.Message(
            self, width=90, text="Hexadecimal: ")
        self.hexadecimal_label.grid(row=3, column=0, sticky="W")

        # Entry Fields for binary, octal, decimal, hexadecimal
        self.binary_entry = tk.Entry(
            self, textvariable=self.binary_var, width=30, justify="center")
        self.binary_entry.grid(row=0, column=1)
        self.octal_entry = tk.Entry(
            self, textvariable=self.octal_var, width=30, justify="center")
        self.octal_entry.grid(row=1, column=1)
        self.decimal_entry = tk.Entry(
            self, textvariable=self.decimal_var, width=30, justify="center")
        self.decimal_entry.grid(row=2, column=1)
        self.hexadecimal_entry = tk.Entry(
            self, textvariable=self.hexadecimal_var, width=30, justify="center")
        self.hexadecimal_entry.grid(row=3, column=1)

        # Checkbuttons
        self.binary_button = tk.Button(
            self, width=3, text="=", command=lambda: self.calculate(1))
        self.binary_button.grid(row=0, column=2, sticky="W")
        self.binary_button = tk.Button(
            self, width=3, text="=", command=lambda: self.calculate(2))
        self.binary_button.grid(row=1, column=2, sticky="W")
        self.binary_button = tk.Button(
            self, width=3, text="=", command=lambda: self.calculate(3))
        self.binary_button.grid(row=2, column=2, sticky="W")
        self.binary_button = tk.Button(
            self, width=3, text="=", command=lambda: self.calculate(4))
        self.binary_button.grid(row=3, column=2, sticky="W")

        # Calculate Button
        self.reset_button = tk.Button(self, text="Reset", width=40, command= lambda: self.calculate(5))
        self.reset_button.grid(rowspan=2, columnspan=2)

    def calculate(self, type):

        try:
            if type == 1:
                self.octal_var.set(binary_octal(int(self.binary_var.get(), 2)))
                self.decimal_var.set(int(self.binary_var.get(), 2))
                self.hexadecimal_var.set(binary_hex(int(self.binary_var.get(), 2)))

            elif type == 2:
                self.binary_var.set(octal_binary(int(self.octal_var.get(), 8)))
                self.decimal_var.set(int(self.binary_var.get(), 2))
                self.hexadecimal_var.set(binary_hex(int(self.binary_var.get(), 2)))

            elif type == 3:
                self.binary_var.set(decimal_binary(int(self.decimal_var.get())))
                self.octal_var.set(binary_octal(int(self.binary_var.get(), 2)))
                self.hexadecimal_var.set(binary_hex(int(self.binary_var.get(), 2)))

            elif type == 4:
                self.binary_var.set(hex_binary(
                    int(self.hexadecimal_var.get(), 16)))
                self.octal_var.set(binary_octal(int(self.binary_var.get(), 2)))
                self.decimal_var.set(int(self.binary_var.get(), 2))

            elif type == 5:
                self.binary_var.set(0)
                self.octal_var.set(0)
                self.decimal_var.set(0)
                self.hexadecimal_var.set(0)

        except ValueError:
            self.binary_var.set("Invalid Input!")
            self.octal_var.set("Invalid Input!")
            self.decimal_var.set("Invalid Input!")
            self.hexadecimal_var.set("Invalid Input!")



        self.master.update_idletasks()
