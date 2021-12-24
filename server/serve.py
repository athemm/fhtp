#!/usr/bin/env python3

from serve_hosts import *


def client(conn):
    while True:
        try:
            data = conn.recv(510213)
            print(data)
            if data[:4] != b"FHTP":
                break
            data = json.loads(zlib.decompress(data[4:]))

            try:
                data["host-id"]
            except:
                resp = "<html><body><p>Please insert host</p></body></html>"
            if data["action"].upper() == "MAP":
                if ".." in data["host-id"]:
                    resp = "<html><body><p>no</p></body></html>"
                else:

                    resp = "<html><body><p>" + "<br>".join(map_host(data["host-id"])) + "</p></body></html>"

            if data["action"].upper() == "SERVE":

                if ".." in data["page-id"] or ".." in data["host-id"]:
                    resp = "<html><body><p>no</p></body></html>"
                else:
                    resp = getPage(data["host-id"], data["page-id"])


            conn.send(b"FHTP" + zlib.compress(resp.encode()))
            print(resp)
        except Exception as e:
            print("client gone", e)
            break


HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 42031  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    threading.Thread(target=client, args=[conn]).start()
