import tkinter as tk
import re
from Operations.operation import Operation

class BookMarks(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        pass

    def add_bookmark(self):
        tab_text = self.tab.get_text().text
        if tab_text == None: return
        index = tab_text.index(tk.INSERT)

        line_idx = index.split(".")[0]
        tab_text.tag_add("bmark-"+index.split('.')[0], "%s.0"%line_idx, "%s.end"%line_idx)
        tab_text.tag_config("bmark-"+index.split('.')[0], foreground='blue')

    def remove_bookmark(self):
        tab_text = self.tab.get_text().text
        if tab_text == None: return
        index = tab_text.index(tk.INSERT)
        line_idx = index.split(".")[0]
        tab_text.tag_remove("bmark-"+index.split('.')[0], "%s.0"%line_idx, "%s.end"%line_idx)

    def remove_all_bookmark(self):
        tab_text = self.tab.get_text().text
        if tab_text == None: return

        for tag in tab_text.tag_names():
            if tag.find("bmark") != -1:
                tab_text.tag_remove(tag, '1.0', 'end')

    def next_bookmark(self):
        tab_text = self.tab.get_text().text
        if tab_text == None: return
        actual_index = tab_text.index(tk.INSERT)

        tag_list = []
        for tag in tab_text.tag_names():
            if tag.find("bmark") != -1:
                tag_list.append(int(tag.split('-')[1]))
        tag_list.sort()

        for line in tag_list:
            if line >= int(actual_index.split('.')[0]):
                tab_text.see("%d.0"%(line))
                break

    def prev_bookmark(self):
        tab_text = self.tab.get_text().text
        if tab_text == None: return
        actual_index = tab_text.index(tk.INSERT)

        tag_list = []
        for tag in tab_text.tag_names():
            if tag.find("bmark") != -1:
                tag_list.append(int(tag.split('-')[1]))
        tag_list.sort(reverse=True)

        for line in tag_list:
            if line <= int(actual_index.split('.')[0]):
                tab_text.see("%d.0"%(line))
                break