import csv
def parksCSVUpdate():
    with open("Parks.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0
        for row in reader:
            if line_count!=0:
                sql = "INSERT INTO park VALUES ("
                sql += (line_count-1)+ ","
                sql += reader['park.key'] + ","
                sql += reader['park.alias'] + ","
                sql += reader['park.name'] + ","
                sql += reader['city'] + ","
                sql += reader['state'] + ","
                sql += reader['country']
                sql += ");"
            line_count +=1