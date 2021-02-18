import re
import tkinter as tk
from tkinter import ttk

from Components.db import Database
from Components.pop_up_menu import PopUpMenu
from Components.text_sync import TextSync
from Components.custom_text import *

class TextScrollCombo(tk.Frame):

    def __init__(self, root, tab):
        super().__init__(root, bg='#e6e6e6')
        self.root = root
        self.tab = tab
        self.changed = False
        self.refresh_enable = False
        self.refresh_interv = 5

        # create a Text widget
        self.text = CustomText(self)
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.text.yview)
        self.text['yscrollcommand'] = scrollb.set

        self.linenumbers.pack(side="left", fill="y")
        scrollb.pack(side="right", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        db = Database.instance()
        if db.global_font != None:
            self.text.config(font=db.global_font, undo=True, wrap='word')
        else:
            self.text.config(font=("consolas", 10), undo=True, wrap='word')

        self.text.config(borderwidth=3, relief="sunken")
        style = ttk.Style()
        style.theme_use('clam')

        self.bind_text_event()

        self.saved_path = ""

        self.popup_menu = PopUpMenu(self.root, self.tab)
        self.text_sync = TextSync(self.tab)

    def bind_text_event(self):
        self.text.bind("<<Highlight>>", self.highlight)
        self.text.bind("<Button-3>", self.popup)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        if self.text.index(tk.INSERT) != "1.0":
            self.changed = True
        self.linenumbers.redraw()

    def popup(self, event):
        try:
            self.popup_menu.menubar.tk_popup(event.x_root+70, event.y_root, 0)
        finally:
            self.popup_menu.menubar.grab_release()

    def clean_highlight(self):
        for tag in self.text.tag_names():
            x = re.search("ptrn-", tag)
            if x  != None:
                self.text.tag_remove(tag, '1.0', tk.END)

    def highlight(self, event):
        self.clean_highlight()

        lastline = self.text.index("end").split(".")[0]
        for i in range(1, int(lastline)):
            contents = self.text.get("%s.0" % i, "%s.end" % i)
            db = Database.instance()
            for pattern in db.get_keys():
                x = re.search(pattern, contents)
                if(x != None):
                    self.text.tag_configure("ptrn-" + pattern, background=db.get_value(pattern))
                    self.text.tag_add("ptrn-" + pattern, "%s.0" % i, "%s.end" % i)
