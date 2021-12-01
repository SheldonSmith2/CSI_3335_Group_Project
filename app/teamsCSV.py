import csv
def teamsCSVUpdate():
    with open("Teams.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql = "INSERT INTO teams VALUES ("
                sql += (line_count - 1) + ","
                sql += teamsreader['teamID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['lgID'] + ","
                sql += teamsreader['divID'] + ","
                sql += teamsreader['franchID'] + ","
                sql += teamsreader['name'] + ","
                sql += teamsreader['teamRank'] + ","
                sql += teamsreader['G'] + ","
                sql += teamsreader['Ghome'] + ","
                sql += teamsreader['W'] + ","
                sql += teamsreader['L'] + ","
                sql += teamsreader['DivWin'] + ","
                sql += teamsreader['WCWin'] + ","
                sql += teamsreader['LgWin'] + ","
                sql += teamsreader['WSWin'] + ","
                sql += teamsreader['R'] + ","
                sql += teamsreader['AB'] + ","
                sql += teamsreader['H'] + ","
                # Check if 2b and 3b are in correct position
                sql += teamsreader['2B'] + ","
                sql += teamsreader['3B'] + ","
                sql += teamsreader['HR'] + ","
                sql += teamsreader['BB'] + ","
                sql += teamsreader['SO'] + ","
                sql += teamsreader['SB'] + ","
                sql += teamsreader['CS'] + ","
                sql += teamsreader['HBP'] + ","
                sql += teamsreader['SF'] + ","
                sql += teamsreader['RA'] + ","
                sql += teamsreader['ER'] + ","
                sql += teamsreader['ERA'] + ","
                sql += teamsreader['CG'] + ","
                sql += teamsreader['SHO'] + ","
                sql += teamsreader['SV'] + ","
                sql += teamsreader['IPouts'] + ","
                sql += teamsreader['HA'] + ","
                sql += teamsreader['HRA'] + ","
                sql += teamsreader['BBA'] + ","
                sql += teamsreader['SOA'] + ","
                sql += teamsreader['E'] + ","
                sql += teamsreader['DP'] + ","
                sql += teamsreader['FP'] + ","
                sql += ");"
            line_count+=1