import csv
import pymysql
import mariadbconfig as cfg

def awardsCSVUpdate():
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        sql = "INSERT INTO `awards` (awardID,yearID,playerID,lgID,tie,notes) VALUES "
        for row in teamsreader:
            if line_count!=0:
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
            line_count+=1
    with open("AwardsManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
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
            line_count+=1
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