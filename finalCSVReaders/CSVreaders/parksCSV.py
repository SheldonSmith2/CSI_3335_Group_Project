import csv
import pymysql
import mariadbconfig as cfg

def parksCSVUpdate():
    with open("Parks.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `park` (parkID,park_alias,park_name,city,state,country) VALUES "
        for row in reader:
            sql += "("
            if row['park.key'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['park.key'] + "',"
            if row['park.alias'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['park.alias'].replace("\'", "\\'") + "',"
            if row['park.name'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['park.name'].replace("\'", "\\'") + "',"
            if row['city'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['city'].replace("\'", "\\'") + "',"
            if row['state'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['state'].replace("\'", "\\'") + "',"
            if row['country'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['country'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = parksCSVUpdate()
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