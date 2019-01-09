import requests
import os
import sys

# Admim Finder WordList
# Create by ToxickWave
# Salve TDA TEAM

os.system("cls||clear")

print
print '\033[1;94m' + "\033[1;33m" + " Admin Finder Wordlist " + '\033[0;0m' + '\033[0;0m'
print '\033[1;94m' + "\033[1;33m" + "       TDA TEAM        " + '\033[0;0m' + '\033[0;0m'
print
print "\033[;1m" + "\033[1;36m" + "Usage: ruby.py https://www.site.com/ wordlist.txt " + '\033[0;0m'
print

if len(sys.argv) > 2:
    word = sys.argv[2]
    arq = open(word , 'r')
    lista = arq.readlines()
    for pay in lista:
        user = {'user-agent':'Opera/1.0 ( Windows 98  )'}
        site = sys.argv[1] + pay
        r = requests.get(site)
        if r.status_code == 200:
            print "\033[;1m" + "\033[1;92m" + "[+] ON: " + site + "\033[0;0m"
        else:
            if r.status_code != 200:
                print "\033[;1m" + "\033[1;91m" + "[!] OFF: " + site + "\033[0;0m"
