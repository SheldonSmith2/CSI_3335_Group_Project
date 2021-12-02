import csv
def salariesCSVUpdate():
    sql = "INSERT INTO salary(playerID, teamID, lgId, yearId, salary) VALUES ("
    with open("Salaries.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        null_Count = 0
        for row in teamsreader:
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
            sql += "), "
    sql = sql[:-2] + ";"
    return sql