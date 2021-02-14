from Components.scp_connect import ScpConnect

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
        self.tab_text = self.tab.get_text()
        self.scp = ScpConnect()

    def syn_disable(self):
        self.refresh_enable = False
        self.server = ""
        self.port = ""
        self.user = ""
        self.passwor = ""
        self.path = ""
        self.interv = 0

    def syn_enable(self, interv = 5):
        self.refresh_enable = True
        self.refresh_interv = int(interv)
        self.local_refresh()

    def syn_enable(self, server, port, user, passwor, path, interv):
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
        if self.tab_text.text == None: return

        self.tab_text.text.delete('1.0', 'end')
        self.tab_text.text.insert('1.0', valeu)
        self.text.see('end')

        if self.refresh_enable:
            self.after(self.refresh_interv*1000, self.ext_refresh)

    def local_refresh(self):
        if self.tab_text.text == None: return
        filename = self.tab_text.saved_path
        if filename == "": return

        f = open(filename, 'r')
        valeu = f.read()
        self.tab_text.text.delete('1.0', 'end')
        self.tab_text.text.insert('1.0', valeu)
        f.close()
        self.text.see('end')

        if self.refresh_enable:
            self.after(self.refresh_interv*1000, self.local_refresh)
