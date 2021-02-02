from Operations.operation import Operation

class New(Operation):

    def __init__(self, root, tab):
       self.root = root
       self.tab = tab

    def execute(self):
        self.tab.add_tab()