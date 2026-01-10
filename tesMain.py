def log(file):

    return [x for x in file if "sshd" in x]

def is_valid_login_line(line):
    return "for " in line and "from " in line and "port " in line

def parsing(x):
    x = x.replace("  ", " ")
    pos = 0

    Auser = x.find("for ", pos) + 4
    Buser = x.find(" ", Auser)

    Aip = x.find("from ", Buser) + 5
    Bip = x.find(" ", Aip)

    Aport= x.find("port ", Bip) + 5
    Bport = x.find(" ", Aport)

    pos = Bport

    bulan = x.split()[0]
    tanggal = x.split()[1]
    jam = x.split()[2]

    if "Accepted password" in x:
        status = "Accepted"
    elif "Failed password" in x:
        status = "Failed"
    else:
        status = "Unknown"

    return {
        "bulan" : bulan,
        "tanggal" : tanggal,
        "jam" : jam,
        "user" : x[Auser:Buser],
        "ip" : x[Aip:Bip],
        "port" : x[Aport:Bport],
        "status" : status
    }

# def accepted():




with open("auth.log", "r") as f:
    logs = f.readlines()
    sshLog = log(logs)

fullData = []

for line in sshLog:
    if not is_valid_login_line(line):
        continue
    data = parsing(line)
    fullData.append(data)

for x in fullData:
    print(x)



