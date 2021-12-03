import csv
import pymysql
import mariadbconfig as cfg

def managersCSVUpdate():
    with open("Managers.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `manager` (playerID,yearID,teamID,inSeason,manager_G,manager_W,manager_L,teamRank,plyrMgr) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['teamID'] + "',"
            sql += row['inseason'] + ","
            sql += row['G'] + ","
            sql += row['W'] + ","
            sql += row['L'] + ","
            if row['rank'] == "":
                sql += "NULL,"
            else:
                sql += row['rank'] + ","
            sql += "'" + row['plyrMgr'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = managersCSVUpdate()
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