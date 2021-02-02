from tkinter import *
from Operations.operation import Operation

class Past(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        tab_text = self.tab.get_text()
        try:
            text = tab_text.text.selection_get(selection='CLIPBOARD')
            if text != '':
                tab_text.text.insert('insert', text)
        except:
            pass