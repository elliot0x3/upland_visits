def filterCMPropsVisits():
    cmprops = {"79520616529774": "San Francisco", "78897980593015": "Fresno", "78053214267194": "Bakersfield", "79566619660565": "Oakland",
               "81378912598000": "Manhattan", "81356145919400": "Brooklyn", "81333278573795": "Staten Island", "82107328554437": "Chicago", "81856693908761": "Cleveland"}
    cmpropids = list(cmprops.keys())
    with open("../visits2021-09-18to2021-10-31.csv", "r") as file, open("../visits2021-11-01to2021-11-22.csv", "r") as file2, open("./cmpropvisits.csv", "w") as csv:
        buffer = file.readlines()
        for b in buffer:
            if str(b.split(",")[2]) in cmpropids:
                csv.write(b)
        buffer2 = file2.readlines()
        for b in buffer2:
            if str(b.split(",")[2]) in cmpropids:
                csv.write(b)


def foundNames():
    names = {}
    with open("./names.csv", "r") as namesfile:
        for name in namesfile:
            temp = name.split(",")
            names[temp[0]] = temp[1]
    return names


def countVisits():
    idslist = []
    filterCMPropsVisits()
    with open("./cmpropvisits.csv", "r") as visits:
        for visit in visits:
            idslist.append(visit.split(",")[3])
    EosIds = set(idslist)
    # the in game names are mathced with EOSid
    names = foundNames()
    with open("leaderboard.csv", "w") as file:
        for i in EosIds:
            # few names may not be updated with the EOS ids because they can't be found on the blockchain
            # or the latest names data should be updated
            if i not in names.keys():
                file.write(i+", "+str(idslist.count(i))+", None"+"\n")
            else:
                file.write(i+", "+str(idslist.count(i))+","+names[i])


countVisits()
