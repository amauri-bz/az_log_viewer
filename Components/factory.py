from Operations.new import New
from Operations.save import Save
from Operations.project import ProjectEdit
from Operations.pattern import PatternEdit
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
from Operations.find import Find
from Operations.text_font import Font
from Operations.auto_sync import AutoSync
from Operations.sync_ctrl import SyncCtrl
from Operations.bookmarks import BookMarks
from Operations.go_to_line import GoToLine

class OperationFactory:
    def create(self, name, root, tab):
        if name == 'new':
            return New(root, tab)
        elif name == 'save':
            return Save(root, tab, name)
        elif name == 'save_as':
            return Save(root, tab, name)
        elif name == 'project':
            return ProjectEdit(root, tab)
        elif name == 'pattern':
            return PatternEdit(root, tab)
        elif name == 'open':
            return Open(root, tab)
        elif name == 'close':
            return Close(root, tab)
        elif name == 'exit':
            return Exit(root, tab)
        elif name == 'select_all':
            return SelectAll(root, tab)
        elif name == 'about':
            return About(root, tab)
        elif name == 'copy':
            return Copy(root, tab)
        elif name == 'past':
            return Past(root, tab)
        elif name == 'cut':
            return Cut(root, tab)
        elif name == 'undo':
            return Undo(root, tab)
        elif name == 'redo':
            return Redo(root, tab)
        elif name == 'find':
            return Find(root, tab)
        elif name == 'bookmark':
            return BookMarks(root, tab)
        elif name == 'go_to_line':
            return GoToLine(root, tab)
        elif name == 'auto_sync':
            return AutoSync(root, tab)
        elif name == 'font':
            return Font(root, tab)
        elif name == 'sync_pause':
            return SyncCtrl(root, tab)
        elif name == 'sync_continue':
            return SyncCtrl(root, tab)
        elif name == 'sync_disable':
            return SyncCtrl(root, tab)
        elif name == 'reset_ext_buffer':
            return SyncCtrl(root, tab)
        else:
            return Help(root, tab)
