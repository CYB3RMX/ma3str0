#!/usr/bin/env python
import os,hashlib
disp='''
     ___  ___  ___   _____  _____ ___________ _____
     |  \/  | / _ \ |____ |/  ___|_   _| ___ \  _  |
     | .  . |/ /_\ \    / /\ `--.  | | | |_/ / |/' |
     | |\/| ||  _  |    \ \ `--. \ | | |    /|  /| |
     | |  | || | | |.___/ //\__/ / | | | |\ \| |_/ /
     \_|  |_/\_| |_/\____/ \____/  \_/ \_| \_|\___/

                  |>>HASH CRACK TOOL<<|
                    |>>By CYB3RMX_<<|

    |>>MENU<<|
    [1] MD5 DECRYPT
    [2] SHA256 DECRYPT
    [3] SHA512 DECRYPT

'''
os.system('clear')
print(disp)
select=int(input("[+] CHOOSE: "))
if select==1:
  mess_md5=str(input("[+] ENTER YOUR MD5 HASH: "))
  print("[!] CRACK STARTS PLEASE BE PATIENT...")
  wordlist=open('hashlist.txt','r').read().split('\n')
  for m in wordlist:
     out=hashlib.md5(m.encode('utf-8')).hexdigest()
     if out==mess_md5:
       print(" ")
       print("[*] YOUR PASSWORD: \u001b[92m"+m)
       break
elif select==2:
  mess_sha256=str(input("[+] ENTER YOUR SHA256 HASH: "))
  print("[!] CRACK STARTS PLEASE BE PATIENT...")
  wordlist=open('hashlist.txt','r').read().split('\n')
  for m in wordlist:
     out=hashlib.sha256(m.encode('utf-8')).hexdigest()
     if out==mess_sha256:
       print(" ")
       print("[*] YOUR PASSWORD: \u001b[92m"+m)
       break
elif select==3:
  mess_sha512=str(input("[+] ENTER YOUR SHA512 HASH: "))
  print("[!] CRACK STARTS PLEASE BE PATIENT...")
  wordlist=open('hashlist.txt','r').read().split('\n')
  for m in wordlist:
     out=hashlib.sha512(m.encode('utf-8')).hexdigest()
     if out==mess_sha512:
       print(" ")
       print("[*] YOUR PASSWORD: \u001b[92m"+m)
       break
else:
  print("\u001b[91m[!] WRONG OPTION...")
