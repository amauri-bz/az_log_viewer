import tkinter as tk 
import tkinter.ttk as ttk

from Operations.factory import OperationFactory

class ToolBar():

    def __init__(self, root, tab):
        self.root = root
        self.tab_ctrl = tab
        self.op_fac = OperationFactory()
        self.add_tool_bar()

    def add_tool_bar(self):
        toolbar = tk.Frame(self.root, borderwidth=1, relief='raised', bg='#e6e6e6')

        _photo = tk.PhotoImage(file="Images/new.png")
        new_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("new", self.root, self.tab_ctrl).execute)
        new_btn.image = _photo
        new_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/open.png")
        open_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("open", self.root, self.tab_ctrl).execute)
        open_btn.image = _photo
        open_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/save.png")
        save_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("save", self.root, self.tab_ctrl).execute)
        save_btn.image = _photo
        save_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/copy.png")
        copy_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("copy", self.root, self.tab_ctrl).execute)
        copy_btn.image = _photo
        copy_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/past.png")
        past_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("past", self.root, self.tab_ctrl).execute)
        past_btn.image = _photo
        past_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/cut.png")
        cut_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("cut", self.root, self.tab_ctrl).execute)
        cut_btn.image = _photo
        cut_btn.pack(side=tk.LEFT)

        # Add the toolbar.
        toolbar.pack(side=tk.TOP,fill=tk.X)