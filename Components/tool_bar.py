import tkinter as tk 
import tkinter.ttk as ttk
from Components.db import Database
from Components.pater_menu import PaternMenu

from Operations.factory import OperationFactory

class ToolBar():

    def __init__(self, root, tab):
        self.root = root
        self.tab = tab
        self.op_fac = OperationFactory()
        self.add_tool_bar()

    def add_tool_bar(self):
        toolbar = tk.Frame(self.root, borderwidth=1, relief='raised', bg='#e6e6e6')

        _photo = tk.PhotoImage(file="Images/new.png")
        new_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("new", self.root, self.tab).execute)
        new_btn.image = _photo
        new_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/open.png")
        open_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("open", self.root, self.tab).execute)
        open_btn.image = _photo
        open_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/save.png")
        save_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("save", self.root, self.tab).execute)
        save_btn.image = _photo
        save_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/copy.png")
        copy_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("copy", self.root, self.tab).execute)
        copy_btn.image = _photo
        copy_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/past.png")
        past_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("past", self.root, self.tab).execute)
        past_btn.image = _photo
        past_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/cut.png")
        cut_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("cut", self.root, self.tab).execute)
        cut_btn.image = _photo
        cut_btn.pack(side=tk.LEFT)

        #-------------------------------
        # FIND SYSTEM
        #-------------------------------
        sv = tk.StringVar()
        self.edit = tk.Entry(toolbar, textvariable=sv)
        sv.trace("w", lambda name, index, mode, sv=sv, text=self.edit: self.op_fac.create("find", self.root, self.tab).find(sv, text))

        prev_btn = tk.Button(toolbar,
        text = "Prev",
        command= lambda edit=self.edit: self.op_fac.create("find", self.root, self.tab).find_prev(edit))

        next_btn = tk.Button(toolbar,
        text = "Next",
        command= lambda edit=self.edit: self.op_fac.create("find", self.root, self.tab).find_next(edit))

        self.edit.bind("<Return>", lambda event, edit=self.edit: self.op_fac.create("find", self.root, self.tab).find_next(edit))

        prev_btn.pack(side=tk.RIGHT)
        next_btn.pack(side=tk.RIGHT)
        self.edit.pack(side=tk.RIGHT, fill=tk.BOTH)

        tk.Label(toolbar,text='Find:').pack(side=tk.RIGHT)

        #-------------------------------
        # PATERN PROJECT SELECTOR
        #-------------------------------
        tkvar = tk.StringVar(self.root)
        self.popupMenu = PaternMenu(self.tab, toolbar, tkvar)
        self.popupMenu.pack(side=tk.RIGHT)
        self.popupMenu.configure(width=20)

        ttk.Label(toolbar,text='Project:').pack(side=tk.RIGHT)

        # Add the toolbar.
        toolbar.pack(side=tk.TOP,fill=tk.X)
