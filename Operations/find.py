import tkinter as tk
from tkinter import messagebox
from Operations.operation import Operation
from Components.db import Database

class Find(Operation):

    def __init__(self, root, tab):
        self.root = root
        self.tab = tab

    def execute(self):
        pass

    def find(self, sv, edit):
        db = Database.instance()
        tag_text = self.tab.get_text().text

        tag_text.tag_remove('found', '1.0', tk.END)
        s = edit.get()
        if s:
            idx = '1.0'
            while 1:
                idx = tag_text.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                tag_text.tag_add('found', idx, lastidx)
                idx = lastidx
        db.actual_pos = '0.0'
        tag_text.tag_config('found', foreground='red')

    def find_next(self, edit):
        db = Database.instance()
        tag_text = self.tab.get_text().text
        edit_txt = edit.get()

        if db.actual_pos == '0.0':
            db.actual_pos = '1.0'

        idx = tag_text.search(edit_txt, db.actual_pos, forwards=True, nocase=1, stopindex=tk.END)
        if idx:
            db.actual_pos = '%s+%dc' % (idx, len(edit_txt))
            tag_text.see(db.actual_pos)

    def find_prev(self, edit):
        db = Database.instance()
        tag_text = self.tab.get_text().text
        edit_txt = edit.get()

        if db.actual_pos == '0.0':
            db.actual_pos = tk.END

        idx = tag_text.search(edit_txt, db.actual_pos, backwards=True, nocase=1, stopindex='1.0')
        if idx:
            db.actual_pos = '%s-%dc' % (idx, len(edit_txt))
            tag_text.see(db.actual_pos)