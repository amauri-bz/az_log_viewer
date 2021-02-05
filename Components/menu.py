import tkinter as tk

from Operations.factory import OperationFactory
from Components.tab import TabCtrl

class Menu:
    def __init__(self, root, tab):
        self.root = root
        self.tab = tab
        self.op_fac = OperationFactory()
 
        self.menubar = tk.Menu(root)
        self.build_file_menu()
        self.build_edit_menu()
        self.build_patern_menu()
        self.build_help_menu()
        self.root.config(menu=self.menubar)

    def build_file_menu(self):
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.op_fac.create("new", self.root, self.tab).execute)
        filemenu.add_command(label="Open", command=self.op_fac.create("open", self.root, self.tab).execute)
        filemenu.add_command(label="Save", command=self.op_fac.create("save", self.root, self.tab).execute)
        filemenu.add_command(label="Save as...", command=self.op_fac.create("save_as", self.root, self.tab).execute)
        filemenu.add_command(label="Close", command=self.op_fac.create("close", self.root, self.tab).execute)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.op_fac.create("exit", self.root, self.tab).execute)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def build_edit_menu(self):
        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.op_fac.create("undo", self.root, self.tab).execute)
        editmenu.add_command(label="Redo", command=self.op_fac.create("redo", self.root, self.tab).execute)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.op_fac.create("cut", self.root, self.tab).execute)
        editmenu.add_command(label="Copy", command=self.op_fac.create("copy", self.root, self.tab).execute)
        editmenu.add_command(label="Paste", command=self.op_fac.create("past", self.root, self.tab).execute)
        editmenu.add_command(label="Select All", command=self.op_fac.create("select_all", self.root, self.tab).execute)
        self.menubar.add_cascade(label="Edit", menu=editmenu)

    def build_patern_menu(self):
        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Add", command=self.op_fac.create("patern", self.root, self.tab).execute)
        self.menubar.add_cascade(label="Patern", menu=editmenu)

    def build_help_menu(self):
        helpmenu = tk.Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.op_fac.create("help", self.root, self.tab).execute)
        helpmenu.add_command(label="About...", command=self.op_fac.create("about", self.root, self.tab).execute)
        self.menubar.add_cascade(label="Help", menu=helpmenu)
