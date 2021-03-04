import os
import sys
import datetime
from tkinter import messagebox
import getpass
checking = 1
cd = __file__
if checking == 0 and getpass.getuser() == "root":
    print("this script is run by root! please do not use sudo command.")
    exit()
if os.system("brew list") != 0:
    sys.stdout.write("Homebrew isn't installed on this system!Do you want to install?(Y/n):")
    while True:
        an = sys.stdin.readline()
        if an.lower() == "y" or an == "\n":
            if os.system("""/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"""") == 0:
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
            sys.stdout.\
                write("Python3 isn't installed on this system!Do you want to install python3 via Homebrew?(Y/n):")
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
            os.system("cp /usr/local/etc/clamav/freshclam.conf.sample freshclam.conf")
            os.system("cp /usr/local/etc/clamav/freshclam.conf.sample clamd.conf")
            f = open(file="/usr/local/etc/clamav/freshclam.conf.sample", mode="r", encoding="UTF-8")
            conf = f.readlines()
            f.close()
            conf[7] = "\n"
            f = open(file="freshclam.conf", mode="w", encoding="UTF-8")
            f.close()
            for x in conf:
                f = open(file="freshclam.conf", mode="a", encoding="UTF-8")
                f.write(x)
                f.close()
            os.system("sudo cp freshclam.conf /usr/local/etc/clamav")
            f = open(file="/usr/local/etc/clamav/clamd.conf.sample", mode="r", encoding="UTF-8")
            conf = f.readlines()
            f.close()
            conf[7] = "\n"
            conf[95] = "LocalSocket /usr/local/var/run/clamav/clamd.sock\n"
            conf[111] = "TCPSocket 3310"
            conf[119] = "TCPAddr 127.0.0.1"
            f = open(file="clamd.conf", mode="w", encoding="UTF-8")
            f.close()
            for x in conf:
                f = open(file="clamd.conf", mode="a", encoding="UTF-8")
                f.write(x)
                f.close()
            os.system("sudo cp clamd.conf /usr/local/etc/clamav")
            os.system("freshclam -v")
            print("Success!")
        else:
            print("ClamAV can't be installed!")
    else:
        print("abort.")
        exit()
for x in range(0, len(checker)):
    if checker[x] == "checking = 0\n":
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
        break
Base = __file__.split("/")
now=""
for x in range(0, len(Base)-1):
	now += "/"+Base[x]
if Base[-2] != ".AV_DONOTREMOVE":
    now += "/.AV_DONOTREMOVE"
f = open(file=now+"/user.txt", mode="r", encoding="UTF-8")
user = f.readline()
f.close()
td = "\""+str(int(str(datetime.date.today()).split("-")[1])) + " " +str(int(str(datetime.date.today()).split("-")[2]))+"\""
if td[-3] == " ":
    td = td.replace(" ", "  ")
yes = "\""+str(int(str(datetime.date.today()-datetime.timedelta(days=1)).split("-")[1]))+ " "+str(int(str(datetime.date.today()-datetime.timedelta(days=1)).split("-")[2]))+ "\""
os.chdir("/Users/"+user)
if yes[-3] == " ":
    yes = yes.replace(" ", "  ")
print(td)
print(yes)
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
    targ_filelist = ["/Applications", ""]
    kekka = []
    for u in targ_filelist:
        os.system("ls -l")
        os.system("ls -l "+u+" | grep "+td+" > "+targ)
        f = open(file=targ, mode="r", encoding="UTF-8")
        files = f.readlines()
        f.close()
        for x in range(0, len(files)):
            # noinspection PyTypeChecker
            files[x] = files[x].rstrip().split(" ")
        for x in range(0, len(files)):
            for y in range(0, len(files[x])):
                if files[x][y] == yes.split(" ")[0]:
                    del files[x][:y+3]
                    break
            if len(files[x]) > 1:
                tmp = files[x][0]
                for z in range(1, len(files[x])):
                    tmp += " "+files[x][z]
                files[x] = tmp
            else:
                files[x] = files[x][0]
        for x in files:
            kekka.append(x)
        os.system("rm " + targ)
edited = []
for x in kekka:
    temp = x.split(" ")
    t = 0
    while t < len(temp):
        if temp[t] == "":
            del temp[t]
        else:
            t += 1
    for y in range(0, len(temp)-1):
        if "\""+temp[y]+" "+temp[y+1]+"\"" == yes or "\""+temp[y]+" "+temp[y+1]+"\"" == td:
            edited.append(temp[y+3:])
        elif "\""+temp[y]+"  "+temp[y+1]+"\"" == yes or "\""+temp[y]+"  "+temp[y+1]+"\"" == td:
            edited.append(temp[y+3:])
for x in range(0, len(edited)):
    unite = edited[x][0]
    for y in range(1, len(edited[x])):
        unite += " "+edited[x][y]
    edited[x] = unite
print(edited)
hdir = ""
app = ""
for x in edited:
    if os.system("stat /Users/"+user+"/\""+x+"\"") == 0:
        hdir += " \"{}\"".format(x)
    if os.system("stat /Applications/\""+x+"\"") == 0:
        app += " \"{}\"".format(x)
#os.system("freshclam ClamAV update")
os.system("clamscan "+hdir+" --infected > result.txt")
os.chdir("/Applications")
os.system("clamscan "+app+" --infected > /Users/"+user+"/result2.txt")
os.chdir("/Users/"+user)
print(hdir)
print(app)
files = []
resultfiles = ""
for x in range(0, 2):
    if x == 0:
        resultfiles = "/result.txt"
    elif x == 1:
        resultfiles = "/result2.txt"
    f = open(file="/Users/"+user+resultfiles, mode="r", encoding="UTF-8")
    pattern = f.readlines()
    f.close()
    end = 0
    for t in range(0, len(pattern)):
        if pattern[t].replace("\n", "") == "----------- SCAN SUMMARY -----------":
            end = t
            break
        else:
            pass
    del pattern[end - 1:]
    print(pattern)
    for y in pattern:
        files.append(y)
if len(files) >= 1:
    text = ""
    for x in files:
        text += x
    messagebox.showwarning("Virus alert", "Virus has been detected!\n" + text)
