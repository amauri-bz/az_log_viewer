import tkinter as tk
from Operations.factory import OperationFactory

class PopUpMenu:
    def __init__(self, root, tab):
        self.root = root
        self.tab_ctrl = tab
        self.op_fac = OperationFactory()

        self.menubar = tk.Menu(root, tearoff=0)
        self.build_edit_menu()

    def build_edit_menu(self):
        self.menubar = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_command(label="Add Patern", command=self.op_fac.create("patern", self.root, self.tab_ctrl).execute)
        self.menubar.add_separator()
        self.menubar.add_command(label="Cut", command=self.op_fac.create("cut", self.root, self.tab_ctrl).execute)
        self.menubar.add_command(label="Copy", command=self.op_fac.create("copy", self.root, self.tab_ctrl).execute)
        self.menubar.add_command(label="Paste", command=self.op_fac.create("past", self.root, self.tab_ctrl).execute)
        self.menubar.add_command(label="Select All", command=self.op_fac.create("select_all", self.root, self.tab_ctrl).execute)