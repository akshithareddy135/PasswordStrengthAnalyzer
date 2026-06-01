import tkinter as tk
from tkinter import ttk
from analyzer import *

class PasswordAnalyzerGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Password Strength Analyzer")
        self.root.geometry("700x650")
        self.root.resizable(False, False)

        self.common_passwords = load_common_passwords()

        title = tk.Label(
            root,
            text="Password Strength Analyzer",
            font=("Segoe UI", 20, "bold")
        )
        title.pack(pady=15)

        self.password_var = tk.StringVar()

        password_frame = tk.Frame(root)
        password_frame.pack(pady=10)

        tk.Label(
            password_frame,
            text="Enter Password:",
            font=("Segoe UI", 12)
        ).pack(side=tk.LEFT, padx=5)

        self.password_entry = tk.Entry(
            password_frame,
            textvariable=self.password_var,
            show="*",
            width=35,
            font=("Segoe UI", 12)
        )
        self.password_entry.pack(side=tk.LEFT)

        self.show_var = tk.BooleanVar()

        tk.Checkbutton(
            root,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password
        ).pack()

        analyze_btn = ttk.Button(
            root,
            text="Analyze Password",
            command=self.analyze_password
        )
        analyze_btn.pack(pady=15)

        self.result_text = tk.Text(
            root,
            width=80,
            height=25,
            font=("Consolas", 10)
        )
        self.result_text.pack(pady=10)

    def toggle_password(self):

        if self.show_var.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def analyze_password(self):

        password = self.password_var.get()

        if not password:
            return

        score = calculate_score(password)
        strength = get_strength(score)

        entropy = calculate_entropy(password)
        crack_time = estimate_crack_time(entropy)

        recommendations = get_recommendations(password)

        self.result_text.delete(1.0, tk.END)

        report = f"""
================ PASSWORD REPORT ================

Length               : {len(password)}
Uppercase            : {has_uppercase(password)}
Lowercase            : {has_lowercase(password)}
Numbers              : {has_number(password)}
Special Characters   : {has_special(password)}

Character Diversity  : {character_diversity(password)}/4

Entropy              : {entropy} bits
Crack Time           : {crack_time}

Score                : {score}
Strength             : {strength}
"""

        if is_common_password(password, self.common_passwords):
            report += "\nWARNING: Common Password Detected!\n"

        if has_repeated_characters(password):
            report += "WARNING: Repeated Characters Found!\n"

        if has_sequential_pattern(password):
            report += "WARNING: Sequential Pattern Found!\n"

        report += "\nRecommendations:\n"

        if recommendations:
            for rec in recommendations:
                report += f"- {rec}\n"
        else:
            report += "- Excellent Password\n"

        self.result_text.insert(tk.END, report)


root = tk.Tk()
app = PasswordAnalyzerGUI(root)
root.mainloop()