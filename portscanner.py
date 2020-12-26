import socket
import termcolor


def scan(target, ports):
    print(termcolor.colored('\n' +  " Scanning the following IP: " + str(target), 'blue'))
    for port in range(1, ports):
        scan_port(target, port)


def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)

else:
    scan(targets.strip(' '), ports)
