import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor

from Components.db import Database
from Operations.operation import Operation
from Components.patter_menu import PatternMenu
from Components.status_bar import StatusBar

class PatternAdd(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.add_pattern()

    def add_pattern(self):
        self.canvas1 = tk.Toplevel(self.root)
        self.canvas1.geometry('300x200')
        self.canvas1.minsize(250, 150)
        self.canvas1.maxsize(350, 250)
        self.canvas1.protocol('WM_DELETE_WINDOW', self.confirmExit)

        label1 = tk.Label(self.canvas1, text='Add Pattern')
        label1.config(font=('helvetica', 15))
        label1.pack()

        label1 = tk.Label(self.canvas1, text='Project:')
        label1.config(font=('helvetica', 10))
        label1.pack()

        tkvar = tk.StringVar(self.root)
        self.popupMenu = PatternMenu(self.tab, self.canvas1, tkvar, top_level = True)
        self.popupMenu.pack()
        self.popupMenu.configure(width=20)

        label1 = tk.Label(self.canvas1, text='New Project:')
        label1.config(font=('helvetica', 10))
        label1.pack()

        self.entry_project = tk.Entry(self.canvas1)
        self.entry_project.pack()

        label1 = tk.Label(self.canvas1, text='New Pattern:')
        label1.config(font=('helvetica', 10))
        label1.pack()

        self.entry_pattern = tk.Entry(self.canvas1)
        self.entry_pattern.pack()

        button1 = tk.Button(self.canvas1, text='Add', command=self.color_chooser, font=('helvetica', 9, 'bold'))
        button1.pack()

        self.canvas1.grab_set()
        self.check_selection()

    def confirmExit(self):
        StatusBar().set("aborted - operation aborted")
        self.canvas1.destroy()

    def check_selection(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return
        text = tab_text.text.get("sel.first", "sel.last")
        if text != '':
            self.entry_pattern.delete(0,tk.END)
            self.entry_pattern.insert(0, text)

    def color_chooser(self):
        proj = self.entry_project.get()
        pattern = self.entry_pattern.get()
        color = askcolor(title = "Pattern Color")
        if color != None:
            db = Database.instance()
            if proj != "" and proj != None:
                db.add_item(proj, pattern, color[1])
                StatusBar().set("pattern added with success")
            else:
                if db.instance().actual_proj != "None" and db.instance().actual_proj != None:
                    db.add_item(db.instance().actual_proj, pattern, color[1])
                    StatusBar().set("pattern added with success")
                else:
                    StatusBar().set("aborted - select a project or a new project name")
        else:
            StatusBar().set("aborted - operation aborted")
        self.canvas1.grab_release()
        self.canvas1.destroy()
        self.canvas1.update()
        self.tab.refresh_tabs()
