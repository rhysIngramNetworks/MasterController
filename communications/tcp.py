import socket


class TcpSocket:
    def __init__(self, address, port):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.address = address
        # addr and port that connects to the server
        self.client_socket = None
        self.client_port = None
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self):
        self.tcp_socket.bind((self.address, self.port))

    def listen(self, num_of_clients):
        self.tcp_socket.listen(num_of_clients)

    def accept(self):
        (self.client_socket, self.client_port) = self.tcp_socket.accept()

    def connect(self, addr, port):
        # addr and port you wish to connect to
        self.tcp_socket.connect((addr, port))
        self.client_socket = self.tcp_socket

    def sendall(self, msg):
        return self.client_socket.sendall(msg.encode("utf-8"))

    def sendbytes(self, msg):
        return self.client_socket.sendall(msg)

    def send(self, msg):
        return self.client_socket.send(msg)

    def recv(self):
        cmd = b""
        cmd_ = self.client_socket.recv(1)
        while cmd_ != b'\n':
            cmd += cmd_
            cmd_ = self.client_socket.recv(1)

        return cmd

    def recv_size(self, size):
        return self.client_socket.recv(size)

    def close(self):
        self.tcp_socket.close()

    def __del__(self):
        self.close()
