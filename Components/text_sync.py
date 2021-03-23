from datetime import datetime
from Components.scp_connect import ScpConnect
from Components.status_bar import StatusBar

class TextSync:

    def __init__(self, tab, combo, text):
        self.refresh_enable = False
        self.pause = False
        self.server = ""
        self.port = ""
        self.user = ""
        self.passwor = ""
        self.path = ""
        self.interv = 0
        self.tab = tab
        self.text = text
        self.combo = combo
        self.scp = ScpConnect()

    def syn_pause_enable(self):
        self.pause = True

    def syn_pause_disable(self):
        self.pause = False

    def syn_disable(self):
        self.refresh_enable = False
        self.server = ""
        self.port = ""
        self.user = ""
        self.passwor = ""
        self.path = ""
        self.interv = 0
        self.text.config(bg='#fff')
        self.scp.end_connection()

    def syn_local_enable(self, interv = 5):
        self.refresh_enable = True
        self.refresh_interv = int(interv)
        self.local_refresh()
        self.text.config(bg='#ededed')

    def syn_ext_enable(self, server, port, user, passwor, path, interv):
        self.refresh_enable = True
        self.server = server
        self.port = port
        self.user = user
        self.passwor = passwor
        self.path = path
        self.refresh_interv = int(interv)
        ret = self.scp.connect(self.tab.get_frame_id(), server, port, user, passwor)
        if(ret==True):
            self.ext_refresh()
            self.text.config(bg='#ededed')
        else:
            return False
        return True

    def ext_refresh(self):
        valeu = self.scp.get_text(self.path)
        if valeu == None:
            StatusBar().set("synced canceled: %s" %(datetime.now().strftime("%H:%M:%S")))
            return

        if self.text == None:
            StatusBar().set("synced canceled: %s" %(datetime.now().strftime("%H:%M:%S")))
            return

        if self.pause == False:
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', valeu)
            self.text.see('end')

        if self.refresh_enable:
            self.text.after(self.refresh_interv*1000, self.ext_refresh)
            if self.pause == False:
                StatusBar().set("synced: %s" %(datetime.now().strftime("%H:%M:%S")))

    def local_refresh(self):
        if self.text == None:
            StatusBar().set("synced canceled: %s" %(datetime.now().strftime("%H:%M:%S")))
            return
        filename = self.combo.saved_path
        if filename == "":
            StatusBar().set("synced canceled: %s" %(datetime.now().strftime("%H:%M:%S")))
            return

        if self.pause == False:
            f = open(filename, 'r')
            valeu = f.read()
            self.text.delete('1.0', 'end')
            self.text.insert('1.0', valeu)
            f.close()
            self.text.see('end')

        if self.refresh_enable:
            self.text.after(self.refresh_interv*1000, self.local_refresh)
            if self.pause == False:
                StatusBar().set("synced: %s" %(datetime.now().strftime("%H:%M:%S")))

    def reset_ext_buffer(self):
        self.scp.reset_ext_buffer(self.path)
