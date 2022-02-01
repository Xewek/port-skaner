
import sys

import pyfiglet
from colorama import Fore
import socket

baner = pyfiglet.figlet_format("SKANER    PORTOW")

print(Fore.GREEN, baner)

host = input(Fore.YELLOW+"Podaj ip/host: ")
hostip = socket.gethostbyname(host)

"""if len(sys.argv) == 2:
    # host na IPv4
    host = socket.gethostname(sys.argv[1])
else:
    print("nieprawidłowa liczba!")

print("*"*50)
print("Skanowanie: " + host)
print("Skanowanie rozpoczęto: "+str(datetime.datetime.now()))
print("*"*50)

try:
    for port in range(1,900000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #erroro
        er = s.connect_ex((host,port))
        if er ==0:
            print(f"{host}:{port} jest {Fore.BLUE}OTWARTY!{Fore.GREEN}")
        s.close()"""
try:
    for port in range(1, 900000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        wynki = s.connect_ex((hostip, port))

        if port == 1:
            print(Fore.GREEN+"\n\n\nRozpoczynam skanowanie...")
        if port == 21:
            print(Fore.GREEN+f"\nSkanowanie{Fore.BLUE} FTP{Fore.GREEN}  -przesyłanie oraz pobieranie plików i folderów")
        if port == 22:
            print(f"\nSkanowanie {Fore.BLUE}SSH{Fore.GREEN}")
        if port == 23:
            print(f"\nSkanowanie {Fore.BLUE}TELNET{Fore.GREEN}")
        if port == 25:
            print(f"\nSkanowanie {Fore.BLUE}SMTP{Fore.GREEN}")
        if port == 53:
            print(f"\nSkanowanie {Fore.BLUE}DNS{Fore.GREEN}")
        if port == 69:
            print(f"\nSkanowanie {Fore.BLUE}TFTP{Fore.GREEN}")
        if port == 80:
            print(f"\nSkanowanie {Fore.BLUE}HTTP{Fore.GREEN}")
        if port == 109:
            print(f"\nSkanowanie {Fore.BLUE}POP2{Fore.GREEN}")
        if port == 110:
            print(f"\nSkanowanie {Fore.BLUE}POP3{Fore.GREEN}")
        if port == 123:
            print(f"\nSkanowanie {Fore.BLUE}NTP{Fore.GREEN}")
        if port == 137:
            print(f"\nSkanowanie {Fore.BLUE}NETBIOS-NS{Fore.GREEN}")
        if port == 138:
            print(f"\nSkanowanie {Fore.BLUE}NETBIOS-DGM{Fore.GREEN}")
        if port == 139:
            print(f"\nSkanowanie {Fore.BLUE}NETBIOS-SSN{Fore.GREEN}")
        if port == 143:
            print(f"\nSkanowanie {Fore.BLUE}IMAP{Fore.GREEN}")
        if port == 156:
            print(f"\nSkanowanie {Fore.BLUE}SQL-SERVER{Fore.GREEN}")
        if port == 389:
            print(f"\nSkanowanie {Fore.BLUE}LDAP{Fore.GREEN}")
        if port == 443:
            print(f"\nSkanowanie {Fore.BLUE}HTTPS{Fore.GREEN}")
        if port == 465:
            print(f"\nSkanowanie {Fore.BLUE}smtps{Fore.GREEN}")
        if port == 546:
            print(f"\nSkanowanie {Fore.BLUE}DHCP-CLIENT{Fore.GREEN}")
        if port == 547:
            print(f"\nSkanowanie {Fore.BLUE}DHCP-CLIENT{Fore.GREEN}")
        if port == 995:
            print(f"\nSkanowanie {Fore.BLUE}POP3-SSL{Fore.GREEN}")
        if port == 993:
            print(f"\nSkanowanie {Fore.BLUE}IMAP-SSL{Fore.GREEN}")
        if port == 2086:
            print(f"\nSkanowanie {Fore.BLUE}WHM/CPANEL{Fore.GREEN}")
        if port == 2083:
            print(f"\nSkanowanie {Fore.BLUE}CPANEL{Fore.GREEN}")
        if port == 3306:
            print(f"\nSkanowanie {Fore.BLUE}MYSQL{Fore.GREEN}")
        if port == 8443:
            print(f"\nSkanowanie {Fore.BLUE}PLESK{Fore.GREEN}")
        if port == 10000:
            print(f"\nSkanowanie {Fore.BLUE}VIRTUALMIN/WEBMIN{Fore.GREEN}")
        if port == 5222:
            print(f"\nSkanowanie {Fore.BLUE}XMPP {Fore.GREEN}– dla serwera sieci Jabber")
        if port == 5432:
            print(f"\nSkanowanie {Fore.BLUE}PostgreSQL {Fore.GREEN}")

        if wynki == 0:
            print(f"{Fore.GREEN}{hostip}:{port} Jest {Fore.BLUE}Otwarty")
        s.close()




except KeyboardInterrupt:
    print(Fore.YELLOW+"\n\n\nProgram wyłączony")
    sys.exit()
except socket.gaierror:
    print(Fore.RED+"\n\n\nBłędna nazwa hosta")
    sys.exit()
except socket.error:
    print(Fore.RED+"\n\n\nServer nie odpowiada")
    sys.exit()

