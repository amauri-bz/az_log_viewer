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

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self.active = None

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
       self.nb.bind("<ButtonPress-1>", self.on_close_press, True)
       self.nb.bind("<ButtonRelease-1>", self.on_close_release)

    def add_tab(self):
        tab = tk.Frame(self.nb, bg='#e6e6e6')

        combo = TextScrollCombo(tab, self)
        combo.pack(fill="both", expand=True)

        self.nb.add(tab, text = "Untitle")
        self.nb.pack(expand = 1, fill ="both")
        self.nb.select(tab)

    def refresh_tabs(self):
        if len(self.nb.children.items())<= 0:
            return None
        for item in self.nb.children.items():
            item[1].winfo_children()[0].highlight(None)

    def get_text(self):
        if len(self.nb.children.items())<= 0:
            return None
        tab_num = self.nb.index('current')
        id = self.get_frame_id()
        return self.nb.children[id].winfo_children()[0]

    def set_tab_name(self, name):
        tab_num = self.nb.index('current')
        if tab_num != None:
            self.nb.tab(tab_num, text = name)

    def get_frame_id(self):
        if len(self.nb.children.items())<= 0:
            return None

        tab_num = self.nb.index('current')
        f_ids = []
        for item in self.nb.children.keys():
            f_ids.append(item.split("frame")[1])
        return "!frame"+str(f_ids[tab_num])

    def close_corrent_tab(self, index = None):
        id = self.get_frame_id()
        if self.get_text().changed == True:
            if not messagebox.askokcancel('Close', 'Are you sure you want to close the tab?'):
                return

        if index == None:
            self.nb.forget(int(id)-1)
        else:
            self.nb.forget(index)
        del self.nb.children[id]

        if len(self.nb.children.items())<= 0:
            self.nb.pack_forget()

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.nb.identify(event.x, event.y)

        if "close" in element:
            index = self.nb.index("@%d,%d" % (event.x, event.y))
            self.nb.state(['pressed'])
            self.nb.active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.nb.instate(['pressed']):
            return

        element =  self.nb.identify(event.x, event.y)
        index = self.nb.index("@%d,%d" % (event.x, event.y))

        if self.get_text().changed == True:
            if not messagebox.askokcancel('Close', 'Are you sure you want to close the tab?'):
                return

        if "close" in element and self.nb.active == index:
            self.close_corrent_tab(index)

        self.nb.state(["!pressed"])
        self.nb.active = None
