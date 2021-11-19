def battingCSVUpdate():
    with open("HallOfFame.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO halloffame VALUES ("
                sql += teamsreader['ID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['votedBy'] + ","
                sql += teamsreader['ballots'] + ","
                sql += teamsreader['needed'] + ","
                sql += teamsreader['votes'] + ","
                sql += teamsreader['inducted'] + ","
                sql += teamsreader['category'] + ","
                sql += teamsreader['needed_note'] + ","
                sql += ";"
            line_count+=1