with open("auth.log", "r") as f:
    logs = f.readlines()

sshLog = []
for x in logs:
    if 'sshd' in x:
        sshLog.append(x)

fullData = []

for x in sshLog:
    x = x.replace("  ", " ")
    pos = 0
    while True:
        Dfor = x.find("for ", pos)
        if Dfor == -1:
            break

        Auser =Dfor + 4
        Buser = x.find(" ", Auser)

        if Buser==-1:
            break
        
        if x[Auser:Buser] == "invalid":
            Auser = x.find("invalid user ") + 13
            Buser = x.find(" ", Auser)
            if Buser == -1:
                break   

        pos = Buser

        Dip = x.find("from ", pos)
        if Dip == -1:
            break
        Aip = Dip + 5
        Bip = x.find(" ", Aip)
        pos = Bip
        if Bip==-1:
            break


        Dport  = x.find("port ", pos)
        if Dport == -1:
            break
        Aport = Dport + 5
        Bport = x.find(" ", Aport)

        if Bport==-1:
            break
        
        los = 0

        # bln = x.find(' ', los)
        # tgl = x.find(' ', 4)
        # jm = x.find(' ', 7)


        data = {
            "bulan" : x.split()[0],
            "jam" : x.split()[1],
            "tanggal" : x.split()[2],
            "user" : x[Auser:Buser],
            "ip" : x[Aip:Bip],
            "port" : x[Aport:Bport]
        }

        fullData.append(data)


print(fullData)




