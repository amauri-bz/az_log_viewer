import importlib
paramiko_found = importlib.find_loader("paramiko")
scp_found = importlib.find_loader("scp")

if paramiko_found != None and scp_found != None:
	import os
	import paramiko
	from scp import SCPClient
	from Components.status_bar import StatusBar

	class ScpConnect:

		def __init__(self):
			pass

		def __exit__(self, exc_type, exc_value, traceback):
			self.end_connection()

		def end_connection(self):
			self.ssh.close()
			self.scp_conn.close()
			os.remove(self.buffer_file)

		def connect(self, tab_id, server, port, user, password):
			try:
				self.buffer_file = "buffer"+tab_id+".txt"
				self.ssh = self.createSSHClient(server, port, user, password)
				self.scp_conn = SCPClient(self.ssh.get_transport())
				f= open(self.buffer_file,"w+")
				f.close()
				return True
			except:
				StatusBar().set("aborted - external connection error")
				return False

		def createSSHClient(self, server, port, user, password):
		    client = paramiko.SSHClient()
		    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		    client.connect(server, username=user, password=password, timeout=5)
		    return client

		def get_text(self, path):
			""" Gets a file from the remote server
			    Arguments:
			    - path: Source file in the remote server.
			"""
			try:
				self.scp_conn.get(path, self.buffer_file)
				f = open(self.buffer_file, 'r')
				f2 = f.read()
				f.close()
				return f2
			except:
				StatusBar().set("aborted - invalid path: %s" %(path))
				return "invalid path: %s" %(path)
		
		def reset_ext_buffer(self, path):
			self.ssh.exec_command('echo "" > ' + path)
else:
	class ScpConnect:

		def __init__(self):
			pass

		def connect(self, server, port, user, passwor):
			StatusBar().set("external sync- ssh and scp libs not intalled")

		def get_text(self, path):
			StatusBar().set("external sync - ssh and scp libs not intalled")
