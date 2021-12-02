import csv
# usage:
# sql = teamsCSVUpdate()
# cur.execute(sql)
def battingCSVUpdate():
    sql = "INSERT INTO salary(playerID, yearId, teamID, stint, b_G, b_AB, b_R, b_H, b_2B, b_3B, b_HR, b_RBI,b_SB,b_CS,"
    sql +=      "b_BB, b_SO, b_IBB, b_ HBP, b_SH, b_SF, b_GIDP) VALUES"
    with open("Batting.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            sql += "("
            if row['playerID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['playerID'] + "'"
            sql += ","
            if row['yearID'] == "":
                sql += "NULL"
            else:
                sql += row['yearID']
            sql += ","

            if row['teamID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['teamID'] + "'"
            sql += ","
            if row['stint'] == "":
                sql += "NULL"
            else:
                sql += row['stint']
            sql += ","
            if row['G'] == "":
                sql += "NULL"
            else:
                sql += row['G']
            sql += ","
            if row['AB'] == "":
                sql += "NULL"
            else:
                sql += row['AB']
            sql += ","
            if row['R'] == "":
                sql += "NULL"
            else:
                sql += row['R']
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
            if row['RBI'] == "":
                sql += "NULL"
            else:
                sql += row['RBI']
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
            if row['IBB'] == "":
                sql += "NULL"
            else:
                sql += row['IBB']
            sql += ","
            if row['HBP'] == "":
                sql += "NULL"
            else:
                sql += row['HBP']
            sql += ","
            if row['SH'] == "":
                sql += "NULL"
            else:
                sql += row['SH']
            sql += ","
            if row['SF'] == "":
                sql += "NULL"
            else:
                sql += row['SF']
            sql += ","
            if row['GIDP'] == "":
                sql += "NULL"
            else:
                sql += row['GIDP']
            sql += "), "
    sql = sql[:-2] + ";"
    return sql