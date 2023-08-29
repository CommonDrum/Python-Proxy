import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def start(self):
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")
            self.handle_client(client_socket)
            client_socket.close()
            print(f"Connection with {client_address} closed")

    def handle_client(self, client_socket):
        data = client_socket.recv(1024)
        while data:
            print(f"Received: {data}")
            client_socket.send(data)  # Echoing data back to client
            data = client_socket.recv(1024)


if __name__ == "__main__":
    server = Server("localhost", 8080)
    server.start()
