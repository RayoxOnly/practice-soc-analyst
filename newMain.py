with open("auth.log", "r") as f:
    logs = f.readlines()

sshLog = []
for x in logs:
    if 'sshd' in x:
        sshLog.append(x)

# print(sshLog[0][0])

data = {
  "bulan", "tanggal", "jam", "user", "ip", "port", "status"
}

# for x in range(len(sshLog)):
time = []
print
# for x in range(len(sshLog)):
    # print(sshLog[x])
    # time.append(list(filter(None, sshLog[x].split())))
    
    # print(sshLog[x])
    # data["bulan"] = time[0]
    # print(time[0][0])

# print(data)

for x in sshLog:
    x = x.replace("  ", " ")
    x = x.split()
   

for x in sshLog:
    pos = 0
    while True:
        Dfor = x.find("for ", pos)
        Dip = x.find("from ", pos)
        Dport  = x.find("port ", pos)

        if Dfor == -1:
            break
        if Dip == -1:
            break
        if Dport == -1:
            break

        Auser =Dfor + 4
        Buser = x.find(" ", Auser)

        Aip = Dip + 5
        Bip = x.find(" ", Aip)

        Aport = Dport + 5
        Bport = x.find(" ", Aport)

        if Buser==-1:
            break
        if Bip==-1:
            break
        if Bport==-1:
            break

        pos = Bip

        print(x[Auser:Buser])
        print(x[Aip:Bip])
        print(x[Aport:Bport])

