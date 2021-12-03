import csv
import pymysql
import mariadbconfig as cfg

# usage:
# sql = teamsCSVUpdate()
# cur.execute(sql)
def battingPostCSVUpdate():
    sql = "INSERT INTO battingpost (playerID, yearId, teamID, round, b_G, b_AB, b_R, b_H, b_2B, b_3B, b_HR, b_RBI,b_SB,b_CS,"
    sql +=      "b_BB, b_SO, b_IBB, b_HBP, b_SH, b_SF, b_GIDP) VALUES"
    with open("BattingPost.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID']
            sql += ","
            sql += "'" + row['teamID'] + "',"
            if row['round'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['round'] + "'"
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
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = battingPostCSVUpdate()
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