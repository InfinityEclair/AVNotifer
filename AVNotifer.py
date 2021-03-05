import os
import sys
import datetime
from tkinter import messagebox
import getpass
checking = 1
if checking == 0 and getpass.getuser() == "root":
    print("this script is run by root! please do not use sudo command.")
    exit()
if os.system("brew list") != 0:
    sys.stdout.write("Homebrew isn't installed on this system!Do you want to install?(Y/n):")
    while True:
        an = sys.stdin.readline()
        if an.lower() == "y" or an == "\n":
            if os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"") == 0:
                print("Success!")
                break
            else:
                print("""Brew can't be installed!Please check 
                if you run python on Rosetta2 if you use an Apple Silicon Mac!""")
                exit()
        else:
            print("abort.")
            exit()
if sys.version_info.major == 2:
    print("This script is running on python 2.x!Please use python 3.x!")
    if os.system("python3 --version") != 0:
        while True:
            sys.stdout.write("Python3 isn't installed on this system!Do you want to install python3 via Homebrew?(Y/n):")
            a = sys.stdin.readline()
            if a.lower() == "y" or a.lower() == "n" or a == "":
                break
        if a.lower() == "y" or a == "":
            if os.system("brew install python@3.9") == 0:
                print("success!please re-run on python 3!")
            else:
                print("Python3 can't be installed!")
        else:
            print("abort.")
        exit()
    else:
        print("abort.")
        exit()
f = open(file=__file__, encoding="UTF-8", mode="r")
checker = f.readlines()
f.close()
if os.system("clamscan --version") != 0:
    while True:
        an = input("clamAV hasn't been installed! Do you want to install via Homebrew?(Y/n):")
        if an.lower() == "y" or an.lower() == "n" or an == "":
            break
    if an.lower() == "y" or an == "":
        if os.system("brew install clamAV") == 0:
            f = open(file="/usr/local/etc/clamav/freshclam.conf.sample", mode="r", encoding="UTF-8")
            conf = f.readlines()
            f.close()
            conf[7] = "\n"
            f = open(file="freshclam.conf", mode="w", encoding="UTF-8")
            for x in conf:
                f.write(x)
            f.close()
            os.system("sudo cp freshclam.conf /usr/local/etc/clamav")
            f = open(file="/usr/local/etc/clamav/clamd.conf.sample", mode="r", encoding="UTF-8")
            conf = f.readlines()
            f.close()
            conf[7] = "\n"
            conf[95] = "LocalSocket /usr/local/var/run/clamav/clamd.sock\n"
            conf[111] = "TCPSocket 3310\n"
            conf[119] = "TCPAddr 127.0.0.1\n"
            f = open(file="clamd.conf", mode="w", encoding="UTF-8")
            for x in conf:
                f.write(x)
            f.close()
            os.system("sudo cp clamd.conf /usr/local/etc/clamav")
            os.system("freshclam -v")
            print("Success!")
        else:
            print("ClamAV can't be installed!")
            exit()
    else:
        print("abort.")
        exit()
if checking == 0:
    while True:
        sel = input("You can set this script when you log in this account.Do you want to?(y/N):")
        if sel.lower() == "" or sel.lower() == "y" or sel.lower() == "n":
            break
    if sel.lower() == "y":
        tmp = __file__.split("/")
        cd = ""
        for t in range(0, len(tmp)-1):
            cd += "/"+tmp[t]
        os.chdir(cd)
        f = open("AVNotiferstarter.command", mode="w", encoding="UTF-8")
        f.write("#! /bin/zsh\n")
        f.write("python3 "+cd[1:]+"/AVNotifer.py\n")
        f.close()
        os.system("chmod u+x AVNotiferstarter.command")
        os.system("open -a /System/Applications/System\ Preferences.app")
        messagebox.showwarning("setting required","Please set AVNotiferstarter.command by going User and Group -> Login activity.")
    checker[x] = "checking = 1\n"
    f = open(file=__file__, mode="w", encoding="UTF-8")
    f.close()
    for y in range(0, len(checker)):
        f = open(file=__file__, mode="a", encoding="UTF-8")
        f.write(checker[y])
        f.close()
user = getpass.getuser()
td = "\""+str(int(str(datetime.date.today()).split("-")[1])) + " " +str(int(str(datetime.date.today()).split("-")[2]))+"\""
atd = td.replace("\"", "")
if td[-3] == " ":
    td = td.replace(" ", "  ")
yes = "\""+str(int(str(datetime.date.today()-datetime.timedelta(days=1)).split("-")[1]))+ " "+str(int(str(datetime.date.today()-datetime.timedelta(days=1)).split("-")[2]))+ "\""
os.chdir("/Users/"+user)
ayes = yes.replace("\"", "")
if yes[-3] == " ":
    yes = yes.replace(" ", "  ")
t = 0
try:
    while True:
        f = open(file="text"+str(t)+".txt", mode="r")
        f.close()
        t += 1
except FileNotFoundError:
    targ = "text" + str(t)+".txt"
    f = open(file=targ, mode="w", encoding="UTF-8")
    f.close()
    targ_filelist = ["/Applications", "/Users/"+user]
    kekka = {}
    for u in targ_filelist:
        os.system("ls -l")
        os.system("(ls -l "+u+" | grep "+td+" && ls -l"+u+" | grep"+yes+") > "+targ)
        f = open(file=targ, mode="r", encoding="UTF-8")
        files = f.readlines()
        f.close()
        for x in range(0, len(files)):
            files[x] = files[x].rstrip().split(" ")
        for s in range(0,len(files)):
            k = 0
            while k < len(files[s]):
                if files[s][k] == "":
                    del files[s][k]
                else:
                    k += 1
        for x in range(0, len(files)):
            for y in range(0, len(files[x])):
                if files[x][y] == atd.split(" ")[0] and files[x][y+1] == atd.split(" ")[1]:
                    del files[x][:y+3]
                    break
                elif files[x][y] == ayes.split(" ")[0] and files[x][y+1] == ayes.split(" ")[1]:
                    del files[x][:y+3]
                    break
            if len(files[x]) > 1:
                tmp = files[x][0]
                for z in range(1, len(files[x])):
                    tmp += " "+files[x][z]
                files[x] = tmp
            else:
                files[x] = files[x][0]
        kekka[u] = ""
        for x in files:
            kekka[u] += " \""+x+"\""
os.system("freshclam ClamAV update")
infected_files = []
for x in kekka:
    os.chdir(x)
    os.system("clamscan "+kekka[x]+" --infected > "+"/Users/"+user+"/result.txt")
    f = open(file="/Users/"+user+"/result.txt", mode="r", encoding="UTF-8")
    pattern = f.readlines()
    f.close()
    for h in range(0, len(pattern)):
        if pattern[h].replace("\n", "") == "----------- SCAN SUMMARY -----------":
            end = h
            break
    del pattern[end - 1:]
    for y in pattern:
        infected_files.append(y)
if len(infected_files) >= 1:
    text = ""
    for x in infected_files:
        text += x
    messagebox.showwarning("Virus alert", "Virus has been detected!\n" + text)
os.system("rm "+targ)
