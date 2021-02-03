import re
import tkinter as tk
from tkinter import ttk

from Components.db import Database
from Components.pop_up_menu import PopUpMenu

class TextScrollCombo(ttk.Frame):

    def __init__(self, root, tab):
        super().__init__(root)
        self.root = root
        self.tab = tab
        # ensure a consistent GUI size
        self.grid_propagate(False)
        # implement stretchability
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create a Text widget
        self.text = tk.Text(self)
        self.text.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.text.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.text['yscrollcommand'] = scrollb.set

        self.text.config(font=("consolas", 12), undo=True, wrap='word')
        self.text.config(borderwidth=3, relief="sunken")
        style = ttk.Style()
        style.theme_use('clam')

        self.bind_text_event()

        self.saved_path = ""

        self.popup_menu = PopUpMenu(self.root, self.tab)

    def bind_text_event(self):
        self.text.bind("<Return>", self.highlight)
        self.text.bind("<<Paste>>", self.highlight)
        self.text.bind("<Button-3>", self.popup)

    def popup(self, event):
        try:
            self.popup_menu.menubar.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.menubar.grab_release()

    def highlight(self, event):
        lastline = self.text.index("end").split(".")[0]
        for i in range(1, int(lastline)):
            contents = self.text.get("%s.0" % i, "%s.end" % i)
            db = Database.instance()
            for patern in db.get_keys():
                x = re.search(patern, contents)
                if(x != None):
                    self.text.tag_configure(patern, background=db.get_value(patern))
                    self.text.tag_add(patern, "%s.0" % i, "%s.0" % (i+1))
