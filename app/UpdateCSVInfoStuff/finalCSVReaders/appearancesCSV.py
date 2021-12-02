import csv
# usage:
# sql = teamsCSVUpdate()
# cur.execute(sql)
def appearancesCSVUpdate():
    sql = "INSERT INTO appearances(playerID, yearID, teamID, stint, G_all, GS, G_batting, G_defense, G_p, G_c, G_1b,"
    sql += " G_2b, G_3b, G_ss, G_lf, G_cf, G_of, G_dh, G_ph, G_pr) VALUES "
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
            if row['G_all'] == "":
                sql += "NULL"
            else:
                sql += row['G_all']
            sql += ","
            if row['GS'] == "":
                sql += "NULL"
            else:
                sql += row['GS']
            sql += ","
            if row['G_batting'] == "":
                sql += "NULL"
            else:
                sql += row['G_batting']
            sql += ","
            if row['G_defense'] == "":
                sql += "NULL"
            else:
                sql += row['G_defense']
            sql += ","
            if row['G_p'] == "":
                sql += "NULL"
            else:
                sql += row['G_p']
            sql += ","
            if row['G_c'] == "":
                sql += "NULL"
            else:
                sql += row['G_c']
            sql += ","
            if row['G_1b'] == "":
                sql += "NULL"
            else:
                sql += row['G_1b']
            sql += ","
            if row['G_2b'] == "":
                sql += "NULL"
            else:
                sql += row['G_2b']
            sql += ","
            if row['G_3b'] == "":
                sql += "NULL"
            else:
                sql += row['G_3b']
            sql += ","
            if row['G_ss'] == "":
                sql += "NULL"
            else:
                sql += row['G_ss']
            sql += ","
            if row['G_lf'] == "":
                sql += "NULL"
            else:
                sql += row['G_lf']
            sql += ","
            if row['G_lf'] == "":
                sql += "NULL"
            else:
                sql += row['G_cf']
            sql += ","
            if row['G_of'] == "":
                sql += "NULL"
            else:
                sql += row['G_of']
            sql += ","
            if row['G_dh'] == "":
                sql += "NULL"
            else:
                sql += row['G_dh']
            sql += ","
            if row['G_ph'] == "":
                sql += "NULL"
            else:
                sql += row['G_ph']
            sql += ","
            if row['G_pr'] == "":
                sql += "NULL"
            else:
                sql += row['G_pr']
            sql += ","
    sql = sql[:-2] + ";"
    return sql