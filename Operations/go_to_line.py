from tkinter import simpledialog
from Operations.operation import Operation

class GoToLine(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        tab = self.tab.get_text()
        lineno = simpledialog.askinteger(
            "Go to Line", "Type a line number and press Enter:",
            parent=tab.winfo_toplevel())
        if lineno is not None:
            column = tab.text.index('insert').split('.')[1]
            tab.text.mark_set('insert', '%d.%s' % (lineno, column))
            tab.text.see('insert')
        tab.text.focus()