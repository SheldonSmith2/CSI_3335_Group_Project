import csv
import pymysql
import mariadbconfig as cfg

# usage:
# sql = teamsCSVUpdate()
# cur.execute(sql)
def appearancesCSVUpdate():
    sql = "INSERT INTO appearances (playerID, yearID, teamID, G_all, GS, G_batting, G_defense, G_p, G_c, G_1b,"
    sql += " G_2b, G_3b, G_ss, G_lf, G_cf, G_of, G_dh, G_ph, G_pr) VALUES "
    with open("Appearances.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID']
            sql += ","
            sql += "'" + row['teamID'] + "',"
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
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = appearancesCSVUpdate()
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
