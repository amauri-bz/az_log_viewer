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
        toolbar = ttk.Frame(self.root, borderwidth=2, relief='raised')

        new_btn = ttk.Button(toolbar,
        text = "New",
        command=self.op_fac.create("new", self.root, self.tab_ctrl).execute)
        new_btn.pack(side=tk.TOP)

        open_btn = ttk.Button(toolbar,
        text = "Open",
        command=self.op_fac.create("open", self.root, self.tab_ctrl).execute)
        open_btn.pack(side=tk.TOP)

        save_btn = ttk.Button(toolbar,
        text = "Save",
        command=self.op_fac.create("save", self.root, self.tab_ctrl).execute)
        save_btn.pack(side=tk.TOP)

        # Add the toolbar.
        toolbar.pack(side=tk.LEFT,fill=tk.Y)