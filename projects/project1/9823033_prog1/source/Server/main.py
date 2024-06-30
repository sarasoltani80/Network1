import random
from socket import *
import os
serverPort = 2121
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)
print('the server is ready to receive')
connectionSocket, addr = serverSocket.accept()
while True:
    Sentence = connectionSocket.recv(1024).decode()
    if Sentence == "PWD":
        location = os.getcwd()
        connectionSocket.send(location.encode())
    if Sentence == "LIST":
        listofdirectories = ''
        totalsize = 0
        for x in os.listdir():
            if os.path.isdir(x) == True:
                listofdirectories += ">" + x + "\n"
            if os.path.isfile(x) == True:
                listofdirectories += " " + x + "\n"
                totalsize += os.path.getsize(x)

        listofdirectories += ('total size of the directory : ' + str(totalsize) + ' ')
        connectionSocket.send(listofdirectories.encode())
    if Sentence[0] == "C":
        lastmessage = ''
        newdirectory = Sentence[3:]
        if(os.path.exists(newdirectory)):
            os.chdir(newdirectory)
            lastmessage += ('changing dir to : ' + newdirectory + ' ')
        connectionSocket.send(lastmessage.encode())
    if Sentence[0] == "D":
       if(os.path.exists(Sentence[5:])):
           print("DWLD is possible")
           myrandom = random.randint(3000, 50000)
           connectionSocket.send(str(myrandom).encode())
           print("porte ijadshode is: ", myrandom, "\n")
           secondserversocket = socket(AF_INET, SOCK_STREAM)
           secondserversocket.bind(('127.0.0.1', myrandom))
           secondserversocket.listen(2)
           secondconnectionserversocket, addr2 = secondserversocket.accept()
           fp = open(Sentence[5:], 'rb')
           secondconnectionserversocket.send(fp.read())
           secondconnectionserversocket.close()
       else:
        number = 0
        connectionSocket.send(str(number).encode())
