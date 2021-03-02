import os
from tkinter import messagebox
import datetime
import getpass
month = {"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May","6":"Jun","7":"Jul","8":"Aug","9":"Sep","10":"Oct","11":"Nov","12":"Dec"}
try:
    assert getpass.getuser() != "root"
except:
    print("this script is run by root! please do not use sudo command.")
    exit()
user = getpass.getuser()
td = "\""+month[str(int(str(datetime.date.today()).split("-")[1]))]+ " " +str(int(str(datetime.date.today()).split("-")[2]))+"\""
if len(td) == 7:
    td = td.replace(" ","  ")
yes ="\""+str(month[str(int(str(datetime.date.today()-datetime.timedelta(days=1)).split("-")[1]))]+" "+str(int(str(datetime.date.today()-datetime.timedelta(days=1)).split("-")[2])))+"\""
os.chdir("/Users/"+user)
if len(yes) == 7:
    yes = yes.replace(" ","  ")
print(td)
print(yes)
try:
    t = 0
    while True:
        f = open(file = "text"+str(t)+".txt",mode = "r")
        f.close()
        t += 1
except:
    targ = "text" + str(t)+".txt"
    f = open(file = targ,mode = "w",encoding = "UTF-8")
    f.close()
    targ_filelist = ["/Applications",""]
    kekka = []
    for u in targ_filelist:
        os.system("ls -l")
        print("ls -l "+u+" | grep "+td)
        os.system("ls -l "+u+" | grep "+td+" > "+targ)
        f = open(file=targ,mode="r",encoding="UTF-8")
        files = f.readlines()
        f.close()
        for x in range(0,len(files)):
            files[x] = files[x].rstrip().split(" ")
        for x in range(0,len(files)):
            for y in range(0,len(files[x])):
                if files[x][y] == yes.split(" ")[0]:
                    del files[x][:y+3]
                    break
            if len(files[x]) > 1:
                tmp = files[x][0]
                for z in range(1,len(files[x])):
                    tmp += " "+files[x][z]
                files[x] = tmp
            else:
                files[x] = files[x][0]
        for x in files:
            kekka.append(x)
        os.system("rm " + targ)
edited = []
print(kekka)
for x in kekka:
    temp = x.split(" ")
    t=0
    while t < len(temp):
        if temp[t] == "":
            del temp[t]
        else:
            t += 1
    for y in range(0,len(temp)-1):
        if "\""+temp[y]+" "+temp[y+1]+"\"" == yes or "\""+temp[y]+" "+temp[y+1]+"\"" == td:
            edited.append(temp[y+3:])
        elif "\""+temp[y]+"  "+temp[y+1]+"\"" == yes or "\""+temp[y]+"  "+temp[y+1]+"\"" == td:
            edited.append(temp[y+3:])
for x in range(0,len(edited)):
    unite = edited[x][0]
    for y in range(1,len(edited[x])):
        unite += " "+edited[x][y]
    edited[x] = unite
print(edited)
hdir=""
app=""
for x in edited:
    if os.system("stat /Users/"+user+"/\""+x+"\" > hakidasi.txt") == 0:
        hdir += " \"{}\"".format(x)
    if os.system("stat /Applications/\""+x+"\" > hakidasi.txt") == 0:
        app += " \"{}\"".format(x)
os.system("rm hakidasi.txt")
print(hdir)
print(app)
os.system("clamscan "+hdir+" --infected > result.txt")
os.chdir("/Applications")
os.system("clamscan "+app+" --infected > /Users/"+user+"/result2.txt")
os.chdir("/Users/"+user)
#  ----------リザルトの出力-----------------
files = []
for x in range(0,2):
    if x == 0:
        resultfiles = "/result.txt"
    elif x == 1:
        resultfiles = "/result2.txt"
    f = open(file="/Users/"+user+resultfiles,mode="r",encoding="UTF-8")
    pattern = f.readlines()
    f.close()
    for x in range(0,len(pattern)):
        if pattern[x].replace("\n","") == "----------- SCAN SUMMARY -----------":
            end = x
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
    messagebox.showwarning("Virus alert","Virus has detected!\n" + text)
