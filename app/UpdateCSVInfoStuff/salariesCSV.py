import csv
def salariesCSVUpdate():
    with open("Salaries.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:

                sql = "INSERT INTO salaries VALUES ("
                sql += teamsreader['ID'] + ","
                sql += teamsreader['yearID'] + ","
                sql += teamsreader['round'] + ","
                sql += teamsreader['teamIDwinner'] + ","
                sql += teamsreader['lgIDwinner'] + ","
                sql += teamsreader['teamIDloser'] + ","
                sql += teamsreader['lgIDloser'] + ","
                sql += teamsreader['wins'] + ","
                sql += teamsreader['losses'] + ","
                sql += teamsreader['ties'] + ","
                sql += ";"
            line_count+=1