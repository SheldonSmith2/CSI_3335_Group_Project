import csv
import pymysql
import mariadbconfig as cfg

# usage:
# sql = teamsCSVUpdate()
# cur.execute(sql)
def teamsCSVUpdate():
    sql = "INSERT INTO `team` (teamID, yearID, lgID, divID, franchID, name, teamRank, team_G, team_G_home, team_W, team_L"
    sql += ", DivWin, WCWin,LgWin, WSWin, team_R, team_AB, team_H,team_2B, team_3B,team_HR,team_BB, team_SO, team_SB, "
    sql += " team_CS, team_HBP,team_SF,team_RA, team_ER, team_ERA, team_CG, team_SHO, team_SV, team_IPouts,team_HA, "
    sql += " team_HRA, team_BBA, team_SOA)"
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
                sql += "'" + row['name'].replace("\'", "\\'") + "'"
            sql += ","
            if row['Rank'] == "":
                sql += "NULL"
            else:
                sql += row['Rank']
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
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = teamsCSVUpdate()
#print(finalSql)

try:
    cur = con.cursor()
    cur.execute(finalSql)
except:
    con.rollback()
    print("Database exception")
    raise
else:
    con.commit()
finally:
    con.close()