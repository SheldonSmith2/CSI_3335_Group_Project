import csv
import pymysql
import mariadbconfig as cfg

def peopleCSVUpdate():
    with open("People.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = '''INSERT INTO `people` 
                    (playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,
                    deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debutDate,finalGameDate) VALUES '''
        for row in teamsreader:
            sql += " ("
            sql += "'" + row['playerID'] + "',"
            if row['birthYear'] == "":
                sql += "NULL,"
            else:
                sql += row['birthYear'] + ","
            if row['birthMonth'] == "":
                sql += "NULL,"
            else:
                sql += row['birthMonth'] + ","
            if row['birthDay'] == "":
                sql += "NULL,"
            else:
                sql += row['birthDay'] + ","
            sql += "'" + row['birthCountry'].replace("\'", "\\'") + "',"
            sql += "'" + row['birthState'].replace("\'", "\\'") + "',"
            sql += "'" + row['birthCity'].replace("\'", "\\'") + "',"
            if row['deathYear'] == "":
                sql += "NULL,"
            else:
                sql += row['deathYear'] + ","
            if row['deathMonth'] == "":
                sql += "NULL,"
            else:
                sql += row['deathMonth'] + ","
            if row['deathDay'] == "":
                sql += "NULL,"
            else:
                sql += row['deathDay'] + ","
            if row['deathCountry'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['deathCountry'].replace("\'", "\\'") + "',"
            if row['deathState'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['deathState'].replace("\'", "\\'") + "',"
            if row['deathDay'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['deathDay'].replace("\'", "\\'") + "',"
            sql += "'" + row['nameFirst'].replace("\'", "\\'") + "',"
            sql += "'" + row['nameLast'].replace("\'", "\\'") + "',"
            sql += "'" + row['nameGiven'].replace("\'", "\\'") + "',"
            
            if row['weight'] == "":
                sql += "NULL,"
            else:
                sql += row['weight'] + ","
            if row['height'] == "":
                sql += "NULL,"
            else:
                sql += row['height'] + ","
            if row['bats'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['bats'] + "',"
            if row['throws'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['throws'] + "',"
            if row['debut'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['debut'] + "',"
            if row['finalGame'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['finalGame'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

finalSql = peopleCSVUpdate()
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