import json
import zlib

class Messenger:

    def __init__(self, sock):
        self.sock = sock

    def send(self, data):
        self.sock.send(b"FHTP" + zlib.compress(json.dumps(data).encode()))

    def decode(self):

        data = self.sock.recv(1000000)
        data = zlib.decompress(data[4:]).decode()
        return data
