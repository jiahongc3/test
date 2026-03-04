import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Dark Calculator")
        master.geometry("300x450")
        master.resizable(False, False)
        master.configure(bg="#2d2d2d") # 主背景深灰色

        self.equation = ""
        self.display_var = tk.StringVar(value="0")

        # 顯示螢幕區域
        display_frame = tk.Frame(master, bg="#2d2d2d", bd=0)
        display_frame.pack(expand=True, fill="both", padx=10, pady=20)

        self.display_label = tk.Label(
            display_frame, 
            textvariable=self.display_var, 
            anchor="e", 
            font=("Segoe UI", 32), 
            bg="#2d2d2d", 
            fg="#ffffff", # 白色文字
            padx=10
        )
        self.display_label.pack(expand=True, fill="both")

        # 按鈕區域
        buttons_frame = tk.Frame(master, bg="#2d2d2d")
        buttons_frame.pack(expand=True, fill="both", padx=5, pady=5)

        # 按鈕配置
        # C: 清除, DEL: 退格, /, *
        # 7, 8, 9, -
        # 4, 5, 6, +
        # 1, 2, 3, =
        # 0, .
        buttons = [
            ('C', "#404040", "#ff5555"),   # 背景, 文字(紅色)
            ('DEL', "#404040", "#55aaff"), # 背景, 文字(藍色)
            ('/', "#404040", "#ffaa00"),   # 背景, 文字(橘色)
            ('*', "#404040", "#ffaa00"),
            ('7', "#505050", "#ffffff"),
            ('8', "#505050", "#ffffff"),
            ('9', "#505050", "#ffffff"),
            ('-', "#404040", "#ffaa00"),
            ('4', "#505050", "#ffffff"),
            ('5', "#505050", "#ffffff"),
            ('6', "#505050", "#ffffff"),
            ('+', "#404040", "#ffaa00"),
            ('1', "#505050", "#ffffff"),
            ('2', "#505050", "#ffffff"),
            ('3', "#505050", "#ffffff"),
            ('=', "#ffaa00", "#2d2d2d"),   # 等於鍵用橘色背景
            ('0', "#505050", "#ffffff"),
            ('.', "#505050", "#ffffff"),
            ('', "#2d2d2d", "#2d2d2d"),
            ('', "#2d2d2d", "#2d2d2d")
        ]

        row = 0
        col = 0
        for btn_text, bg_color, fg_color in buttons:
            if btn_text == "":
                col += 1
                if col > 3:
                    col = 0
                    row += 1
                continue

            action = lambda x=btn_text: self.on_button_click(x)
            
            btn = tk.Button(
                buttons_frame, 
                text=btn_text, 
                font=("Segoe UI", 14, "bold"),
                bg=bg_color,
                fg=fg_color,
                bd=0,
                activebackground="#606060",
                activeforeground="#ffffff",
                relief="flat",
                command=action
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # 設定格線權重
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                # 簡單處理 eval
                result = str(eval(self.equation))
                self.display_var.set(result)
                self.equation = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.clear_display()
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear_display()
        elif char == "C":
            self.clear_display()
        elif char == "DEL":
            self.equation = self.equation[:-1]
            self.display_var.set(self.equation if self.equation else "0")
        else:
            if self.display_var.get() == "0" and char not in ['+', '-', '*', '/']:
                self.equation = char
            else:
                self.equation += str(char)
            self.display_var.set(self.equation)

    def clear_display(self):
        self.equation = ""
        self.display_var.set("0")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
