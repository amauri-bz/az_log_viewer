from tkinter import *
from Operations.operation import Operation

class Copy(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return

        tab_text.text.clipboard_clear()
        text = tab_text.text.get("sel.first", "sel.last")
        if text != '':
            tab_text.text.clipboard_append(text)
