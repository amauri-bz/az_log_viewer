import tkinter as tk 
import tkinter.ttk as ttk

from Operations.factory import OperationFactory

class ToolBar():

    def __init__(self, root, tab):
        self.root = root
        self.tab_ctrl = tab
        self.op_fac = OperationFactory()
        self.add_tool_bar()
        self.find_list = []
        self.actual_pos = 0

    def add_tool_bar(self):
        toolbar = tk.Frame(self.root, borderwidth=1, relief='raised', bg='#e6e6e6')

        _photo = tk.PhotoImage(file="Images/new.png")
        new_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("new", self.root, self.tab_ctrl).execute)
        new_btn.image = _photo
        new_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/open.png")
        open_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("open", self.root, self.tab_ctrl).execute)
        open_btn.image = _photo
        open_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/save.png")
        save_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("save", self.root, self.tab_ctrl).execute)
        save_btn.image = _photo
        save_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/copy.png")
        copy_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("copy", self.root, self.tab_ctrl).execute)
        copy_btn.image = _photo
        copy_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/past.png")
        past_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("past", self.root, self.tab_ctrl).execute)
        past_btn.image = _photo
        past_btn.pack(side=tk.LEFT)

        _photo = tk.PhotoImage(file="Images/cut.png")
        cut_btn = tk.Button(toolbar,
        image = _photo,
        command=self.op_fac.create("cut", self.root, self.tab_ctrl).execute)
        cut_btn.image = _photo
        cut_btn.pack(side=tk.LEFT)



        next_btn = tk.Button(toolbar,
        text = "Next",
        command=self.next)
        next_btn.pack(side=tk.RIGHT)

        sv = tk.StringVar()
        sv.trace("w", lambda name, index, mode, sv=sv: self.find(sv))
        self.edit = tk.Entry(toolbar, textvariable=sv)
        self.edit.pack(side=tk.RIGHT, fill=tk.BOTH)
        tk.Label(toolbar,text='Find:').pack(side=tk.RIGHT)

        # Add the toolbar.
        toolbar.pack(side=tk.TOP,fill=tk.X)

    def find(self, sv):
        self.tag_text = self.tab_ctrl.get_text().text

        self.tag_text.tag_remove('found', '1.0', tk.END)
        s = self.edit.get()
        if s:
            idx = '1.0'
            while 1: 
                idx = self.tag_text.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))
                self.tag_text.tag_add('found', idx, lastidx)
                self.find_list.append(lastidx)
                idx = lastidx
        self.tag_text.see(self.find_list[0])
        self.actual_pos = 0
        self.tag_text.tag_config('found', foreground='red')

    def next(self):
        self.actual_pos+=1
        if self.actual_pos < len(self.find_list):
            self.tag_text.see(self.find_list[self.actual_pos])
        else:
            self.actual_pos = 0

