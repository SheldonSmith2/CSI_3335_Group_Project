def peopleCSVUpdate():
    with open("allstarfull.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO allstarfull VALUES ("
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['birthYear'] + ","
                sql += teamsreader['birthMonth'] + ","
                sql += teamsreader['birthDay'] + ","
                sql += teamsreader['birthCountry'] + ","
                sql += teamsreader['birthState'] + ","
                sql += teamsreader['birthCity'] + ","
                sql += teamsreader['deathYear'] + ","
                sql += teamsreader['deathMonth'] + ","
                sql += teamsreader['deathDay'] + ","
                sql += teamsreader['deathCountry'] + ","
                sql += teamsreader['deathState'] + ","
                sql += teamsreader['deathCity'] + ","
                sql += teamsreader['nameFirst'] + ","
                sql += teamsreader['nameLast'] + ","
                sql += teamsreader['nameGiven'] + ","
                sql += teamsreader['weight'] + ","
                sql += teamsreader['height'] + ","
                sql += teamsreader['bats'] + ","
                sql += teamsreader['throws'] + ","
                sql += teamsreader['debut'] + ","
                sql += ";"
                line_count