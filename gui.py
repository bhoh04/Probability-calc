import tkinter as tk
from tkinter import ttk
from functools import partial
from probability_calc import Hat, experiment

class HatExperimentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hat Experiment Probability Calculator")
        
        self.label1 = ttk.Label(root, text="Number of balls in the hat:")
        self.label1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.balls_entry = ttk.Entry(root)
        self.balls_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.label2 = ttk.Label(root, text="Expected balls (e.g., red:2 green:1):")
        self.label2.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        
        self.expected_entry = ttk.Entry(root)
        self.expected_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.label3 = ttk.Label(root, text="Number of balls drawn:")
        self.label3.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        
        self.drawn_entry = ttk.Entry(root)
        self.drawn_entry.grid(row=2, column=1, padx=5, pady=5)
        
        self.label4 = ttk.Label(root, text="Number of experiments:")
        self.label4.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        
        self.experiments_entry = ttk.Entry(root)
        self.experiments_entry.grid(row=3, column=1, padx=5, pady=5)
        
        self.calculate_button = ttk.Button(root, text="Calculate Probability", command=self.calculate_probability)
        self.calculate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
        self.probability_label = ttk.Label(root, text="")
        self.probability_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
        
    def calculate_probability(self):
        balls_str = self.balls_entry.get()
        expected_str = self.expected_entry.get()
        drawn_str = self.drawn_entry.get()
        experiments_str = self.experiments_entry.get()
        
        try:
            balls = {color: int(count) for color, count in (item.split(":") for item in balls_str.split())}
            expected = {color: int(count) for color, count in (item.split(":") for item in expected_str.split())}
            drawn = int(drawn_str)
            experiments = int(experiments_str)
            
            hat = Hat(**balls)
            probability = experiment(hat, expected, drawn, experiments)
            self.probability_label.config(text=f"Probability: {probability:.4f}")
        except Exception as e:
            self.probability_label.config(text="Error: Invalid input")

root = tk.Tk()
app = HatExperimentApp(root)
root.mainloop()
