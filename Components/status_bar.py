import tkinter as tk 
import tkinter.ttk as ttk

class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance

class StatusBar(metaclass=Singleton):

    def __init__(self, root):
        self.root = root
        self.statusbar = ttk.Label(self.root, text="ready...", relief='sunken')
        self.statusbar.pack(side='bottom', fill='x')

    def set_status(self, msg):
        self.statusbar.config(text=msg)