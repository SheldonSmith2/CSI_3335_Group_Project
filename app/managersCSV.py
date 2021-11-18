def managersCSVUpdate(fileName):
    with open("allstarfull.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count!=0:
                sql = "INSERT INTO allstarfull VALUES ("
                sql += reader['ID'] + ","
                sql += reader['playerid'] + ","
                sql += reader['yearID'] + ","
                sql += reader['teamID'] + ","
                sql += reader['lgID'] + ","
                sql += reader['G'] + ","
                sql += reader['W'] + ","
                sql += reader['L'] + ","
                sql += reader['teamRank'] + ","
                sql += reader['plyrMgr']
                sql += ";"
                line_count +=1