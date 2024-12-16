import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Калькулятор")
        self.window.geometry("300x600")
        self.window.configure(bg='#1A1A1A')
        self.window.resizable(False, False)

        # Экран результата
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_label = tk.Label(
            self.window, 
            textvariable=self.result_var, 
            font=('Segoe UI', 40),  
            bg='#1A1A1A', 
            fg='white', 
            anchor='e', 
            padx=10
        )
        self.result_label.pack(fill='x', pady=(10, 5))

        # Создание кнопок в правильном порядке
        buttons = [
            'C', '(', ')', '%',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            '√', '!'
        ]

        # Фрейм для кнопок
        buttons_frame = tk.Frame(self.window, bg='#1A1A1A')
        buttons_frame.pack(padx=10, pady=5)

        # Создание сетки кнопок
        row, col = 0, 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(
                buttons_frame, 
                text=button, 
                width=4,  
                height=1,  
                font=('Segoe UI', 16),  
                bg='#2C2C2C', 
                fg='white', 
                command=cmd
            ).grid(row=row, column=col, padx=3, pady=3)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Привязка событий клавиатуры
        self.window.bind('<Key>', self.key_press)

    def factorial(self, n):
        if n < 0:
            return 'Ошибка'
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)

    def adjust_font_size(self, text):
        base_font_size = 40
        max_length = 10
        
        if len(text) > max_length:
            font_size = max(10, base_font_size - (len(text) - max_length) * 2)
            self.result_label.configure(font=('Segoe UI', font_size))
        else:
            self.result_label.configure(font=('Segoe UI', base_font_size))

    def key_press(self, event):
        key = event.char
        current_text = self.result_var.get()

        if key in '0123456789.()+-*/':
            if current_text == '0':
                self.result_var.set(key)
            else:
                self.result_var.set(current_text + key)
            self.adjust_font_size(self.result_var.get())
        elif event.keysym == 'Return':
            self.click('=')
        elif event.keysym == 'BackSpace':
            self.result_var.set(current_text[:-1] or '0')
            self.adjust_font_size(self.result_var.get())

    def click(self, key):
        try:
            current_text = self.result_var.get()
            
            if key == 'C':
                self.result_var.set("0")
                self.result_label.configure(font=('Segoe UI', 40))
            elif key == '√':
                current = float(current_text)
                result = math.sqrt(current)
                self.result_var.set(str(result))
            elif key == '!':
                current = int(float(current_text))
                result = self.factorial(current)
                self.result_var.set(str(result))
            elif key == '%':
                current = float(current_text)
                result = current / 100
                self.result_var.set(str(result))
            elif key == '=':
                result = eval(current_text)
                self.result_var.set(str(result))
            elif key in '0123456789.()+-*/':
                if current_text == '0':
                    self.result_var.set(key)
                else:
                    self.result_var.set(current_text + key)
            
            # Динамическая настройка размера шрифта
            self.adjust_font_size(self.result_var.get())
        
        except Exception:
            self.result_var.set('Ошибка')
            self.result_label.configure(font=('Segoe UI', 40))

    def run(self):
        self.window.mainloop()

# Запуск калькулятора
calc = Calculator()
calc.run()
