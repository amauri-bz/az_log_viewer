import tkinter as tk
from tkinter import messagebox
from Operations.operation import Operation
from Components.db import Database

class Find(Operation):

    def __init__(self, root, tab):
        self.root = root
        self.tab = tab
        tab_text = self.tab.get_text().text
        tab_text.bind("<<Find>>", self._on_change)

    def execute(self):
        pass

    def find(self, sv, edit, text=""):
        db = Database.instance()
        tab_text = self.tab.get_text().text

        tab_text.tag_remove('found', '1.0', tk.END)
        s = edit.get() if edit != None else text
        db.actual_find = s
        if s:
            idx = '1.0'
            while 1:
                idx = tab_text.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                tab_text.tag_add('found', idx, lastidx)
                idx = lastidx

        if tab_text.index(tk.INSERT) != tab_text.index("end-1c"):
            db.actual_pos = tab_text.index(tk.INSERT)
        else:
            db.actual_pos = '0.0'
        tab_text.tag_config('found', foreground='red')

    def find_next(self, edit):
        db = Database.instance()
        tab_text = self.tab.get_text().text
        edit_txt = edit.get()

        if edit_txt =="":
            return

        if db.actual_pos == '0.0':
            db.actual_pos = '1.0'

        idx = tab_text.search(edit_txt, db.actual_pos, forwards=True, nocase=1, stopindex=tk.END)
        if idx:
            db.actual_pos = '%s+%dc' % (idx, len(edit_txt))
            tab_text.see(db.actual_pos)

    def find_prev(self, edit):
        db = Database.instance()
        tab_text = self.tab.get_text().text
        edit_txt = edit.get()

        if edit_txt =="":
            return

        if db.actual_pos == '0.0':
            db.actual_pos = tk.END

        idx = tab_text.search(edit_txt, db.actual_pos, backwards=True, nocase=1, stopindex='1.0')
        if idx:
            db.actual_pos = '%s-%dc' % (idx, len(edit_txt))
            tab_text.see(db.actual_pos)

    def _on_change(self, event):
        tab_text = self.tab.get_text().text
        if tab_text.index(tk.INSERT) != "1.0":
            db = Database.instance()
            self.find(None, None, text=db.actual_find)
