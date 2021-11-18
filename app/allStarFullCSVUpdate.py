def allStarFullCSVUpdate(fileName):
    with open(fileName) as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql = "INSERT INTO allstarfull VALUES ("
            for col in teamsreader:
                sql += teamsreader['ID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['gameNum'] + ","
                sql += teamsreader['teamID'] + ","
                sql += teamsreader['GP'] + ","
                sql += teamsreader['startingPos'] + ","
            sql += ";"