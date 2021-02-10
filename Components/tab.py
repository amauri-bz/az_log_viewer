import tkinter as tk
from tkinter import ttk
from Components.text import TextScrollCombo
from tkinter import messagebox

class CustomNotebook(ttk.Notebook):
    """
    A ttk Notebook with close buttons on each tab
    sorce code from:
    https://stackoverflow.com/questions/39458337/is-there-a-way-to-add-close-buttons-to-tabs-in-tkinter-ttk-notebook
    """

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True
            self.tabs = {}

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        element =  self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if self.tabs[index].changed == True:
            if not messagebox.askokcancel('Close', 'Are you sure you want to close the tab?'):
                return

        if "close" in element and self._active == index:
            for item in self.tabs[index].winfo_children():
                item.destroy()
            del self.tabs[index]
            self.forget(index)

            if len(self.tabs) <=0:
                self.pack_forget()

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe", 
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top", 
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top", 
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])

class TabCtrl(object):

    def __init__(self, root):
       self.root = root
       self.nb = CustomNotebook(root)
       #self.add_tab()

    def add_tab(self):
        tab = tk.Frame(self.nb, bg='#e6e6e6')

        combo = TextScrollCombo(tab, self)
        combo.pack(fill="both", expand=True)

        self.nb.add(tab, text = "Untitle")
        self.nb.pack(expand = 1, fill ="both")
        self.nb.select(tab)

        self.nb.tabs[self.nb.index('current')] = combo

    def refresh_tabs(self):
        for i in range(0, self.nb.index('end')):
            self.nb.tabs[i].highlight(None)

    def get_text(self):
        try:
            tab_num = self.nb.index('current')
            if tab_num != None:
                return self.nb.tabs[tab_num]
        except:
            return None

    def set_tab_name(self, name):
        tab_num = self.nb.index('current')
        if tab_num != None:
            self.nb.tab(tab_num, text = name)

    def close_corrent_tab(self):
            tab_num = self.nb.index('current')
            if tab_num != None :
                if self.tabs[index].changed == True:
                    if not messagebox.askokcancel('Close', 'Are you sure you want to close the tab?'):
                        return

                for item in self.nb.tabs[tab_num].winfo_children():
                    item.destroy()
                del self.nb.tabs[tab_num]
                self.nb.forget(tab_num)

                if len(self.nb.tabs) <=0:
                    self.nb.pack_forget()


