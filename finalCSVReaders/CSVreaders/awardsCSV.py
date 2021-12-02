import csv
import pymysql
import mariadbconfig as cfg

def awardsCSVUpdate():
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `awards` (awardID,yearID,playerID,lgID,tie,notes) VALUES "
        for row in teamsreader:
            sql +=" ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['tie'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['tie'] + "',"
            if row['notes'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['notes'] + "'"
            
            sql += "), "
    with open("AwardsManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql +=" ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['tie'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['tie'] + "',"
            if row['notes'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['notes'] + "'"
            
            sql += "), "
    sql = sql [:-2] + ";"
    return sql
	
con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = awardsCSVUpdate()
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