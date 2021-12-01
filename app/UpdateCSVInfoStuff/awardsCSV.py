import csv
def awardsCSVUpdate():
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO awards(awardID,yearID,playerID,lgID,tie,notes)"
                sql +=" VALUES ("
                sql += teamsreader['awardID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['tie'] + ","
                sql += teamsreader['notes']
                sql += ");"
            line_count+=1
    with open("AwardsManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql ="INSERT INTO awards(awardID,yearID,playerID,lgID,tie,notes)"
                sql += " VALUES ("
                sql += teamsreader['awardID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['tie'] + ","
                sql += teamsreader['notes']
                sql += ");"
            line_count+=1