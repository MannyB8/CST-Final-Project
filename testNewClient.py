import socket
import threading

host = '127.0.0.1'
port = 65443

class Client:
    def __init__(self,host,port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))

        self.isRunning = True

        guiTLoop = threading.Thread(target=self.guiLoop)
        guiTRecieve = threading.Thread(target=self.guiRecieve)

        guiTLoop.start()
        guiTRecieve.start()

    def guiLoop(self):
        pass

    def messagefun(self):
        messages = f'{self.nickname}: {self.inputArea.get('start to end ')}'
        self.sock.send(messages.encode('utf-8'))
        self.inputArea.delete()

    def guiRecieve(self):
        while self.isRunning:
            try:
                message = self.sock.recv(1024)
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                else:
                    if self.gdone:
                        pass
                        # insert new text to the server here
                        # add the message at the end
            except ConnectionAbortedError:
                break
            except:
                print("Error has occured ")
                self.sock.close()
                break

client = Client(host, port)