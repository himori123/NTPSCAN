import os
from huepy import *

print(cyan("""

███    ██ ████████ ██████  ███████  ██████  █████  ███    ██ 
████   ██    ██    ██   ██ ██      ██      ██   ██ ████   ██ 
██ ██  ██    ██    ██████  ███████ ██      ███████ ██ ██  ██ 
██  ██ ██    ██    ██           ██ ██      ██   ██ ██  ██ ██ 
██   ████    ██    ██      ███████  ██████ ██   ██ ██   ████ 
            

    "NTPSCAN is a tool for scanning NTP servers to identify vulnerabilities and 
                Inappropriate settings that can be exploited
                 by attackers in NTP amplification attacks"

"""))
ntp_question = input("Enter the IP you want to search for: ")
one_system = os.popen(f"ntpq -c readlist {ntp_question}").read()
two_system = os.popen(f"ntpq -c readvar {ntp_question}").read()
three_system = os.popen(f"ntpq -c peers {ntp_question}").read()
four_system = os.popen(f"ntpq -c associations {ntp_question}").read()
five_system = os.popen(f"ntpdc -c monlist {ntp_question}").read()
six_system = os.popen(f"ntpdc -c listpeers {ntp_question}").read()
seven_system = os.popen(f"ntpdc -c sysinfo {ntp_question}").read()
eight_system = os.popen(f"ntpdc -n -c monlist {ntp_question}").read()
nine_system = os.popen(f"nmap -sU -pU:123 -Pn -n --script=ntp-monlist {ntp_question}").read()
then_system = os.popen(f"nmap -sU -p 123 --script ntp-info {ntp_question}").read()


print(purple("Command Output ntpq -c readlist:"))
print(one_system)

print(green("Command Output ntpq -c readvar:"))
print(two_system)

print(yellow("Saída do comando ntpq -c peers:"))
print(three_system)

print(red("Command Output ntpq -c associations:"))
print(four_system)

print(cyan("Command Output ntpdc -c monlist:"))
print(five_system)

print(blue("Command Output ntpdc -c listpeers:"))
print(six_system)

print(lightpurple("Command Output ntpdc -c sysinfo:"))
print(seven_system)

print(yellow("Command Output -n -c monlist"))
print(eight_system)

print(red("Command Output : nmap -sU -pU:123 -Pn -n --script=ntp-monlist"))
print(nine_system)

print(green("Command Output : nmap -sU -p 123 --script ntp-info"))
print(then_system)

print(bold("APÓS A EXECUSÃO DESTE SCRIPT, VOCÊ PODE USAR O METASPLOIT PARA EXPLORAR"))
