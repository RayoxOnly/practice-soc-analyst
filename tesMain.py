def log(file):

    return [x for x in file if "sshd" in x]

def is_valid_login_line(line):
    return "for " in line and "from " in line and "port " in line

def if_True(line):
    return "Accepted" in line or "Failed" in line or "invalid" in line


def parsing(x):
    x = x.replace("  ", " ")

    Auser = x.find("for ") + 4
    Buser = x.find(" ", Auser)

    Aip = x.find("from ", Buser) + 5
    Bip = x.find(" ", Aip)

    Aport= x.find("port ", Bip) + 5
    Bport = x.find(" ", Aport)

    # if x[Auser:Buser] == "invalid":
    #     Aip = x.find("from ", Buser) + 5
    #     Bip = x.find(" ", Aip)

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

    elif "Invalid user" in x:
        status = "Invalid User"


    return {
        "bulan" : bulan,
        "tanggal" : tanggal,
        "jam" : jam,
        "user" : x[Auser:Buser],
        "ip" : x[Aip:Bip],
        "port" : x[Aport:Bport],
        "status" : status
    }

with open("auth.log", "r") as f:
    logs = f.readlines()
    sshLog = log(logs)

# for x in sshLog:
#     if "invalid"in x:
#         print(x)

fullData = []

for line in sshLog:
    if not is_valid_login_line(line):
        continue
    if not if_True(line):
        continue
    data = parsing(line)
    fullData.append(data)

# for x in fullData:
    # if x["status"] == "unknown":
    #     print(x)
    # print(x)
# print(fullData)
for x in fullData:
    if x["status"] == "unknown":
        print(x)

