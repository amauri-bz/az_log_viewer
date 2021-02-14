import importlib
paramiko_found = importlib.find_loader("paramiko")
scp_found = importlib.find_loader("scp")

if paramiko_found != None and scp_found != None:
	import os
	import paramiko
	from scp import SCPClient

	class ScpConnect:

		def __init__(self):
			pass

		def __exit__(self, exc_type, exc_value, traceback):
			self.ssh.close()
			self.scp_conn.close()
			os.remove("tmp/buffer.txt")

		def connect(self, server, port, user, passwor):
			self.ssh = self.createSSHClient(server, port, user, password)
			self.scp_conn = SCPClient(ssh.get_transport())
			f= open("tmp/buffer.txt","w+")
			f.close()

		def createSSHClient(self, server, port, user, password):
		    client = paramiko.SSHClient()
		    client.load_system_host_keys()
		    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		    client.connect(server, port, user, password)
		    return client

		def get_text(self, path):
			""" Gets a file from the remote server
			    Arguments:
			    - path: Source file in the remote server.
			"""
			self.scp_conn.get(path, "tmp/buffer.txt")
else:
	class ScpConnect:

		def __init__(self):
			pass

		def connect(self, server, port, user, passwor):
			print("Not supported")

		def get_text(self, path):
			print("Not supported")
