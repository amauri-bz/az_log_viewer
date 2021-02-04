import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from Operations.factory import OperationFactory
from Components.tab_ctrl import TabCtrl
from Components.tool_bar import ToolBar
from Components.menu import Menu
from Components.status_bar import StatusBar

class App:
    def __init__(self, root):
        self.root = root
        self.op_fac = OperationFactory()
        self.tab_ctrl = TabCtrl(self.root)
        self.toolbar = ToolBar(self.root, self.tab_ctrl)
        self.menu = Menu(self.root, self.tab_ctrl)
        self.status_bar = StatusBar(self.root)
        self.status_bar.instance.set_status("ola")

def confirmExit():
    if messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
        root.destroy()

if __name__ == '__main__':
    root = tk.Tk()

    root.title("Az-Log-Viewer")
    root.geometry('800x500')
    root.minsize(400, 200)
    root.protocol('WM_DELETE_WINDOW', confirmExit)
    root.config(bg='#e6e6e6')

    App(root)

    root.mainloop()