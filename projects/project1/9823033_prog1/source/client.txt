from socket import *
serverName = '127.0.0.1'
serverPort = 2121
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('welcome to the FTP client.')
print('call one of the following functions:')
print('HELP\t\t : show this help')
print('LIST\t\t : list files')
print('PWD\t\t : show current dir')
print('CD dir_name\t\t : change directory')
print('DWLD file_path\t\t : Download file')
print('QUIT\t\t : Exit')
while True:
    message = input("enter a command:")
    if message == "HELP":
        print('welcome to the FTP client.')
        print('call one of the following functions:')
        print('HELP\t\t : show this help')
        print('LIST\t\t : list files')
        print('PWD\t\t : show current dir')
        print('CD dir_name\t\t : change directory')
        print('DWLD file_path\t\t : Download file')
        print('QUIT\t\t : Exit')
        print('Enter a command:')
    if message == "LIST":
        clientSocket.send(message.encode())
        finalone = clientSocket.recv(1024)
        print("from TCP server: ", finalone.decode())
    if message == "PWD":
        clientSocket.send(message.encode())
        finaltwo = clientSocket.recv(1024)
        print("from TCP server: ", finaltwo.decode())
    if message[0] == "C":
        clientSocket.send(message.encode())
        finalthree = clientSocket.recv(1024)
        print("from TCP server: ", finalthree.decode())
    if message[0] == "D":
        clientSocket.send(message.encode())
        number = clientSocket.recv(1024).decode()
        z = int(number)
        if (z == 0):
            print("cannot find this file")
            continue
        else:
            print("created port :", z,  "\n")
            secondclientsocket = socket(AF_INET, SOCK_STREAM)
            secondclientsocket.connect((serverName, z))
            fp = open(message[5:], 'wb')
            secondmessage = secondclientsocket.recv(1024)
            while secondmessage:
                fp.write(secondmessage)
                secondmessage = secondclientsocket.recv(1024)
            fp.close()
            print("IT HAS BEEN DONE SUCCESFULLY")
    if message == "QUIT":
        break


clientSocket.close()


