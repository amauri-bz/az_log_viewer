from tkinter import simpledialog
from Operations.operation import Operation

class GoToLine(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return
        lineno = simpledialog.askinteger(
            "Go to Line", "Type a line number and press Enter:",
            parent=tab_text.winfo_toplevel())
        if lineno is not None:
            column = tab_text.text.index('insert').split('.')[1]
            tab_text.text.mark_set('insert', '%d.%s' % (lineno, column))
            tab_text.text.see('insert')
        tab_text.text.focus()