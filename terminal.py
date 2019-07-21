import socket, time, os, platform

global author_instagram
author_instagram = "tchewui"

class symbols():
    def __init__(self):
        self.defaults = "\033[37m"
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
        return self.sucesss + str(text)
    def error(self, text):
        return self.errors + str(text)
    def warning(self, text):
        return self.warnings + str(text)
    def info(self, text):
        return self.infos + str(text)

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
    print(symbols.info("in progress"))

def listen_multiple_sessions():
    print(symbols.info("in progress"))


def changeMenu():
    print("""        Menu 
1. Create Backdoor
2. Listen
3. Listen Multiple Sessions
""")
    menu = input()
    if(menu.isnumeric() and len(menu)==1):
        current_menu = menu
    else:
        print(symbols.error("Invalid value, please try again:"))
        changeMenu()

    if(current_menu == 1):
        create_backdoor()
    elif(current_menu == 2):
        listen()
    elif(current_menu == 3):
        listen_multiple_sessions()
    else:
        print(symbols.error("Invalid option, please select a valid one:"))
        changeMenu()

changeMenu()