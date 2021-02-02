from tkinter import messagebox
from Operations.operation import Operation

class Help(Operation):

    def __init__(self, root, tab):
        pass

    def execute(self):
        messagebox.showinfo('Help', 'Text display system for log analysis\n\n'+
            'Based on the Python TKinter library')