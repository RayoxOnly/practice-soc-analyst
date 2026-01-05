with open("auth.log", "r") as f:
    logs = f.readlines()
sshLog = []
for x in logs:
    x = x.strip()
    if "sshd" in x:
        sshLog.append(x)

#INTI
berhasil = []
gagal = []
invalid = []

#MENGELOMPOKAN
for x in sshLog:
    if "Accepted password" in x:
        berhasil.append(x)
    if "Failed password for" in x:
        if "invalid" not in x:
            gagal.append(x)
    if "Failed password for invalid" in x:
        invalid.append(x)


#USER_DATA
def data(bulan, tanggal, jam, user, ip, port):
    return{
        "bulan" : bulan,
        "tanggal" : tanggal,
        "jam" : jam,
        "user" : user,
        "ip" : ip,
        "port" : port
    }

newBulanAcc = []
newTanggalAcc = []
newJamAcc = []

newBulanFai = []
newTanggalFai = []
newJamFai = []

newJamInv = []
newBulanInv = []
newTanggalInv = []


def time(inti, bulan, tanggal, jam):
    sample = []
    for y in range(len(inti)):
        sample.append(list(filter(None, inti[y].split())))
    for x in sample:
        bulan.append(x[0])
        tanggal.append(x[1])
        jam.append(x[2])

    return bulan, tanggal, jam

time(berhasil, newBulanAcc, newTanggalAcc, newJamAcc)
time(gagal, newBulanFai, newTanggalFai, newJamFai)
time(invalid, newBulanInv, newTanggalInv, newJamInv )

def dataData(inti,newUserList, newIpList, newPortList):
    for x in inti:
        pos = 0
        while True:
            user = x.find('for ', pos)
            ip = x.find('from ', pos)
            port = x.find('port ', pos)

            if user == -1:
                break
        

            awalID = user + 4
            akhirID = x.find(' ', awalID)

            awalIP = ip + 5
            akhirIP = x.find(' ', awalIP)

            awalPort = port + 5
            akhirPort = x.find(" ", awalPort)

        
            if akhirID == -1:
                break
            
            newUserList.append(x[awalID:akhirID])
            newIpList.append(x[awalIP:akhirIP])
            newPortList.append(x[awalPort:akhirPort])
            pos = akhirID + 1

    return user, ip, port


def datainv(inti,newUserList, newIpList, newPortList):
    for x in inti:
        pos = 0
        while True:
            user = x.find('user ', pos)
            ip = x.find('from ', pos)
            port = x.find('port ', pos)

            if user == -1:
                break
        

            awalID = user + 5
            akhirID = x.find(' ', awalID)

            awalIP = ip + 5
            akhirIP = x.find(' ', awalIP)

            awalPort = port + 5
            akhirPort = x.find(" ", awalPort)

        
            if akhirID == -1:
                break
            
            newUserList.append(x[awalID:akhirID])
            newIpList.append(x[awalIP:akhirIP])
            newPortList.append(x[awalPort:akhirPort])
            pos = akhirID + 1

    return user, ip, port




newUserAcc = []
newIPAcc = []
newPortAcc = []

newUserFai = []
newIPFai = []
newPortFai = []

newUserInv = []
newIPInv = []
newPortInv = []


dataData(berhasil, newUserAcc, newIPAcc, newPortAcc )
dataData(gagal, newUserFai, newIPFai, newPortFai)
datainv(invalid, newUserInv, newIPInv, newPortInv)


botBulan = []
botTanggal = []
botJam = []

botUser = []
botIp = []
botPort = []


timeSementara = []


for x in range(len(newUserInv)- 1, -1, -1):
    if newUserInv[x] == '':
        # time(x, botBulan, botTanggal, botJam)

        bot = newUserInv.pop(x)
        ip = newIPInv.pop(x)
        port = newPortInv.pop(x)
        
        waktu = invalid.pop(x)

        botUser.append(bot)
        botIp.append(ip)
        botPort.append(port)
        timeSementara.append(waktu)

time(timeSementara, botBulan, botTanggal, botJam)

# print(len(botBulan))
# print(len(botTanggal))
# print(len(botUser))
# print(len(botIp))

dataBerhasilLog = []
dataGagalLog = []
dataInvalidLog = []

def fullData(container, Len, bulan, tanggal, jam, user, ip, port):
    for i in range(len(Len)):
        container.append(data(bulan[i], tanggal[i], jam[i], user[i], ip[i], port[i]))
        
    return bulan, tanggal, jam, user, ip, port

fullData(dataBerhasilLog, newUserAcc, newBulanAcc, newTanggalAcc, newJamAcc, newUserAcc, newIPAcc, newPortAcc)
fullData(dataGagalLog, newUserFai, newBulanFai, newTanggalFai, newJamFai, newUserFai, newIPFai, newPortFai)
fullData(dataInvalidLog, newUserInv, newBulanInv, newTanggalInv, newJamInv, newUserInv, newIPInv, newPortInv)



# print(len(newUserFai))
# print(len(newIPFai))
# print(len(newPortFai))
# print(len(newJamAcc))
# print(len(newUserAcc))
# print(len(newJamFai))
# print(len(newUserFai))
# print(len(newJamInv))
# print(len(newUserInv))
# print(len(newTanggalFai))
# print(len(newBulanFai))
 
#USER ACCEPTED
userLoginTotal = {}
for x in newUserAcc:
    userLoginTotal[x] = userLoginTotal.get(x, 0) + 1


#USER GAGAL
userGagalTotal = {}
for x in newUserFai:
    userGagalTotal[x] = userGagalTotal.get(x, 0) + 1



#USER INVALID
userInvalidTotal = {}
for x in newUserInv:
    userInvalidTotal[x] = userInvalidTotal.get(x, 0) + 1


print('percobaan login dari bot ' ' ',len(botUser))

print(userLoginTotal)
print("/////////////////////////////////////////////////////////")

print(userGagalTotal)
print("/////////////////////////////////////////////////////////")

print(userInvalidTotal)





# for x in dataInvalidLog:
#     x = x["user"]
#     user


# for x in invalid:
#     print(x)
# print(invalid)
# print(newUserInv)
# print(len(newTanggalInv))
# print(len(newBulanInv))






