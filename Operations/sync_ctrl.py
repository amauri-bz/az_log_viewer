from tkinter import *
from Operations.operation import Operation
from Components.status_bar import StatusBar

class SyncCtrl(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        pass

    def sync_disable(self):
        pass

    def sync_pause(self):
        pass

    def sync_continue(self):
        pass

    def reset_ext_buffer(self):
        pass
