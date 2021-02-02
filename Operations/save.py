import os
from tkinter import filedialog
from Operations.operation import Operation

class Save(Operation):

    def __init__(self, root, tab, cmd_name):
       self.root = root
       self.cmd_name = cmd_name
       self.tab = tab

    def execute(self):
        tab_text = self.tab.get_text()
        filename = tab_text.saved_path
        if self.cmd_name == "save_as" or filename == "":
            filename = filedialog.asksaveasfilename(
                initialdir="/",
                title="Select An Image",
                filetypes=(
                        ("text files", "*.txt"),
                        ("log files", "*.log*")))
        if filename == '':
            return
        
        if self.save_file(tab_text, filename)==True:
            tab_text.saved_path = filename
            head, tail = os.path.split(filename)
            self.tab.set_tab_name(tail)
        else:
            print("saving '%s' failed", filename)

    def save_file(self, tab_text, path):
        try:
            f = open(path, 'w')
            f.write(tab_text.text.get('1.0', 'end'))
            f.close()
            return True
        except (OSError, UnicodeError) as e:
            pass
        return False
