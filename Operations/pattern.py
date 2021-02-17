import re

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.colorchooser import askcolor

from Components.db import Database
from Operations.operation import Operation
from Components.patter_menu import PatternMenu
from Components.status_bar import StatusBar
from Components.custom_text import CustomText

class TextPaternList(tk.Frame):

    def __init__(self, root):
        super().__init__(root, bg='#e6e6e6')
        self.root = root
        self.data = {}

        # create a Text widget
        self.text = CustomText(self, height = 25, width = 20)

        # create a Scrollbar and associate it with txt
        scrollb = ttk.Scrollbar(self, command=self.text.yview)
        self.text['yscrollcommand'] = scrollb.set

        scrollb.pack(side="right", fill="y")
        self.text.pack(side="right", fill="both")

        self.text.config(font=("consolas", 10), undo=True, wrap='word')
        self.text.config(borderwidth=3, relief="sunken")
        style = ttk.Style()
        style.theme_use('clam')
        self.text.tag_configure("select_tag", background="#ccc")

        self.init_text(None)

    def init_text(self, event):
        self.text.configure(state='normal')
        db = Database.instance()
        self.text.delete('1.0', 'end')
        self.data.clear()

        for pattern in db.get_keys():
            self.data[pattern] = db.get_value(pattern)
            self.text.insert('end', pattern+"\n")
        self.update_text()

    def update_text(self):
        self.text.configure(state='normal')
        self.text.delete('1.0', 'end')

        for key, item in self.data.items():
            self.text.insert('end', key+"\n")
        self.text.tag_remove("select_tag", '1.0', tk.END)
        self.text.configure(state='disabled')


class PatternEdit(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.edit_pattern()

    def edit_pattern(self):
        self.canvas = tk.Toplevel(self.root)
        self.canvas.geometry('350x600')
        self.canvas.minsize(300, 550)
        self.canvas.maxsize(400, 650)
        self.canvas.protocol('WM_DELETE_WINDOW', self.confirmExit)

        label1 = tk.Label(self.canvas, text='Edit Pattern')
        label1.config(font=('helvetica', 15))
        label1.grid(row=0, column=0, columnspan=4, padx= 10, pady=10)

        tkvar = tk.StringVar(self.root)
        self.popupMenu = PatternMenu(self.tab, self.canvas, tkvar, top_level = True)
        self.popupMenu.grid(row=1, column=0, columnspan=4, padx= 10, pady=10)
        self.popupMenu.configure(width=20)

        self.entry_pattern = tk.Entry(self.canvas)
        self.entry_pattern.grid(row=2, column=0, columnspan=2, padx= 10, pady=10)

        button_add = tk.Button(self.canvas, text='Add', command=self.add_patter, font=('helvetica', 9, 'bold'))
        button_add.grid(row=2, column=2, padx= 10, pady=10)

        self.text_frame = TextPaternList(self.canvas)
        self.text_frame.grid(row=3, column=0, padx= 10, pady=2, columnspan=2)

        self.button_color = tk.Button(self.canvas,
                text="Color",
                command=self.color_chooser,
                font=('helvetica', 9, 'bold'))
        self.button_color.grid(row=3, column=2, padx= 10, pady=2)

        button_delete = tk.Button(self.canvas, text='Delete', command=self.btn_delete, font=('helvetica', 9, 'bold'))
        button_delete.grid(row=3, column=3, padx= 10, pady=10)

        button_apply = tk.Button(self.canvas, text='Apply', command=self.btn_apply, font=('helvetica', 9, 'bold'))
        button_apply.grid(row=4, column=1, padx=10, pady=10)

        button_cancel = tk.Button(self.canvas, text='Cancel', command=self.btn_end, font=('helvetica', 9, 'bold'))
        button_cancel.grid(row=4, column=2, padx=10, pady=10)

        self.canvas.grab_set()
        self.bind_text_event()
        self.check_selection()

    def confirmExit(self):
        StatusBar().set("aborted - operation aborted")
        self.canvas.destroy()

    def btn_apply(self):
        db = Database.instance()
        db.delete_proj(db.instance().actual_proj)

        for patern, color in self.text_frame.data.items():
            db.add_item(db.instance().actual_proj, patern, color)

        self.btn_end()

    def btn_delete(self):
        line_idx = self.text_frame.text.index("insert").split(".")[0]
        pattern = self.text_frame.text.get("%s.0"%line_idx, "%s.end"%line_idx)
        if pattern in self.text_frame.data:
            del self.text_frame.data[pattern]
            self.text_frame.update_text()
            self.button_color.configure(bg="#ccc")

    def btn_end(self):
        self.canvas.grab_release()
        self.canvas.destroy()
        self.tab.refresh_tabs()

    def add_patter(self):
        color = askcolor(title = "Pattern Color")
        if color != None:
            pattern = self.entry_pattern.get()
            StatusBar().set("new patern:%s color:%s"%(pattern, color[1]))
            self.text_frame.data[pattern] = color[1]
            self.text_frame.update_text()
            self.entry_pattern.delete(0,"end")
        else:
            StatusBar().set("aborted - operation aborted")

    def color_chooser(self):
        color = askcolor(title = "Pattern Color")
        if color != None:
            line_idx = self.text_frame.text.index("insert").split(".")[0]
            pattern = self.text_frame.text.get("%s.0"%line_idx, "%s.end"%line_idx)
            if pattern in self.text_frame.data:
                StatusBar().set("new color %s"%(color[1]))
                self.text_frame.data[pattern] = color[1]
                self.button_color.configure(bg = self.text_frame.data[pattern])
        else:
            StatusBar().set("aborted - operation aborted")

    def bind_text_event(self):
        self.text_frame.text.bind("<<Change>>", self._on_change)
        self.text_frame.text.bind("<Configure>", self._on_change)
        self.popupMenu.bind("<<ProjChange>>", self.text_frame.init_text)

    def _on_change(self, event):
        line_idx = self.text_frame.text.index("insert").split(".")[0]
        pattern = self.text_frame.text.get("%s.0"%line_idx, "%s.end"%line_idx)
        if pattern in self.text_frame.data:
            self.text_frame.text.tag_remove("select_tag", '1.0', tk.END)
            self.text_frame.text.tag_add("select_tag", "%s.0" % line_idx, "%s.end" % line_idx)
            self.button_color.configure(bg = self.text_frame.data[pattern])

    def check_selection(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return
        text = tab_text.text.get("sel.first", "sel.last")
        if text != '':
            self.entry_pattern.delete(0,tk.END)
            self.entry_pattern.insert(0, text)
