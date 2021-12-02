import csv
def allStarFullCSVUpdate():
    sql = "INSERT INTO `allstarfull`(playerID, lgID, yearID, gameNum, gameID, GP, startingPos) VALUES"
    with open("AllstarFull.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            if row['playerID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['playerID'] + "'"
            sql += ","
            if row['lgID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['lgID'] + "'"
            sql += ","
            if row['yearID'] == "":
                sql += "NULL"
            else:
                sql += row['yearID']
            sql += ","
            if row['gameNum'] == "":
                sql += "NULL"
            else:
                sql += row['gameNum']
            sql += ","
            if row['gameID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['gameID'] + "'"
            sql += ","
            if row['GP'] == "":
                sql += "NULL"
            else:
                sql += row['GP']
            sql += ","
            if row['startingPos'] == "":
                sql += "NULL"
            else:
                sql += row['startingPos']
            sql += "), "
    sql = sql[:-2] + ";"
    return sql