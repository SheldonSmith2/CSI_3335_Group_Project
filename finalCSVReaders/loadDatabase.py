# The program to load the baseball database with the data from the csv files
# Please have a file called "mariadbconfig.py" that contains your connection information

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

def schoolsCSVUpdate():
    with open("Schools.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `school` (schoolId,name,city,state,country) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['schoolID'] + "',"
            sql += "'" + row['name_full'].replace("\'", "\\'") + "',"
            sql += "'" + row['city'].replace("\'", "\\'") + "',"
            sql += "'" + row['state'].replace("\'", "\\'") + "',"
            sql += "'" + row['country'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

def parksCSVUpdate():
    with open("Parks.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `park` (parkID,park_alias,park_name,city,state,country) VALUES "
        for row in reader:
            sql += "("
            if row['park.key'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['park.key'] + "',"
            if row['park.alias'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['park.alias'].replace("\'", "\\'") + "',"
            if row['park.name'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['park.name'].replace("\'", "\\'") + "',"
            if row['city'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['city'].replace("\'", "\\'") + "',"
            if row['state'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['state'].replace("\'", "\\'") + "',"
            if row['country'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['country'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

# TODO
# Add teamID to table
def managersCSVUpdate():
    with open("Managers.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `manager` (playerID,yearID,lgID,inSeason,manager_G,manager_W,manager_L,teamRank,plyrMgr) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID'] + ","
            #sql += "'" + row['teamID'] + "'," Add in attribute list above
            sql += "'" + row['lgID'] + "',"
            sql += row['inseason'] + ","
            sql += row['G'] + ","
            sql += row['W'] + ","
            sql += row['L'] + ","
            if row['rank'] == "":
                sql += "NULL,"
            else:
                sql += row['rank'] + ","
            sql += "'" + row['plyrMgr'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

# TODO
# Add yearID to table
def hallOfFameCSVUpdate():
    with open("HallOfFame.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `halloffame` (playerID,votedBy,ballots,needed,votes,inducted,category,note) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            # sql += teamsreader['yearID'] + "," Add in attribute list above
            sql += "'" + row['votedBy'] + "',"
            if row['ballots'] == "":
                sql += "NULL,"
            else:
                sql += row['ballots'] + ","
            if row['needed'] == "":
                sql += "NULL,"
            else:
                sql += row['needed'] + ","
            if row['votes'] == "":
                sql += "NULL,"
            else:
                sql += row['votes'] + ","
            sql += "'" + row['inducted'] + "',"
            if row['category'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['category'] + "',"
            if row['needed_note'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['needed_note'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

def franchisesCSVUpdate():
    with open("TeamsFranchises.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `franchises` (franchID,franchName,active,NAassoc) VALUES "
        for row in reader:
            sql += " ("
            sql += "'" + row['franchID'] + "',"
            sql += "'" + row['franchName'].replace("\'", "\\'") + "',"
            sql += "'" + row['active'] + "',"
            if row['NAassoc'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['NAassoc'] + "'"
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

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

def fieldingPostCSVUpdate():
    with open("FieldingPost.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `fieldingpost` (playerID,yearID,teamID,round,position,f_G,f_GS,f_InnOuts,f_PO,f_A,f_E,f_DP,f_PB,f_SB,f_CS) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['teamID'] + "',"
            sql += "'" + row['round'] + "',"
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
            if row['SB'] == "":
                sql += "NULL,"
            else:
                sql += row['SB'] + ","
            if row['CS'] == "":
                sql += "NULL"
            else:
                sql += row['CS']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

def awardsShareCSVUpdate():
    with open("AwardsSharePlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `awardsShare` (awardID,yearID,playerID,lgID,pointsWon,pointsMax,votesFirst) VALUES "
        for row in teamsreader:
            sql +=" ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['pointsWon'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsWon'] + ","
            if row['pointsMax'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsMax'] + ","
            if row['votesFirst'] == "":
                sql += "NULL"
            else:
                sql += row['votesFirst']
            sql += "),"
    with open("AwardsShareManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += " ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['pointsWon'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsWon'] + ","
            if row['pointsMax'] == "":
                sql += "NULL,"
            else:
                sql += row['pointsMax'] + ","
            if row['votesFirst'] == "":
                sql += "NULL"
            else:
                sql += row['votesFirst']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

def awardsCSVUpdate():
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `awards` (awardID,yearID,playerID,lgID,tie,notes) VALUES "
        for row in teamsreader:
            sql +=" ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['tie'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['tie'] + "',"
            if row['notes'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['notes'] + "'"
            
            sql += "), "
    with open("AwardsManagers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql +=" ("
            sql += "'" + row['awardID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['playerID'] + "',"
            sql += "'" + row['lgID'] + "',"
            if row['tie'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['tie'] + "',"
            if row['notes'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['notes'] + "'"
            
            sql += "), "
    sql = sql [:-2] + ";"
    return sql

def allStarFullCSVUpdate():
    with open("AllstarFull.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `allstarfull` (playerID,lgID,yearID,gameNum,gameID,GP,startingPos) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            if row['lgID'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['lgID'] + "',"
            if row['yearID'] == "":
                sql += "NULL,"
            else:
                sql += row['yearID'] + ","
            if row['gameNum'] == "":
                sql += "NULL,"
            else:
                sql += row['gameNum'] + ","
            if row['gameID'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['gameID'] + "',"
            sql += row['GP'] + ","
            if row['startingPos'] == "":
                sql += "NULL"
            else:
                sql += row['startingPos']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

def seriesPostCSVUpdate():
    with open("SeriesPost.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `seriespost` (teamIDwinner,teamIDloser,yearID,round,wins,loses,ties) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['teamIDwinner'] + "',"
            sql += "'" + row['teamIDloser'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['round'] + "',"
            sql += row['wins'] + ","
            sql += row['losses'] + ","
            sql += row['ties']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

def homeGamesCSVUpdate():
    with open("HomeGames.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `homegames` (teamID,parkID,yearID,firstGame,lastGame,games,openings,attendence) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['team.key'] + "',"
            sql += "'" + row['park.key'] + "',"
            sql += row['year.key'] + ","
            sql += "'" + row['span.first'] + "',"
            sql += "'" + row['span.last'] + "',"
            sql += row['games'] + ","
            sql += row['openings'] + ","
            sql += row['attendance']
            sql += "),"
    sql = sql [:-1] + ";"
    return sql

# Remove LeagueDivision table and foreign keys from all tables
# TODO

con = pymysql.connect(host=cfg.root['host'], user=cfg.root['user'], password=cfg.root['password'], database=cfg.root['database'])

try:
    cur = con.cursor()
    finalSql = peopleCSVUpdate()
    cur.execute(finalSql)
    print("People table loaded")

    finalSql = schoolsCSVUpdate()
    cur.execute(finalSql)
    print("School table loaded")

    finalSql = parksCSVUpdate()
    cur.execute(finalSql)
    print("Parks table loaded")

    finalSql = managersCSVUpdate()
    cur.execute(finalSql)
    print("Manager table loaded")

    finalSql = hallOfFameCSVUpdate()
    cur.execute(finalSql)
    print("HallOfFame table loaded")

    finalSql = franchisesCSVUpdate()
    cur.execute(finalSql)
    print("Franchises table loaded")

    finalSql = fieldingCSVUpdate()
    cur.execute(finalSql)
    print("Fielding table loaded")

    finalSql = fieldingPostCSVUpdate()
    cur.execute(finalSql)
    print("FieldingPost table loaded")

    finalSql = awardsShareCSVUpdate()
    cur.execute(finalSql)
    print("AwardsShare table loaded")

    finalSql = awardsCSVUpdate()
    cur.execute(finalSql)
    print("Awards table loaded")

    finalSql = allStarFullCSVUpdate()
    cur.execute(finalSql)
    print("AllStarFull table loaded")

    finalSql = seriesPostCSVUpdate()
    cur.execute(finalSql)
    print("SeriesPost table loaded")

    finalSql = homeGamesCSVUpdate()
    cur.execute(finalSql)
    print("HomeGames table loaded")
except:
    con.rollback()
    print("Database exception")
    raise
else:
    con.commit()
finally:
    con.close()