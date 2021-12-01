import csv
def managersCSVUpdate():
    with open("Managers.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count!=0:
                sql = "INSERT INTO manager VALUES ("
                sql += (line_count - 1) + ","
                sql += reader['playerID'] + ","
                sql += reader['yearID'] + ","
                sql += reader['inseason'] + ","
                sql += reader['lgID'] + ","
                sql += reader['manager_G'] + ","
                sql += reader['manager_W'] + ","
                sql += reader['manager_L'] + ","
                sql += reader['teamRank'] + ","
                sql += reader['plyrMgr']
                sql += ");"
            line_count +=1