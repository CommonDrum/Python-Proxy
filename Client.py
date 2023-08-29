import socket

class Client:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.server_host, self.server_port))
        print(f"Connected to {self.server_host}:{self.server_port}")

    def send_receive(self, message):
        self.client_socket.send(message.encode())
        response = self.client_socket.recv(1024)
        print(f"Received: {response.decode()}")

    def close(self):
        self.client_socket.close()


if __name__ == "__main__":
    client = Client("localhost", 8080)
    client.connect()
    client.send_receive("Hello World!")
    client.close()