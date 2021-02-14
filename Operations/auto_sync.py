import tkinter as tk
import tkinter.ttk as ttk

from Components.db import Database
from Operations.operation import Operation
from Components.status_bar import StatusBar

class AutoSync(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab
       self.external = False

    def execute(self):
        self.auto_sync()

    def auto_sync(self):
        self.canvas1 = tk.Toplevel(self.root)
        self.canvas1.geometry('250x250')
        self.canvas1.minsize(200, 150)
        self.canvas1.maxsize(300, 300)
        self.canvas1.protocol('WM_DELETE_WINDOW', self.confirmExit)

        grid_pady = 2
        grid_padx = 10

        label1 = tk.Label(self.canvas1, text='Automatic File Sync')
        label1.config(font=('helvetica', 15))
        label1.grid(row=0,column=0,columnspan=2)

        var1 = tk.IntVar()
        c1 = tk.Checkbutton(self.canvas1,
            text='External sync',
            variable=var1,
            onvalue=1,
            offvalue=0,
            command= lambda var=var1: self.check_box(var))
        c1.grid(row=1,column=0,columnspan=2)

        label1 = tk.Label(self.canvas1, text='IP:')
        label1.config(font=('helvetica', 10))
        label1.grid(row=2,column=0, padx= grid_padx, pady=grid_pady)
        self.entry_ip = tk.Entry(self.canvas1)
        self.entry_ip.grid(row=2,column=1, padx= grid_padx, pady=grid_pady)

        label2 = tk.Label(self.canvas1, text='User:')
        label2.config(font=('helvetica', 10))
        label2.grid(row=3,column=0, padx= grid_padx, pady=grid_pady)
        self.entry_user = tk.Entry(self.canvas1)
        self.entry_user.grid(row=3,column=1, padx= grid_padx, pady=grid_pady)

        label3 = tk.Label(self.canvas1, text='Password:')
        label3.config(font=('helvetica', 10))
        label3.grid(row=4,column=0, padx= grid_padx, pady=grid_pady)
        self.entry_pass = tk.Entry(self.canvas1)
        self.entry_pass.grid(row=4,column=1, padx= grid_padx, pady=grid_pady)

        label4 = tk.Label(self.canvas1, text='Path:')
        label4.config(font=('helvetica', 10))
        label4.grid(row=5,column=0, padx= grid_padx, pady=grid_pady)
        self.entry_path = tk.Entry(self.canvas1)
        self.entry_path.grid(row=5,column=1, padx= grid_padx, pady=grid_pady)

        label5 = tk.Label(self.canvas1, text='Interval:')
        label5.config(font=('helvetica', 10))
        label5.grid(row=6,column=0, padx= grid_padx, pady=grid_pady)
        self.entry_interv = tk.Entry(self.canvas1)
        self.entry_interv.grid(row=6,column=1, padx= grid_padx, pady=grid_pady)

        btn_enable = tk.Button(self.canvas1, text='Enable', command=self.syn_enable, font=('helvetica', 9, 'bold'))
        btn_enable.grid(row=7,column=0, padx= grid_padx, pady=grid_pady)

        btn_disable = tk.Button(self.canvas1, text='Disable', command=self.syn_disable, font=('helvetica', 9, 'bold'))
        btn_disable.grid(row=7,column=1, padx= grid_padx, pady=grid_pady)

        self.disable_ext_param()
        self.canvas1.grab_set()

    def confirmExit(self):
        StatusBar().set("aborted - operation aborted")
        self.canvas1.destroy()

    def check_box(self, var1):
        if var1.get() == 0:
            self.external = False
            cmd = 'disabled'
        else:
            cmd = 'normal'
            self.external = True

        self.disable_ext_param(cmd)

    def disable_ext_param(self, cmd = 'disabled'):
        self.entry_ip.config(state=cmd)
        self.entry_user.config(state=cmd)
        self.entry_pass.config(state=cmd)
        self.entry_path.config(state=cmd)

    def syn_enable(self):
        tab_text = self.tab.get_text()
        if tab_text != None:
            interv = self.entry_interv.get()
            interv = int(interv) if interv != "" else 5
            if self.external != True:
                tab_text.text_sync.syn_local_enable(interv)
                StatusBar().set("local sync enabled")
            else:
                server = self.entry_ip.get()
                user = self.entry_user.get()
                passwor = self.entry_pass.get()
                path =self.entry_path.get()
                tab_text.text_sync.syn_ext_enable(server, 22, user, passwor, path, interv)
                StatusBar().set("external sync enabled")
        self.close_window()

    def syn_disable(self):
        tab_text = self.tab.get_text()
        if tab_text != None:
            tab_text.text_sync.syn_disable()
        StatusBar().set("sync disabled")
        self.close_window()

    def close_window(self):
        self.canvas1.grab_release()
        self.canvas1.destroy()
        self.canvas1.update()