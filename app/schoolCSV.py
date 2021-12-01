import csv
def schoolsCSVUpdate():
    with open("Schools.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count!=0:
                sql = "INSERT INTO school VALUES ("
                sql += reader['schoolID'] + ","
                sql += reader['name_full'] + ","
                sql += reader['city'] + ","
                sql += reader['state'] + ","
                sql += reader['country']
                sql += ");"
            line_count +=1