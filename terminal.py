import socket, time, os, platform

class symbols():
    sucess = "\033[32m[+] "
    error = "\033[31m[-] "
    warning = "\033[33m[#] "
    info = "\033[34m[!] "
    #if (platform.system() != "Linux"):##########debugging
    if(platform.system() == "Windows"):
        sucess = "[+] "
        error = "[-] "
        warning = "[#] "
        info = "[!] "

    def sucess(self, text):
        return self.sucess + str(text)
    def error(self, text):
        return self.error + str(text)
    def warning(self, text):
        return self.warning + str(text)
    def info(self, text):
        return self.info + str(text)
#print(color.green + "+")
#print(color.red + "-")
#print(color.blue + "!")

print("""
###################################################################################
###################################################################################
##||||||############|||||||########################################################
##||  ||############||   ||##|||||###########||#####    ||#########################
##||||||#\\\\  //#####|||||||###   ||##||||||##|| //##    ||##||||||##||||||##|| __##
##||######\\\\//######||   ||##||||||##||    ##||// ##||||||##||  ||##||  ||##||//-##
##||#######//#######||    ||#||  ||##||    ##||\\\\ ##||  ||##||  ||##||  ||##||   ##
##||######//########|||||||##||||||##||||||##|| \\\\##||||||##||||||##||||||##||   ##
###################################################################################
###################################################################################""")

def create_backdoor():
    print(symbols.info("in progress"))

def listen():
    print(symbols.info("in progress"))

def listen_multiple_sessions():
    print(symbols.info("in progress"))


def changeMenu():
    print("""
        Menu 
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