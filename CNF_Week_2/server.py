import socket
import threading
import random
from _thread import *
dict = {20158501:['What is my first vehicle first number?',501], 20158502:['What is my masters degree?','MSIT'],20158503:['Who is my close friend?','Sriram'],
20158504:['When did you meet your close friend?','1999'],20158505:["What’s your mother's maiden name?",'John'],20158506:['Who invented telephone?','Graham Bell'],
20158507:['Who invented radium?,Madam Curie'],20158508:['Which country is called as land of rising sun?','Japan'],20158509:['Which country is called of white elephants?','Thailand'],
20158510:['Gateway of India?','Mumbai']}
# def serverthread(inp_list):
def main():
    host = '127.0.0.1'
    port  = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen(10)
    print('socket is ready')
    # inp_list = []
    while True:
        conn, addr = s.accept()
        data = s.recv(1024)
        data = data.decode().split()
        if data[0] == 'MARK-ATTENDANCE':
            if data[1] not in dict:
                print("ROLLNUMBER-NOTFOUND")
            else:
                print(dict[data[0]][0])
                clientdata = s.recv(1024)
                if clientdata == dict[data[0]][0]:
                    s.send("ATTENDANCE SUCCESS").encode()
                else:
                    s.send("ATTENDANCE FAILURE").encode()
                    s.send(dict[data[0]][0]).encode()
                    s.recv(1024)
    s.close()
    # a = input().split()
    # inp_list.append(a)
# t1 = threading.Thread(target = serverthread, args=(inp_list, ))
    # print('connected from  ' + str(addr))
    # connections.append(conn)
    # start_new_thread(clientthread, (conn, addr,connections,players))

if __name__ == '__main__':
    main()



