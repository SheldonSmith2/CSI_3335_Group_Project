import csv
def battingCSVUpdate():
    with open("Batting.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO batting VALUES ("
                sql += teamsreader['ID'] + ","
                sql += teamsreader['playerid'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['stint'] + ","
                sql += teamsreader['teamID'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['G'] + ","
                sql += teamsreader['AB'] + ","
                sql += teamsreader['R'] + ","
                sql += teamsreader['H'] + ","
                sql += teamsreader['HR'] + ","
                sql += teamsreader['RBI'] + ","
                sql += teamsreader['SB'] + ","
                #Check if 2b and 3b are in correct position
                sql += teamsreader['2B'] + ","
                sql += teamsreader['3B'] + ","
                sql += teamsreader['CS'] + ","
                sql += teamsreader['BB'] + ","
                sql += teamsreader['SO'] + ","
                sql += teamsreader['IBB'] + ","
                sql += teamsreader['HBP'] + ","
                sql += teamsreader['SH'] + ","
                sql += teamsreader['SF'] + ","
                sql += teamsreader['GIDP'] + ","
                sql += ";"
            line_count+=1