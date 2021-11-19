def fieldingCSVUpdate():
    with open("Fielding.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO allstarfull VALUES ("
                sql += teamsreader['ID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['stint'] + ","
                sql += teamsreader['teamID'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['POS'] + ","
                sql += teamsreader['G'] + ","
                sql += teamsreader['GS'] + ","
                sql += teamsreader['InnOuts'] + ","
                sql += teamsreader['PO'] + ","
                sql += teamsreader['A'] + ","
                sql += teamsreader['E'] + ","
                sql += teamsreader['DP'] + ","
                sql += teamsreader['PB'] + ","
                sql += teamsreader['WP'] + ","
                sql += teamsreader['SB'] + ","
                sql += teamsreader['CS'] + ","
                sql += teamsreader['ZR'] + ","
                sql += ";"
            line_count+=1