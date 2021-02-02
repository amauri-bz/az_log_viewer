from tkinter import *
from Operations.operation import Operation

class Undo(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        tab_text = self.tab.get_text()
        try:
            tab_text.text.edit_undo()
        except:
            pass
