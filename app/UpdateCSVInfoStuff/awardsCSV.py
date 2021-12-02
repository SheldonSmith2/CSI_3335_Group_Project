import csv
import pymysql
import sys
import warnings
def awardsCSVUpdate():
    sql = ""
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql += "INSERT INTO awards(awardID,yearID,playerID,lgID,tie,notes)"
                sql +=" VALUES ("
                sql += row['awardID'] + ","
                sql += row['yearID'] + ","
                sql += row['playerID'] + ","
                sql += row['lgID'] + ","
                sql += row['tie'] + ","
                sql += row['notes']
                sql += ");"
            line_count+=1
    with open("AwardsManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        line_count = 0
        for row in teamsreader:
            if line_count!=0:
                sql +="INSERT INTO awards(awardID,yearID,playerID,lgID,tie,notes)"
                sql += " VALUES ("
                sql += row['awardID'] + ","
                sql += row['yearID'] + ","
                sql += row['playerID'] + ","
                sql += row['lgID'] + ","
                sql += row['tie'] + ","
                sql += row['notes']
                sql += ");"
            line_count+=1
    return sql
