#!/usr/bin/python3

import socket
import re

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('52.61.142.146', 31802))

    while True:
        data = ''

        oper = client.recv(1028)
        data = oper.decode('utf-8')
        snookie = ''
        print(oper) 
        if '\nright' in data:
            snookie = str('>').encode('utf-8') + b'\n'
            client.send(snookie)
        elif '\nleft' in data:
            snookie=str('<').encode('utf-8')+b'\n'
            client.send(snookie)
        elif '\nup' in data:
            snookie=str('^').encode('utf-8')+b'\n'
            client.send(snookie)
        elif '\ndown' in data:
            snookie=str('V').encode('utf-8')+b'\n'
            client.send(snookie)
        else: 
            data = client.recv(4096)
            break

    print (data)
