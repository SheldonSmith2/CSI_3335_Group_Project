import csv
import pymysql
import mariadbconfig as cfg

def hallOfFameUpdate():
    with open("HallOfFame.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `halloffame` (playerID,votedBy,ballots,needed,votes,inducted,category,note) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            # yearID is in the CSV, but not in the .sql script
            # sql += teamsreader['yearID'] + ","
            sql += "'" + row['votedBy'] + "',"
            if row['ballots'] == "":
                sql += "NULL,"
            else:
                sql += row['ballots'] + ","
            if row['needed'] == "":
                sql += "NULL,"
            else:
                sql += row['needed'] + ","
            if row['votes'] == "":
                sql += "NULL,"
            else:
                sql += row['votes'] + ","
            sql += "'" + row['inducted'] + "',"
            if row['category'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['category'] + "',"
            if row['needed_note'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['needed_note'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = hallOfFameUpdate()
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
