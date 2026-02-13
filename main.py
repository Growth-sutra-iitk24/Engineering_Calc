import tkinter as tk
from civil_engineering import *
from mechanical_engineering import *
from electrical_engineering import *

class EngineeringCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Engineering Calculator")

        # GUI Elements go here

    # Define other GUI methods to handle calculations

if __name__ == '__main__':
    root = tk.Tk()
    app = EngineeringCalculator(root)
    root.mainloop()