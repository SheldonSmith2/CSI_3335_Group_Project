import csv
def franchisesCSVUpdate():
    with open("TeamsFranchises.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count!=0:
                sql = "INSERT INTO franchises VALUES ("
                sql += reader['franchID'] + ","
                sql += reader['franchName'] + ","
                sql += reader['active'] + ","
                sql += reader['NAassoc']
                sql += ");"
            line_count +=1