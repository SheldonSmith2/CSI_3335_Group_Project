import csv
import pymysql
import mariadbconfig as cfg

def fieldingCSVUpdate():
    with open("Fielding.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `fielding` (playerID,yearID,teamID,stint,position,f_G,f_GS,f_InnOuts,f_PO,f_A,f_E,f_DP,f_PB,f_WP,f_SB,f_CS,f_ZR) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['teamID'] + "',"
            sql += row['stint'] + ","
            sql += "'" + row['POS'] + "',"
            if row['G'] == "":
                sql += "NULL,"
            else:
                sql += row['G'] + ","
            if row['GS'] == "":
                sql += "NULL,"
            else:
                sql += row['GS'] + ","
            if row['InnOuts'] == "":
                sql += "NULL,"
            else:
                sql += row['InnOuts'] + ","
            if row['PO'] == "":
                sql += "NULL,"
            else:
                sql += row['PO'] + ","
            if row['A'] == "":
                sql += "NULL,"
            else:
                sql += row['A'] + ","
            if row['E'] == "":
                sql += "NULL,"
            else:
                sql += row['E'] + ","
            if row['DP'] == "":
                sql += "NULL,"
            else:
                sql += row['DP'] + ","
            if row['PB'] == "":
                sql += "NULL,"
            else:
                sql += row['PB'] + ","
            if row['WP'] == "":
                sql += "NULL,"
            else:
                sql += row['WP'] + ","
            if row['SB'] == "":
                sql += "NULL,"
            else:
                sql += row['SB'] + ","
            if row['CS'] == "":
                sql += "NULL,"
            else:
                sql += row['CS'] + ","
            if row['ZR'] == "":
                sql += "NULL"
            else:
                sql += row['ZR']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = fieldingCSVUpdate()
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