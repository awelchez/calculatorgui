import customtkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        entry = tk.CTkEntry(self.root, textvariable=self.result_var, font=("Arial", 20))
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="news")

        buttons = [
            ('C', 1, 0), ('%', 1, 1), ('x^y', 1, 2), ('Del', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.CTkButton(self.root, text=text, font=("Arial", 16), width=70, height=50, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=1, pady=5, sticky="news")
    def on_button_click(self, button_text):
        if button_text == "=":
            try:
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        elif button_text == "C":  
            self.expression = ""
            self.result_var.set("0")
        elif button_text == "Del":
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif button_text == "%":
            try:
                result = str(eval(self.expression) / 100)
                self.result_var.set(result)
                self.expression = result
            except Exception as e:
                self.result_var.set("Error")
                self.expression = ""
        elif button_text == "x^y":
            self.expression += "**"
            self.result_var.set(self.expression)
        else:
            self.expression += button_text
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.CTk()
    app = CalculatorApp(root)
    root.mainloop()
