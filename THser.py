import subprocess
import threading
from _thread import start_new_thread
import socket 
import os

def threaded(c,addr):
	while True:
		data = c.recv(1024)
		cmd = subprocess.Popen(['arp',addr],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		stdout,stderr = cmd.communicate()
		arp = str(stdout)
		print(arp)

		data = data[::-1]
		if not data:
			print('Bye')
			break

		c.send(arp.encode('ascii'))
	c.close()

def main():
	host = ''
	port = 2213
	threads = []

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((host,port))
	s.listen(5)
	print("ACCEPTING CONN")

	while True:
		c,addr = s.accept()
		print("Connection established TO: ",addr[0])
		t = start_new_thread(threaded,(c,addr[0]),)
		threads.append(t)
	s.close()

	for t in threads:
		t.join()

if __name__ == '__main__':
	main()
