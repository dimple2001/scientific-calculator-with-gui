from tkinter import *
from tkinter.messagebox import showerror, showinfo
from calculator import Calculator
from scientific import ScientificCalculator
from styles import FONT, BUTTON_COLORS
from utils import format_result

class CalculatorUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('Scientific Calculator')
        self.window.geometry('510x700')

        self.setup_gui()

    def setup_gui(self):
        self.main_frame = Frame(self.window)
        self.main_frame.pack(expand=True, fill=BOTH, padx=10, pady=10)

        self.textField = Entry(
            self.main_frame, font=FONT, justify=CENTER, bg='white', insertbackground='black'
        )
        self.textField.pack(side=TOP, pady=10, fill=X)
        self.textField.bind('<Return>', self.enter_click)

        self.create_scientific_frame()
        self.create_normal_frame()
        self.create_menu()

    def create_scientific_frame(self):
        self.scFrame = Frame(self.main_frame)
        self.scFrame.pack(side=TOP, pady=10)

        scientific_buttons = [
            ('√', 0, 0, lambda: self.calculate_scientific(ScientificCalculator.sqrt)),
            ('x!', 0, 1, lambda: self.calculate_scientific(ScientificCalculator.factorial)),
            ('π', 0, 2, lambda: self.insert_text(str(math.pi))),
            ('sin', 1, 0, lambda: self.calculate_scientific(ScientificCalculator.sin)),
            ('cos', 1, 1, lambda: self.calculate_scientific(ScientificCalculator.cos)),
            ('tan', 1, 2, lambda: self.calculate_scientific(ScientificCalculator.tan)),
            ('log', 2, 0, lambda: self.calculate_scientific(ScientificCalculator.log)),
            ('ln', 2, 1, lambda: self.calculate_scientific(ScientificCalculator.ln)),
            ('(', 2, 2, lambda: self.insert_text('(')),
            (')', 2, 3, lambda: self.insert_text(')'))
        ]

        for text, row, col, command in scientific_buttons:
            self.create_button(self.scFrame, text, row, col, command)

    def create_normal_frame(self):
        self.buttonFrame = Frame(self.main_frame)
        self.buttonFrame.pack(side=TOP, pady=10)

        for i in range(3):
            for j in range(3):
                num = i * 3 + j + 1
                self.create_button(self.buttonFrame, str(num), i, j, lambda x=num: self.insert_text(str(x)))

        operators = [
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2),
            ('+', 0, 3), ('-', 1, 3), ('×', 2, 3), ('÷', 3, 3)
        ]

        for text, row, col in operators:
            command = self.calculate if text == '=' else lambda x=text: self.insert_text(x)
            self.create_button(self.buttonFrame, text, row, col, command)

        self.create_button(self.buttonFrame, '⌫', 4, 0, self.clear, 2)
        self.create_button(self.buttonFrame, 'AC', 4, 2, self.all_clear, 2)

    def create_button(self, parent, text, row, column, command=None, columnspan=1):
        btn = Button(
            parent, text=text, font=FONT, width=5 if columnspan == 1 else 11,
            relief='ridge', bg=BUTTON_COLORS['bg'],
            activebackground=BUTTON_COLORS['active_bg'],
            activeforeground=BUTTON_COLORS['active_fg'],
            command=command
        )
        btn.grid(row=row, column=column, columnspan=columnspan, padx=2, pady=2)

    def calculate_scientific(self, func):
        try:
            value = float(self.textField.get())
            result = func(value)
            self.update_display(result)
        except Exception as e:
            showerror("Error", str(e))

    def calculate(self):
        try:
            expression = self.textField.get().replace('×', '*').replace('÷', '/')
            result = eval(expression)
            self.update_display(result)
        except Exception as e:
            showerror("Error", str(e))

    def insert_text(self, text):
        self.textField.insert(END, text)

    def clear(self):
        text = self.textField.get()
        if text:
            self.textField.delete(len(text) - 1)

    def all_clear(self):
        self.textField.delete(0, END)

    def enter_click(self, event):
        self.calculate()

    def create_menu(self):
        menubar = Menu(self.window)
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.window.config(menu=menubar)

    def show_about(self):
        showinfo("About", "Scientific Calculator\nVersion 1.0")

    def update_display(self, result):
        self.textField.delete(0, END)
        self.textField.insert(0, format_result(result))

    def run(self):
        self.window.mainloop()
