import socket


class UdpSocket:
    def __init__(self, address, port):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = port
        self.address = address

    def bind(self):
        self.udp_socket.bind((self.address, self.port))

    def recv_from(self, package_length):
        ret = -1, -1
        try:
            ret = self.udp_socket.recvfrom(package_length)
        except TimeoutError:
            ret = -1, -1
        return ret

    def set_blocking(self, is_blocking):
        self.udp_socket.setblocking(is_blocking)

    def send_to(self, msg, addr, port):
        self.udp_socket.sendto(msg, (addr, port))

    def settimeout(self, timeout):
        self.udp_socket.settimeout(timeout)

    def close(self):
        self.udp_socket.close()

    def __del__(self):
        self.close()
