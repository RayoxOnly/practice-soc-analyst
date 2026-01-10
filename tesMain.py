def log(file):

    return [x for x in file if "sshd" in x]

def is_valid_login_line(line):
    return "for " in line and "from " in line and "port " in line

# def if_True(line):
#     return "Accepted" in line or "Failed" in line or "invalid" in line


def parsing(x):
    x = x.replace("  ", " ")

    Auser = x.find("for ") + 4
    Buser = x.find(" ", Auser)

    Aip = x.find("from ", Buser) + 5
    Bip = x.find(" ", Aip)

    Aport= x.find("port ", Bip) + 5
    Bport = x.find(" ", Aport)

    if x[Auser:Buser] == "invalid":
        Auser = x.find("invalid user ") + 13
        Buser = x.find(" ", Auser)

    bulan = x.split()[0]
    tanggal = x.split()[1]
    jam = x.split()[2]


    status = "unknown"

    if "Accepted" in x:
        status = "Accepted publickey" if "publickey" in x else "Accepted password"

    elif "Failed" in x:
        if "invalid user" in x:
            status = "Invalid User"
        elif "message repeated" in x:
            status = "Message Repeated"
        elif "publickey" in x:
            status = "Failed Publickey"
        else:
            status = "Failed Password"

    elif "Starting session:" in x:
        status = "Session Started (Shell)"
    elif "Invalid user" in x:
        status = "Invalid User"

    elif "error" in x:
        status = "Error"


    return {
        "bulan" : bulan,
        "tanggal" : tanggal,
        "jam" : jam,
        "user" : x[Auser:Buser],
        "ip" : x[Aip:Bip],
        "port" : x[Aport:Bport],
        "status" : status
    }

# def FailedLoginIPCount(line):


with open("auth.log", "r") as f:
    logs = f.readlines()
    sshLog = log(logs)

fullData = []

for line in sshLog:
    if not is_valid_login_line(line):
        continue
    # if not if_True(line):
    #     continue
    data = parsing(line)
    fullData.append(data)


for x in fullData:
    if x["status"] ==  "unknown":
        print(x)

acceptedLog = []
failedLog = []
invalidUserLog = []



for x in fullData:
    if x["status"] == "Accepted password":
        acceptedLog.append(x)
    if x["status"] == "Failed Password":
        failedLog.append(x)
    if x["status"] == "Invalid User":
        invalidUserLog.append(x)

CounterIpFailed = []
counterIP = {}

for x in failedLog:
    CounterIpFailed.append(x["ip"])    
for x in CounterIpFailed:
    counterIP[x] = counterIP.get(x, 0)+1
sorted_ip = sorted(counterIP.items(), key=lambda item: item[1], reverse=True)

print("=== TOP ATTACKER IPs ===")
for ip, count in sorted_ip:
    print(f"IP: {ip} | Total Serangan: {count}")

allInvalidUser = []
countInvUser = {}
for x in invalidUserLog:
    allInvalidUser.append(x["user"])
for x in allInvalidUser:
    countInvUser[x] = countInvUser.get(x, 0) +1
sorted_user = sorted(countInvUser.items(), key=lambda item: item[1], reverse=True)


print("=== TOP ATTACKED USER ===")
for user, count in sorted_user: 
    print(f"User: {user} | Total Serangan: {count}")





# print(len(acceptedLog))
# print(len(failedLog))
# print(len(invalidUserLog))