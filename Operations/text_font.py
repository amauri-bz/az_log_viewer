import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont

from Components.db import Database
from Operations.operation import Operation
from Components.patter_menu import PatternMenu
from Components.status_bar import StatusBar

class Font(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.edit_font()

    def edit_font(self):
        db = Database.instance()
        tab_text = self.tab.get_text()
        if tab_text == None:
            StatusBar().set("aborted - aba not found")
            return
        db.global_font = tab_text.text["font"]

        self.canvas1 = tk.Toplevel(self.root)
        self.canvas1.geometry('250x150')
        self.canvas1.minsize(200, 100)
        self.canvas1.maxsize(300, 200)
        self.canvas1.protocol('WM_DELETE_WINDOW', self.confirmExit)

        label1 = tk.Label(self.canvas1, text='Edit Font')
        label1.config(font=('helvetica', 15))
        label1.grid(row=0, column=0, padx= 10, pady=2, columnspan=2)

        label1 = tk.Label(self.canvas1, text='Font:')
        label1.config(font=('helvetica', 10))
        label1.grid(row=1, column=0, padx= 2, pady=2)

        tkvar = tk.StringVar(self.root)
        self.popupMenu = FontMenu(self.tab, self.canvas1, tkvar)
        self.popupMenu.grid(row=1, column=1, padx= 2, pady=2)
        self.popupMenu.configure(width=20)

        label1 = tk.Label(self.canvas1, text='Size:')
        label1.config(font=('helvetica', 10))
        label1.grid(row=2, column=0, padx= 2, pady=2)

        self.font_size = tk.StringVar(value =db.global_font.split(" ")[1])
        sp = tk.Spinbox(self.canvas1, from_= 1, to = 50, command=self.update_font, textvariable = self.font_size)
        sp.grid(row=2, column=1, padx= 2, pady=2)
        self.update_font()

        button_cancel = tk.Button(self.canvas1, text='Cancel', command=self.cancel, font=('helvetica', 9, 'bold'))
        button_cancel.grid(row=3, column=0, padx= 10, pady=2)

        button_add = tk.Button(self.canvas1, text='Add', command=self.apply_font, font=('helvetica', 9, 'bold'))
        button_add.grid(row=3, column=1, padx= 10, pady=2)

        self.canvas1.grab_set()

    def confirmExit(self):
        StatusBar().set("aborted - operation aborted")
        self.canvas1.destroy()

    def cancel(self):
        tab_text = self.tab.get_text()
        if tab_text != None:
            db = Database.instance()
            tab_text.text.configure(font=db.global_font)
        self.canvas1.grab_release()
        self.canvas1.destroy()

    def apply_font(self):
        tab_text = self.tab.get_text()
        if tab_text != None:
            new_font = tkFont.Font(family=self.popupMenu.get_font(), size=int(self.font_size.get()))
            tab_text.text.configure(font=new_font)

            db = Database.instance()
            db.global_font = new_font

        self.canvas1.grab_release()
        self.canvas1.destroy()

    def update_font(self, *args):
        tab_text = self.tab.get_text()
        new_font = tkFont.Font(size=int(self.font_size.get()))
        tab_text.text.configure(font=new_font)


class FontMenu(ttk.OptionMenu):

    def __init__(self, tab, frame, tkvar):
        ttk.OptionMenu.__init__(self, frame, tkvar, ())
        self.tab = tab
        self.tkvar = tkvar
        self.tkvar.trace('w', self.change_dropdown)
        self.new_font = None
        self.reset_dropdown()

    def get_font(self):
        return self.new_font

    def change_dropdown(self, *args):
        db = Database.instance()
        tab_text = self.tab.get_text()
        if tab_text == None: return
        self.new_font = self.tkvar.get()
        fontExample = tkFont.Font(family=self.new_font)
        tab_text.text.configure(font=fontExample)

    def reset_dropdown(self):
        db = Database.instance()
        menu = self["menu"]
        menu.delete(0, "end")
        for string in list(tkFont.families()):
            menu.add_command(label=string,
                             command=lambda value=string:
                                  self.tkvar.set(value))

        self.tkvar.set(db.global_font.split(" ")[0])
