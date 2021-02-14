import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor

from Components.db import Database
from Operations.operation import Operation
from Components.pater_menu import PaternMenu

class Patern(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.add_patern()

    def add_patern(self):
        self.canvas1 = tk.Toplevel(self.root)
        self.canvas1.geometry('300x200')
        self.canvas1.minsize(250, 150)
        self.canvas1.maxsize(350, 250)

        label1 = tk.Label(self.canvas1, text='Add Patern')
        label1.config(font=('helvetica', 15))
        label1.pack()

        label1 = tk.Label(self.canvas1, text='Project:')
        label1.config(font=('helvetica', 10))
        label1.pack()

        tkvar = tk.StringVar(self.root)
        self.popupMenu = PaternMenu(self.tab, self.canvas1, tkvar, top_level = True)
        self.popupMenu.pack()
        self.popupMenu.configure(width=20)

        label1 = tk.Label(self.canvas1, text='New Project:')
        label1.config(font=('helvetica', 10))
        label1.pack()

        self.entry_project = tk.Entry(self.canvas1)
        self.check_selection()
        self.entry_project.pack()

        label1 = tk.Label(self.canvas1, text='New Patern:')
        label1.config(font=('helvetica', 10))
        label1.pack()

        self.entry_patern = tk.Entry(self.canvas1)
        self.check_selection()
        self.entry_patern.pack()

        button1 = tk.Button(self.canvas1, text='Add', command=self.color_chooser, font=('helvetica', 9, 'bold'))
        button1.pack()

        self.canvas1.grab_set()

    def check_selection(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return
        text = tab_text.text.get("sel.first", "sel.last")
        if text != '':
            self.entry_patern.delete(0,tk.END)
            self.entry_patern.insert(0, text)


    def color_chooser(self):
        proj = self.entry_project.get()
        patern = self.entry_patern.get()
        color = askcolor(title = "Patern Color")
        if color != None:
            db = Database.instance()
            if proj != "" and proj != None:
                db.add_item(proj, patern, color[1])
            else:
                db.add_item(db.instance().actual_pattern, patern, color[1])
        self.canvas1.grab_release()
        self.canvas1.destroy()
        self.canvas1.update()
        self.tab.refresh_tabs()
