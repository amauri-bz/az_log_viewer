import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor

from Components.db import Database
from Operations.operation import Operation
from Components.patter_menu import PatternMenu
from Components.status_bar import StatusBar

class ProjectEdit(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.add_pattern()

    def add_pattern(self):
        self.canvas1 = tk.Toplevel(self.root)
        self.canvas1.geometry('200x200')
        self.canvas1.minsize(150, 150)
        self.canvas1.maxsize(250, 250)
        self.canvas1.protocol('WM_DELETE_WINDOW', self.confirmExit)

        label1 = tk.Label(self.canvas1, text='Edit Project')
        label1.config(font=('helvetica', 15))
        label1.grid(row=0, column=0, padx= 10, pady=2, columnspan=2)

        label1 = tk.Label(self.canvas1, text='Project:')
        label1.config(font=('helvetica', 10))
        label1.grid(row=1, column=0, padx= 10, pady=2, columnspan=2)

        tkvar = tk.StringVar(self.root)
        self.popupMenu = PatternMenu(self.tab, self.canvas1, tkvar, top_level = True)
        self.popupMenu.grid(row=2, column=0, padx= 10, pady=2, columnspan=2)
        self.popupMenu.configure(width=20)

        label1 = tk.Label(self.canvas1, text='New Project:')
        label1.config(font=('helvetica', 10))
        label1.grid(row=3, column=0, padx= 10, pady=2, columnspan=2)

        self.entry_project = tk.Entry(self.canvas1)
        self.entry_project.grid(row=4, column=0, padx= 10, pady=2, columnspan=2)

        button_del = tk.Button(self.canvas1, text='Delete', command=self.del_proj, font=('helvetica', 9, 'bold'))
        button_del.grid(row=5, column=0, padx= 10, pady=2)

        button_add = tk.Button(self.canvas1, text='Add', command=self.add_proj, font=('helvetica', 9, 'bold'))
        button_add.grid(row=5, column=1, padx= 10, pady=2)

        self.canvas1.grab_set()

    def confirmExit(self):
        StatusBar().set("aborted - operation aborted")
        self.canvas1.destroy()

    def del_proj(self):
        proj = self.entry_project.get()
        db = Database.instance()
        if proj != "" and proj != None:
            db.delete_proj(proj)
            StatusBar().set("project deleted with success")
        else:
            if db.instance().actual_proj != "None" and db.instance().actual_proj != None:
                db.delete_proj(db.instance().actual_proj)
                StatusBar().set("project deleted with success")
            else:
                StatusBar().set("aborted - select a project or a new project name")

    def add_proj(self):
        proj = self.entry_project.get()
        db = Database.instance()
        if proj != "" and proj != None:
            db.add_item(proj, "None", "#ccc")
            StatusBar().set("project added with success")
        else:
            if db.instance().actual_proj != "None" and db.instance().actual_proj != None:
                db.add_item(db.instance().actual_proj, "None", "#ccc")
                StatusBar().set("project added with success")
            else:
                StatusBar().set("aborted - select a project or a new project name")

        self.canvas1.grab_release()
        self.canvas1.destroy()
