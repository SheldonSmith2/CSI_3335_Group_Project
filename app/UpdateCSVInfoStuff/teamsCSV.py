import csv
def teamsCSVUpdate():
    sql = "INSERT INTO Team(teamID, yearID, lgID, divID, franchID, team_name, teamRank, G, G_home, W, L, DivWin, WCWin,"
    sql += "LgWin, WSWin, R, AB, H, team_2B, team_3B, team_HR, team_ BB, team_SO, team_SB, team_CS, team_HBP,team_SF,"
    sql += "team_RA, team_ER, team_ERA, team_CG, team_SHO, team_SV, team_IPouts, team_HA, team_HRA, team_BBA, team_SOA)"
    sql += " VALUES"
    with open("Teams.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            if row['teamID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['teamID'] + "'"
            sql += ","
            if row['yearID'] == "":
                sql += "NULL"
            else:
                sql += row['yearID']
            sql += ","
            if row['lgID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['lgID'] + "'"
            sql += ","
            if row['divID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['divID'] + "'"
            sql += ","
            if row['franchID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['franchID'] + "'"
            sql += ","
            if row['name'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['name'] + "'"
            sql += ","
            if row['teamRank'] == "":
                sql += "NULL"
            else:
                sql += row['teamRank']
            sql += ","
            if row['G'] == "":
                sql += "NULL"
            else:
                sql += row['G']
            sql += ","
            if row['Ghome'] == "":
                sql += "NULL"
            else:
                sql += row['Ghome']
            sql += ","
            if row['W'] == "":
                sql += "NULL"
            else:
                sql += row['W']
            sql += ","
            if row['L'] == "":
                sql += "NULL"
            else:
                sql += row['L']
            sql += ","
            if row['DivWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['DivWin'] + "'"
            sql += ","
            if row['WCWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['WCWin'] + "'"
            sql += ","
            if row['LgWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['LgWin']+ "'"
            sql += ","
            if row['WSWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['WSWin'] + "'"
            sql += ","
            if row['R'] == "":
                sql += "NULL"
            else:
                sql += row['R']
            sql += ","
            if row['AB'] == "":
                sql += "NULL"
            else:
                sql += row['AB']
            sql += ","
            if row['H'] == "":
                sql += "NULL"
            else:
                sql += row['H']
            sql += ","
            if row['2B'] == "":
                sql += "NULL"
            else:
                sql += row['2B']
            sql += ","
            if row['3B'] == "":
                sql += "NULL"
            else:
                sql += row['3B']
            sql += ","
            if row['HR'] == "":
                sql += "NULL"
            else:
                sql += row['HR']
            sql += ","
            if row['BB'] == "":
                sql += "NULL"
            else:
                sql += row['BB']
            sql += ","
            if row['SO'] == "":
                sql += "NULL"
            else:
                sql += row['SO']
            sql += ","
            if row['SB'] == "":
                sql += "NULL"
            else:
                sql += row['SB']
            sql += ","
            if row['CS'] == "":
                sql += "NULL"
            else:
                sql += row['CS']
            sql += ","
            if row['HBP'] == "":
                sql += "NULL"
            else:
                sql += row['HBP']
            sql += ","
            if row['SF'] == "":
                sql += "NULL"
            else:
                sql += row['SF']
            sql += ","
            if row['RA'] == "":
                sql += "NULL"
            else:
                sql += row['RA']
            sql += ","
            if row['ER'] == "":
                sql += "NULL"
            else:
                sql += row['ER']
            sql += ","
            if row['ERA'] == "":
                sql += "NULL"
            else:
                sql += row['ERA']
            sql += ","
            if row['CG'] == "":
                sql += "NULL"
            else:
                sql += row['CG']
            sql += ","
            if row['SHO'] == "":
                sql += "NULL"
            else:
                sql += row['SHO']
            sql += ","
            if row['SV'] == "":
                sql += "NULL"
            else:
                sql += row['SV']
            sql += ","
            if row['IPouts'] == "":
                sql += "NULL"
            else:
                sql += row['IPouts']
            sql += ","
            if row['HA']  == "":
                sql += "NULL"
            else:
                sql += row['HA']
            sql += ","
            if row['HRA'] == "":
                sql += "NULL"
            else:
                sql += row['HRA']
            sql += ","
            if row['BBA'] == "":
                sql += "NULL"
            else:
                sql += row['BBA']
            sql += ","
            if row['SOA'] == "":
                sql += "NULL"
            else:
                sql += row['SOA']
            sql += ","
            if row['E'] == "":
                sql += "NULL"
            else:
                sql += row['E']
            sql += ","
            if row['DP']  == "":
                sql += "NULL"
            else:
                sql += row['DP']
            sql += ","
            if row['FP'] == "":
                sql += "NULL"
            else:
                sql += row['FP']
            sql += "), "
    sql = sql[:-1] + ";"
    return sql
