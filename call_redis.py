from sys import argv, exit
import time
import socket

BLOCK_LENGTH = 512


def connect(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    return s


def call_redis(host, port, command):
    s = connect(host, port)
    s.sendall(command.encode())
    data = s.recv(BLOCK_LENGTH)
    if data:
        print(repr(data))
    s.shutdown(socket.SHUT_WR)
    s.close()


if __name__ == "__main__":
    if len(argv) < 3:
        print("usage: call_redis host port command")
        exit(1)

    cmd = " ".join(argv[3:]) + "\r\n"
    print(cmd)
    call_redis(argv[1], argv[2], cmd)
