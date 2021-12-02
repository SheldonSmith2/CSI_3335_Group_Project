import csv
import pymysql
import mariadbconfig as cfg

def leagueDivisionCSVUpdate():
    with open("HomeGames.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `homegames` (teamID,parkID,yearID,firstGame,lastGame,games,openings,attendence) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['team.key'] + "',"
            sql += "'" + row['park.key'] + "',"
            sql += row['year.key'] + ","
            sql += "'" + row['span.first'] + "',"
            sql += "'" + row['span.last'] + "',"
            sql += row['games'] + ","
            sql += row['openings'] + ","
            sql += row['attendance']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = leagueDivisionCSVUpdate()
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