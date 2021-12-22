from Modals.Messenger import Messenger
import socket

class Zone:

    def __init__(self, addr):

        self.s = socket.socket()
        self.s.connect(addr)  # Established a connection!
        self.messenger = Messenger(self.s)

    def request_page(self, host_id, page_id):

        self.messenger.send({
            "action": "SERVE",
            "page-id": page_id,
            "host-id": host_id
        })

        return self.messenger.decode()

    def request_hostmap(self, host_id):

        self.messenger.send({
            "action": "MAP",
            "host-id": host_id
        })

        return self.messenger.decode()