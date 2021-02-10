import tkinter as tk
import tkinter.ttk as ttk
from Components.db import Database

class PaternMenu(ttk.OptionMenu):

    def __init__(self, tab, frame, tkvar, top_level = False):
        ttk.OptionMenu.__init__(self, frame, tkvar, ())
        self.tab = tab
        self.frame = frame
        self.tkvar = tkvar
        self.top_level = top_level
        db = Database.instance()
        self.tkvar.trace('w', self.change_dropdown)
        self.reset_dropdown()
        self.tkvar.set(db.instance().actual_pattern)

    def change_dropdown(self, *args):
        db = Database.instance()
        db.instance().actual_pattern = self.tkvar.get()
        if self.top_level == False:
            text = self.tab.get_text()
            if text != None:
                text.highlight(None)

    def reset_dropdown(self):
        db = Database.instance()
        menu = self["menu"]
        menu.delete(0, "end")
        for string in db.get_projects():
            menu.add_command(label=string,
                             command=lambda value=string:
                                  self.tkvar.set(value))
        self.tkvar.set(db.instance().actual_pattern)
        self.after(2000, self.reset_dropdown)
