import csv
import pymysql
import mariadbconfig as cfg

def franchisesCSVUpdate():
    with open("TeamsFranchises.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `franchises` (franchID,franchName,active,NAassoc) VALUES "
        for row in reader:
            sql += " ("
            sql += "'" + row['franchID'] + "',"
            sql += "'" + row['franchName'].replace("\'", "\\'") + "',"
            sql += "'" + row['active'] + "',"
            if row['NAassoc'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['NAassoc'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = franchisesCSVUpdate()
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