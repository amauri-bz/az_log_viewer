from tkinter import *
from Operations.operation import Operation

class SelectAll(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return
        self.select_all(tab_text)

    # Select all the text in textbox
    def select_all(self, tab_text):
        tab_text.text.tag_add(SEL, "1.0", END)
        tab_text.text.mark_set(INSERT, "1.0")
        tab_text.text.see(INSERT)