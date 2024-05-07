import socket
import threading
from PyQt6.QtCore import pyqtSignal, QObject

class Client(QObject):
    messageReceived = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 65443))

        # Start a separate thread to run the receive method
        self.receive_thread = threading.Thread(target=self.receive)
        self.receive_thread.start()

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.messageReceived.emit(message)
            except:
                print("An error has occurred.")
                self.client.close()
                break

    def send_message(self, message):
        self.client.send(message.encode('utf-8'))
