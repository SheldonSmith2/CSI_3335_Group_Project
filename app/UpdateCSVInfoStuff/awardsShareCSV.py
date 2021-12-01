import csv
def awardsCSVUpdate():
    with open("AwardsSharePlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO awardsShare(awardID,yearID,playerID,lgID,pointsWon,pointsMax,votesFirst)"
                sql +=" VALUES ("
                sql += teamsreader['awardID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['pointsWon'] + ","
                sql += teamsreader['pointsMax'] + ","
                sql += teamsreader['votesFirst']
                sql += ");"
            line_count+=1
    with open("AwardsShareManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO awardsShare(awardID,yearID,playerID,lgID,pointsWon,pointsMax,votesFirst)"
                sql += " VALUES ("
                sql += teamsreader['awardID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['pointsWon'] + ","
                sql += teamsreader['pointsMax'] + ","
                sql += teamsreader['votesFirst']
                sql += ");"
            line_count+=1