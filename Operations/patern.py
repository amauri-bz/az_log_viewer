import tkinter as tk
from tkinter.colorchooser import askcolor

from Components.db import Database
from Operations.operation import Operation

class Patern(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.add_patern()

    def add_patern(self):
        self.canvas1 = tk.Toplevel(self.root)

        label1 = tk.Label(self.canvas1, text='Add Patern')
        label1.config(font=('helvetica', 10))
        label1.pack()

        self.entry1 = tk.Entry(self.canvas1)
        self.check_selection()
        self.entry1.pack()

        button1 = tk.Button(self.canvas1, text='Add', command=self.color_chooser,
                            bg='brown', fg='white', font=('helvetica', 9, 'bold'))
        button1.pack()

    def check_selection(self):
        try:
            tab_text = self.tab.get_text()
            text = tab_text.text.get("sel.first", "sel.last")
            if text != '':
                self.entry1.delete(0,tk.END)
                self.entry1.insert(0, text)
        except:
            pass

    def color_chooser(self):
        patern = self.entry1.get()
        color = askcolor(title = "Patern Color")
        db = Database.instance()
        db.add_item(patern, color[1])
        self.canvas1.destroy()
        self.canvas1.update()
        self.tab.refresh_tabs()