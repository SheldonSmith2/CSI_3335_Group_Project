import csv
import pymysql
import mariadbconfig as cfg

def awardsShareCSVUpdate():
    with open("AwardsSharePlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `awardsShare` (awardID,yearID,playerID,lgID,pointsWon,pointsMax,votesFirst) VALUES "
        for row in teamsreader:
            sql +=" ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['pointsWon'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsWon'] + ","
            if row['pointsMax'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsMax'] + ","
            if row['votesFirst'] == "":
                sql += "NULL"
            else:
                sql += row['votesFirst']
            sql += "),"
    with open("AwardsShareManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += " ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['pointsWon'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsWon'] + ","
            if row['pointsMax'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsMax'] + ","
            if row['votesFirst'] == "":
                sql += "NULL"
            else:
                sql += row['votesFirst']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = awardsShareCSVUpdate()
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