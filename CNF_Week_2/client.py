import socket
def main():
	host  = '10.10.8.254'
	port = 5200
	s = socket.socket()
	s.connect((host, port))
	msg = input('>>> ')
	count = 0
	while msg != 'q':
		s.send(msg.encode())
		data = s.recv(1024)
	    data = str(data.decode()).split()
	    if data[1] == 'ATTENDANCE FAILURE':
	    	serverdata = s.recv(1024)
	    	s.send(msg.encode())
	    elif data[1] == 'ATTENDANCE-SUCCESS':
	    	s.close()
	    	# serverdata = s.recv(1024)
	    	# s.send(msg.encode())

		print('received from server ' + str(data.decode()))
		msg = input(">>> ")
	s.close()
if __name__ == '__main__':
	main()
