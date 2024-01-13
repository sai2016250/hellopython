import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

import pandas as pd

class BestStudentsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Best Students App")

        # Load data from the CSV file (assuming the file is named 'students_data.csv')
        self.load_data()

        # Calculate the best student
        self.calculate_best_student()

        # Create and configure the GUI
        self.create_gui()

    def load_data(self):
        # Load data from the CSV file
        self.students_data = pd.read_csv('students_data.csv')

    def calculate_best_student(self):
        # Calculate the best student based on the average test score
        self.best_student = self.students_data.loc[self.students_data['AVG(TEST)'].idxmax()]

    def create_gui(self):
        # Display the best student on the screen
        tk.Label(self.master, text="Best Student:").grid(row=0, column=0, pady=10)
        tk.Label(self.master, text=f"Name: {self.best_student['Name']}").grid(row=1, column=0)
        tk.Label(self.master, text=f"Avg Test: {self.best_student['AVG(TEST)']}").grid(row=2, column=0)
        tk.Label(self.master, text=f"Avg Year: {self.best_student['AVG(YEAR)']}").grid(row=3, column=0)

if __name__ == "__main__":
    root = tk.Tk()
    app = BestStudentsApp(root)
    root.mainloop()

