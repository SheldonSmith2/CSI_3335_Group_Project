import csv
def allStarFullCSVUpdate():
    with open("AllstarFull.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO allstarfull VALUES ("
                sql += teamsreader['ID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['gameNum'] + ","
                sql += teamsreader['teamID'] + ","
                sql += teamsreader['GP'] + ","
                sql += teamsreader['startingPos'] + ","
                sql += ";"
            line_count+=1