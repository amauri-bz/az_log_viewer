import os
from tkinter import filedialog
from Operations.operation import Operation

class Open(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):

        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select An Image",
            filetypes=(
                    ("text files", "*.txt"),
                    ("log files", "*.log*")))

        if filename == '':
            return

        self.tab.add_tab()
        tab_text = self.tab.get_text()
        if tab_text == None: return
        
        self.open_file(tab_text, filename)
        tab_text.saved_path = filename
        head, tail = os.path.split(filename)
        self.tab.set_tab_name(tail)  

    def open_file(self, tab_text, filename):
        f = open(filename, 'r')
        f2 = f.read()
        tab_text.text.delete('1.0', 'end')
        tab_text.text.insert('1.0', f2)
        f.close()
