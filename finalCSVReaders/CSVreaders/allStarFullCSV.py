import csv
import pymysql
import mariadbconfig as cfg

def allStarFullCSVUpdate():
    with open("AllstarFull.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `allstarfull` (playerID,lgID,yearID,gameNum,gameID,GP,startingPos) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            if row['lgID'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['lgID'] + "',"
            if row['yearID'] == "":
                sql += "NULL,"
            else:
                sql += row['yearID'] + ","
            if row['gameNum'] == "":
                sql += "NULL,"
            else:
                sql += row['gameNum'] + ","
            if row['gameID'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['gameID'] + "',"
            sql += row['GP'] + ","
            if row['startingPos'] == "":
                sql += "NULL"
            else:
                sql += row['startingPos']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql
        
con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = allStarFullCSVUpdate()
print(finalSql)

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
