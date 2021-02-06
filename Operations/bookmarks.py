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
        index = tab_text.index(tk.INSERT)
        tab_text.mark_set("bmark-"+index.split('.')[0], index)

    def remove_bookmark(self):
        tab_text = self.tab.get_text().text
        index = tab_text.index(tk.INSERT)
        tab_text.mark_unset("bmark-"+index.split('.')[0])

    def remove_all_bookmark(self):
        tab_text = self.tab.get_text().text
        for mark in tab_text.mark_names():
            if mark.find("bmark") != -1:
                tab_text.mark_unset(mark)

    def next_bookmark(self):
        tab_text = self.tab.get_text().text
        actual_index = tab_text.index(tk.INSERT)

        mark_list = []
        for mark in tab_text.mark_names():  
            if mark.find("bmark") != -1:
                mark_list.append(int(mark.split('-')[1]))
        mark_list.sort()

        for line in mark_list:
            if line >= int(actual_index.split('.')[0]):
                tab_text.see("%d.0"%(line))
                break

    def prev_bookmark(self):
        tab_text = self.tab.get_text().text
        actual_index = tab_text.index(tk.INSERT)

        mark_list = []
        for mark in tab_text.mark_names():  
            if mark.find("bmark") != -1:
                mark_list.append(int(mark.split('-')[1]))
        mark_list.sort(reverse=True)

        for line in mark_list:
            if line <= int(actual_index.split('.')[0]):
                tab_text.see("%d.0"%(line))
                break