from Operations.new import New
from Operations.save import Save
from Operations.patern import Patern
from Operations.open import Open
from Operations.close import Close
from Operations.exit import Exit
from Operations.select_all import SelectAll
from Operations.about import About
from Operations.help import Help
from Operations.copy import Copy
from Operations.past import Past
from Operations.cut import Cut
from Operations.undo import Undo
from Operations.redo import Redo

class OperationFactory:
    def create(self, name, root, tab_ctrl):
        if name == 'new':
            return New(root, tab_ctrl)
        elif name == 'save':
            return Save(root, tab_ctrl, name)
        elif name == 'save_as':
            return Save(root, tab_ctrl, name)
        elif name == 'patern':
            return Patern(root, tab_ctrl)
        elif name == 'open':
            return Open(root, tab_ctrl)
        elif name == 'close':
            return Close(root, tab_ctrl)
        elif name == 'exit':
            return Exit(root, tab_ctrl)
        elif name == 'select_all':
            return SelectAll(root, tab_ctrl)
        elif name == 'about':
            return About(root, tab_ctrl)
        elif name == 'copy':
            return Copy(root, tab_ctrl)
        elif name == 'past':
            return Past(root, tab_ctrl)
        elif name == 'cut':
            return Cut(root, tab_ctrl)
        elif name == 'undo':
            return Undo(root, tab_ctrl)
        elif name == 'redo':
            return Redo(root, tab_ctrl)
        else:
            return Help(root, tab_ctrl)
