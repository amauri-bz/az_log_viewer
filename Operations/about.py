from tkinter import messagebox
from Operations.operation import Operation

class About(Operation):

    def __init__(self, root, tab):
        pass

    def execute(self):
        messagebox.showinfo('Az-Log-Viewer', 'Text display system for log analysis\n\n'+
            'Based on the Python TKinter library')