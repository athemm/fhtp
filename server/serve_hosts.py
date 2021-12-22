#!/usr/bin/env python3

import socket
import zlib
import threading
import urllib.request
import json
import os


def getPage(hostid,pageid):
    try:
        f = open(os.getcwd() + f"/hosts/{hostid}/{pageid}/index.html", "r").read()
        return f
    except Exception as e:
        print(e)
        return "<html><body><p>Code 404</p></body></html>"
    
