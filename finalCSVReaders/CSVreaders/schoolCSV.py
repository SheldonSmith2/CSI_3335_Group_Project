import csv
import pymysql
import mariadbconfig as cfg

def schoolsCSVUpdate():
    with open("Schools.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO school VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['schoolID'] + "',"
            sql += "'" + row['name_full'].replace("\'", "\\'") + "',"
            sql += "'" + row['city'].replace("\'", "\\'") + "',"
            sql += "'" + row['state'.replace("\'", "\\'")] + "',"
            sql += "'" + row['country'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = schoolsCSVUpdate()
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