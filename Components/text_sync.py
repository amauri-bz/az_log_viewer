from datetime import datetime
from Components.scp_connect import ScpConnect
from Components.status_bar import StatusBar

class TextSync:

    def __init__(self, tab):
        self.refresh_enable = False
        self.server = ""
        self.port = ""
        self.user = ""
        self.passwor = ""
        self.path = ""
        self.interv = 0
        self.tab = tab
        self.scp = ScpConnect()

    def syn_disable(self):
        self.refresh_enable = False
        self.server = ""
        self.port = ""
        self.user = ""
        self.passwor = ""
        self.path = ""
        self.interv = 0

    def syn_local_enable(self, interv = 5):
        self.refresh_enable = True
        self.refresh_interv = int(interv)
        self.local_refresh()

    def syn_ext_enable(self, server, port, user, passwor, path, interv):
        self.refresh_enable = True
        self.server = server
        self.port = port
        self.user = user
        self.passwor = passwor
        self.path = path
        self.refresh_interv = int(interv)
        self.scp.connect(server, port, user, passwor)
        self.ext_refresh()

    def ext_refresh(self):
        valeu = self.scp.get_text(self.path)
        if valeu == None: return

        tab_text = self.tab.get_text()
        if tab_text == None: return
        if tab_text.text == None: return

        tab_text.text.delete('1.0', 'end')
        tab_text.text.insert('1.0', valeu)
        tab_text.text.see('end')

        if self.refresh_enable:
            tab_text.text.after(self.refresh_interv*1000, self.ext_refresh)
            StatusBar().set("synced: %s" %(datetime.now().strftime("%H:%M:%S")))

    def local_refresh(self):
        tab_text = self.tab.get_text()
        if tab_text == None: return
        if tab_text.text == None: return
        filename = tab_text.saved_path
        if filename == "": return

        f = open(filename, 'r')
        valeu = f.read()
        tab_text.text.delete('1.0', 'end')
        tab_text.text.insert('1.0', valeu)
        f.close()
        tab_text.text.see('end')

        if self.refresh_enable:
            tab_text.text.after(self.refresh_interv*1000, self.local_refresh)
            StatusBar().set("synced: %s" %(datetime.now().strftime("%H:%M:%S")))
