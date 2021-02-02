from tkinter import messagebox
from Operations.operation import Operation

class Exit(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        if messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
            self.root.destroy()