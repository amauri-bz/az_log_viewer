from Operations.operation import Operation

class Close(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.tab.close_corrent_tab()
