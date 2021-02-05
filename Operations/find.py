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

    def find(self, edit, forward = False):
        tag_text = self.tab.get_text().text
        edit_txt = edit.get()
        db = Database.instance()

        db.find_list.clear()

        tag_text.tag_remove('found', '1.0', tk.END)
        if edit_txt:
            idx = '1.0' if forward else tk.END
            while 1:
                if forward:
                    idx = tag_text.search(edit_txt, idx, forwards=True, nocase=1, stopindex=tk.END)
                else:
                    idx = tag_text.search(edit_txt, idx, backwards=True, nocase=1, stopindex='1.0')

                if not idx: break
                lastidx = '%s+%dc' % (idx, len(edit_txt))
                tag_text.tag_add('found', idx, lastidx)
                db.find_list.append(lastidx)
                idx = lastidx
        db.actual_pos = 0 if forward else len(db.find_list)
        print(db.find_list)
        print(db.actual_pos)
        tag_text.tag_config('found', foreground='red')

    def find_next(self, edit):
        self.find(edit, True)
        db = Database.instance()
        tag_text = self.tab.get_text().text

        db.actual_pos+=1
        if db.actual_pos < len(db.find_list)-1:
            tag_text.see(db.find_list[db.actual_pos])
        else:
            db.actual_pos = 0
    
    def find_prev(self, edit):
        self.find(edit, False)
        db = Database.instance()
        tag_text = self.tab.get_text().text

        db.actual_pos-=1
        if db.actual_pos > len(db.find_list):
            tag_text.see(db.find_list[db.actual_pos])
        else:
            db.actual_pos = len(db.find_list)-1