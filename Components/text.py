import re
import tkinter as tk
from tkinter import ttk

from Components.db import Database
from Components.pop_up_menu import PopUpMenu

#Line number solution from:
#https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

#Line number solution from:
#https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        result = ""
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        try:
            result = self.tk.call(cmd)
        except:
            pass

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")):
            self.event_generate("<<Change>>", when="tail")
            self.event_generate("<<Find>>", when="tail")
            self.event_generate("<<Highlight>>", when="tail")

        # return what the actual widget returned
        return result


class TextScrollCombo(tk.Frame):

    def __init__(self, root, tab):
        super().__init__(root, bg='#e6e6e6')
        self.root = root
        self.tab = tab
        self.changed = False

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

        self.text.config(font=("consolas", 12), undo=True, wrap='word')
        self.text.config(borderwidth=3, relief="sunken")
        style = ttk.Style()
        style.theme_use('clam')

        self.bind_text_event()

        self.saved_path = ""

        self.popup_menu = PopUpMenu(self.root, self.tab)

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

    def highlight(self, event):
        lastline = self.text.index("end").split(".")[0]
        for i in range(1, int(lastline)):
            contents = self.text.get("%s.0" % i, "%s.end" % i)
            db = Database.instance()
            for patern in db.get_keys():
                x = re.search(patern, contents)
                if(x != None):
                    self.text.tag_configure(patern, background=db.get_value(patern))
                    self.text.tag_add(patern, "%s.0" % i, "%s.end" % i)
