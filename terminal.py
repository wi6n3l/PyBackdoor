import socket, time, os, platform

encrypted = list("b^$3k/I7h=gMnCe?«*HX#PqyuJRlDUSV_w6o>YmTK2'-|aL+9zrG<5s1\%OE48icQvdxp!AtNZB W»~jf&0F")
decrypted = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| ")

def encrypt(string):
    final = ""
    for i in list(string):
        n = decrypted.index(i)
        print(encrypted[n])
        final += encrypted[n]
    return final

def decrypt(string):
    final = ""
    for i in list(string):
        n = encrypted.index(i)
        final += decrypted[n]
    return final

global author_instagram
author_instagram = "tchewui"

class symbols():
    def __init__(self):
        self.defaults = "\033[39m"
        self.banners = "\033[36m"
        self.credits = "\033[34mmade by \033[31m@" + author_instagram+"\033[39m"
        self.sucesss = "\033[32m[+] "
        self.errors = "\033[31m[-] "
        self.warnings = "\033[33m[#] "
        self.infos = "\033[34m[!] "
        #if (platform.system() != "Linux"):##########debugging
        if(platform.system() != "Windows"):
            self.defaults = ""
            self.banners = ""
            self.credits = "made by @" + author_instagram
            self.sucesss = "[+] "
            self.errors = "[-] "
            self.warnings = "[#] "
            self.infos = "[!] "
    def default(self, text):
        return self.defaults + str(text)
    def banner(self, text):
        return self.banners + str(text)
    def credit(self):
        return self.credits
    def sucess(self, text):
        return self.sucesss + str(text) + "\033[39m"
    def error(self, text):
        return self.errors + str(text) + "\033[39m"
    def warning(self, text):
        return self.warnings + str(text) + "\033[39m"
    def info(self, text):
        return self.infos + str(text) + "\033[39m"

symbols = symbols()

print(symbols.default("###################################################################################\n" +
                      "###################################################################################\n" +
                      "##")+symbols.banner("||||||") + symbols.default("############") + symbols.banner("|||||") + symbols.default("##########################################################\n" +
                      "##" + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("############") + symbols.banner("||") + symbols.default("   ") + symbols.banner("|") + symbols.default("###") + symbols.banner("|||||") + symbols.default("###########") + symbols.banner("||") + symbols.default("#########") + symbols.banner("||") + symbols.default("#########################\n" +
                      "##") + symbols.banner("||||||") + symbols.default("#") + symbols.banner("\\\\") + symbols.default("  ") + symbols.banner("//") + symbols.default("#####") + symbols.banner("||||||") + symbols.default("####   ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||") + symbols.default(" ") + symbols.banner("//") + symbols.default("######") + symbols.banner("||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||") + symbols.default(" ") + symbols.banner("__") + symbols.default("##\n" +
                      "##") + symbols.banner("||") + symbols.default("######") + symbols.banner("\\\\//") + symbols.default("######") + symbols.banner("||") + symbols.default("   ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||") + symbols.default("    ##") + symbols.banner("||//") + symbols.default(" ##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||//") + symbols.default("###\n" +
                      "##") + symbols.banner("||") + symbols.default("#######") + symbols.banner("//") + symbols.default("#######") + symbols.banner("||") + symbols.default("    ") + symbols.banner("|") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||") + symbols.default("    ##") + symbols.banner("||\\\\") + symbols.default(" ##") + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner("||") + symbols.default("#####\n" +
                      "##") + symbols.banner("||") + symbols.default("######") + symbols.banner("//") + symbols.default("########") + symbols.banner("|||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||") + symbols.default(" ") + symbols.banner("\\\\") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner("||") + symbols.default("#####\n" +
                      "###################################################################################\n" +
                      "###################################################################################\n\n")) +
                      " "*(93-len(symbols.credit())) + symbols.credit())



def create_backdoor():
    print(symbols.info("in progress"))

def listen():
    try:
        #listen_port = int(input(symbols.default("Listening port : "))) ## to 65535 ###DEBUG### UNCOMMENT
        listen_port = 23125  ##DEBUG## COMENT
        if (listen_port > 0 and listen_port < 65535):
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("", listen_port))
            server.listen(1)
            conn, addr = server.accept()

            def send(string):
                conn.send(encrypt(string).encode("utf-8"))

            def recive(buffer):
                return decrypt(conn.recv(buffer).decode("utf-8"))

            condition = True

            while condition:
                id_msg = recive(1024)
                condition = False

            print(id_msg)
            if id_msg.startswith("231Py8ackd00r231"):
                send("200")
                condition = True
                while condition:
                    bff = recive(1024)
                    if bff.startswith("#"):
                        buffer = int(bff.split("#")[1])
                        condition_msg = True
                        while condition_msg:
                            msg = recive(buffer)
                            condition_msg = False
                    print(msg)
    except Exception as e:
        print(e)
        pass
        #server = socket.socket

    except KeyboardInterrupt:
        server.close()

def listen_multiple_sessions():
    print(symbols.info("in progress"))


def changeMenu():
    print("""        Menu 
1. Create Backdoor
2. Listen
3. Listen Multiple Sessions
""")
    menu = input()
    if(menu.isnumeric() and len(menu)== 1):
        current_menu = menu
    else:
        print(symbols.error("Invalid value, please try again:"))
        changeMenu()

    print(current_menu)

    if(current_menu == "1"):
        create_backdoor()
    elif(current_menu == "2"):
        listen()
    elif(current_menu == "3"):
        listen_multiple_sessions()
    else:
        print(symbols.error("Invalid option, please select a valid one:"))
        changeMenu()

#changeMenu() #DEBUG UNCOMMENT

listen()###### DEBUG # COMMENT ##########