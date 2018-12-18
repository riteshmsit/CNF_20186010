import socket
def main():
	host = '127.0.0.1'
	port = 5095
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
		data, addr = s.recvfrom(1024)
		print('message from: ' + str(addr))
		print('from user: ' + data.decode())
		data = str(data.decode()).upper()
		print('sending: ' + data)
		s.sendto(data.encode(), addr)
	s.close()
if __name__ == '__main__':
	main()