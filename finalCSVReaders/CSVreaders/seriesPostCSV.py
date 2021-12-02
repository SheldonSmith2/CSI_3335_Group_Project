import csv
import pymysql
import mariadbconfig as cfg

def seriesPostCSVUpdate():
    with open("SeriesPost.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `seriespost` (teamIDwinner,teamIDloser,yearID,round,wins,loses,ties) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['teamIDwinner'] + "',"
            sql += "'" + row['teamIDloser'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['round'] + "',"
            sql += row['wins'] + ","
            sql += row['losses'] + ","
            sql += row['ties']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = seriesPostCSVUpdate()
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