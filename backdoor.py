import socket, time, os

server = "192.168.1.103" ##### Change
port = 23125 #### Change

try:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.connect((server, port))
except:
    pass





server_connection.close()
