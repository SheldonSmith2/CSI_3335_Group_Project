import csv
import pymysql
import mariadbconfig as cfg

# usage:
# sql = teamsCSVUpdate()
# cur.execute(sql)
def salariesCSVUpdate():
    sql = "INSERT INTO salary(playerID, teamID, lgId, yearId, salary) VALUES "
    with open("Salaries.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            if row['playerID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['playerID'] + "',"
            if row['teamID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['teamID'] + "',"
            if row['lgID']  == "":
                sql += "NULL"
            else:
                sql += "'" + row['lgID']  + "',"
            if row['yearID'] == "":
                sql += "NULL"
            else:
                sql += row['yearID'] + ","
            if row['salary'] == "":
                sql += "NULL"
            else:
                sql += row['salary']
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = salariesCSVUpdate()
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