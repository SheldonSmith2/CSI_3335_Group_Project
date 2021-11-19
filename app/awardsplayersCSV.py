def battingCSVUpdate():
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO batting VALUES ("
                sql += teamsreader['ID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['awardID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['teamID'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['tie'] + ","
                sql += teamsreader['notes'] + ","
                sql += ";"
            line_count+=1