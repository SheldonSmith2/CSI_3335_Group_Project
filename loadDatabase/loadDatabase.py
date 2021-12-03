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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
    return sql


def managersCSVUpdate():
    with open("Managers.csv", mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        sql = "INSERT INTO `manager` (playerID,yearID,teamID,inSeason,manager_G,manager_W,manager_L,teamRank,plyrMgr) VALUES "
        for row in reader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID'] + ","
            sql += "'" + row['teamID'] + "',"
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


def hallOfFameCSVUpdate():
    with open("HallOfFame.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `halloffame` (playerID,yearID,votedBy,ballots,needed,votes,inducted,category,note) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID'] + ","
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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
    return sql


def awardsShareCSVUpdate():
    with open("AwardsSharePlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `awardsShare` (awardID,yearID,playerID,lgID,pointsWon,pointsMax,votesFirst) VALUES "
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
    sql = sql[:-1] + ";"
    return sql


def awardsCSVUpdate():
    with open("AwardsPlayers.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `awards` (awardID,yearID,playerID,lgID,tie,notes) VALUES "
        for row in teamsreader:
            sql += " ("
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
            sql += " ("
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
    sql = sql[:-2] + ";"
    return sql


def allStarFullCSVUpdate():
    with open("AllstarFull.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        sql = "INSERT INTO `allstarfull` (playerID,lgID,teamID,yearID,gameNum,gameID,GP,startingPos) VALUES "
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            if row['lgID'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['lgID'] + "',"
            if row['teamID'] == "":
                sql += "NULL,"
            else:
                sql += "'" + row['teamID'] + "',"
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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
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
    sql = sql[:-1] + ";"
    return sql

def teamsCSVUpdate():
    sql = "INSERT INTO `team` (teamID, yearID, lgID, divID, franchID, name, teamRank, team_G, team_G_home, team_W, team_L"
    sql += ", DivWin, WCWin,LgWin, WSWin, team_R, team_AB, team_H,team_2B, team_3B,team_HR,team_BB, team_SO, team_SB, "
    sql += " team_CS, team_HBP,team_SF,team_RA, team_ER, team_ERA, team_CG, team_SHO, team_SV, team_IPouts,team_HA, "
    sql += " team_HRA, team_BBA, team_SOA)"
    sql += " VALUES"
    with open("Teams.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            if row['teamID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['teamID'] + "'"
            sql += ","
            if row['yearID'] == "":
                sql += "NULL"
            else:
                sql += row['yearID']
            sql += ","
            if row['lgID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['lgID'] + "'"
            sql += ","
            if row['divID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['divID'] + "'"
            sql += ","
            if row['franchID'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['franchID'] + "'"
            sql += ","
            if row['name'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['name'].replace("\'", "\\'") + "'"
            sql += ","
            if row['Rank'] == "":
                sql += "NULL"
            else:
                sql += row['Rank']
            sql += ","
            if row['G'] == "":
                sql += "NULL"
            else:
                sql += row['G']
            sql += ","
            if row['Ghome'] == "":
                sql += "NULL"
            else:
                sql += row['Ghome']
            sql += ","
            if row['W'] == "":
                sql += "NULL"
            else:
                sql += row['W']
            sql += ","
            if row['L'] == "":
                sql += "NULL"
            else:
                sql += row['L']
            sql += ","
            if row['DivWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['DivWin'] + "'"
            sql += ","
            if row['WCWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['WCWin'] + "'"
            sql += ","
            if row['LgWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['LgWin']+ "'"
            sql += ","
            if row['WSWin'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['WSWin'] + "'"
            sql += ","
            if row['R'] == "":
                sql += "NULL"
            else:
                sql += row['R']
            sql += ","
            if row['AB'] == "":
                sql += "NULL"
            else:
                sql += row['AB']
            sql += ","
            if row['H'] == "":
                sql += "NULL"
            else:
                sql += row['H']
            sql += ","
            if row['2B'] == "":
                sql += "NULL"
            else:
                sql += row['2B']
            sql += ","
            if row['3B'] == "":
                sql += "NULL"
            else:
                sql += row['3B']
            sql += ","
            if row['HR'] == "":
                sql += "NULL"
            else:
                sql += row['HR']
            sql += ","
            if row['BB'] == "":
                sql += "NULL"
            else:
                sql += row['BB']
            sql += ","
            if row['SO'] == "":
                sql += "NULL"
            else:
                sql += row['SO']
            sql += ","
            if row['SB'] == "":
                sql += "NULL"
            else:
                sql += row['SB']
            sql += ","
            if row['CS'] == "":
                sql += "NULL"
            else:
                sql += row['CS']
            sql += ","
            if row['HBP'] == "":
                sql += "NULL"
            else:
                sql += row['HBP']
            sql += ","
            if row['SF'] == "":
                sql += "NULL"
            else:
                sql += row['SF']
            sql += ","
            if row['RA'] == "":
                sql += "NULL"
            else:
                sql += row['RA']
            sql += ","
            if row['ER'] == "":
                sql += "NULL"
            else:
                sql += row['ER']
            sql += ","
            if row['ERA'] == "":
                sql += "NULL"
            else:
                sql += row['ERA']
            sql += ","
            if row['CG'] == "":
                sql += "NULL"
            else:
                sql += row['CG']
            sql += ","
            if row['SHO'] == "":
                sql += "NULL"
            else:
                sql += row['SHO']
            sql += ","
            if row['SV'] == "":
                sql += "NULL"
            else:
                sql += row['SV']
            sql += ","
            if row['IPouts'] == "":
                sql += "NULL"
            else:
                sql += row['IPouts']
            sql += ","
            if row['HA']  == "":
                sql += "NULL"
            else:
                sql += row['HA']
            sql += ","
            if row['HRA'] == "":
                sql += "NULL"
            else:
                sql += row['HRA']
            sql += ","
            if row['BBA'] == "":
                sql += "NULL"
            else:
                sql += row['BBA']
            sql += ","
            if row['SOA'] == "":
                sql += "NULL"
            else:
                sql += row['SOA']
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

def salariesCSVUpdate():
    sql = "INSERT INTO salary(playerID, teamID, lgId, yearId, salary) VALUES "
    with open("Salaries.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
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
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

def pitchingPostCSVUpdate():
    sql = "INSERT INTO pitchingpost (playerID,yearId,teamID,round, p_W, p_L, p_G,p_GS, p_CG,p_SHO,p_SV,p_IPOuts,p_H,p_ER,p_HR,"
    sql += "p_BB, p_SO, p_BAOpp, p_ERA, p_IBB, p_WP, p_HBP, p_BK, p_BFP, p_GF, p_R, p_SH, p_SF, p_GIDP) VALUES"
    with open("PitchingPost.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
                sql += "("
                sql += "'" + row['playerID'] + "',"
                sql += row['yearID'] + ","
                sql += "'" + row['teamID'] + "',"
                if row['round'] == "":
                    sql += "NULL"
                else:
                    sql += "'" + row['round'] + "'"
                sql += ","
                if row['W'] == "":
                    sql += "NULL"
                else:
                    sql += row['W']
                sql += ","
                if row['L'] == "":
                    sql += "NULL"
                else:
                    sql += row['L']
                sql += ","
                if row['G'] == "":
                    sql += "NULL"
                else:
                    sql += row['G']
                sql += ","
                if row['GS'] == "":
                    sql += "NULL"
                else:
                    sql += row['GS']
                sql += ","
                if row['CG'] == "":
                    sql += "NULL"
                else:
                    sql += row['CG']
                sql += ","
                if row['SHO'] == "":
                    sql += "NULL"
                else:
                    sql += row['SHO']
                sql += ","
                if row['SV'] == "":
                    sql += "NULL"
                else:
                    sql += row['SV']
                sql += ","
                if row['IPouts'] == "":
                    sql += "NULL"
                else:
                    sql += row['IPouts']
                sql += ","
                if row['H'] == "":
                    sql += "NULL"
                else:
                    sql += row['H']
                sql += ","
                if row['ER'] == "":
                    sql += "NULL"
                else:
                    sql += row['ER']
                sql += ","
                if row['HR'] == "":
                    sql += "NULL"
                else:
                    sql += row['HR']
                sql += ","
                if row['BB'] == "":
                    sql += "NULL"
                else:
                    sql += row['BB']
                sql += ","
                if row['SO'] == "":
                    sql += "NULL"
                else:
                    sql += row['SO']
                sql += ","
                if row['BAOpp'] == "":
                    sql += "NULL"
                else:
                    sql += row['BAOpp']
                sql += ","
                if row['ERA'] == "":
                    sql += "NULL"
                elif row['ERA'] == "inf":
                    sql += "-1"
                else:
                    sql += row['ERA']
                sql += ","
                if row['IBB'] == "":
                    sql += "NULL"
                else:
                    sql += row['IBB']
                sql += ","
                if row['WP'] == "":
                    sql += "NULL"
                else:
                    sql += row['WP']
                sql += ","
                if row['HBP'] == "":
                    sql += "NULL"
                else:
                    sql += row['HBP']
                sql += ","
                if row['BK'] == "":
                    sql += "NULL"
                else:
                    sql += row['BK']
                sql += ","
                if row['BFP'] == "":
                    sql += "NULL"
                else:
                    sql += row['BFP']
                sql += ","
                if row['GF'] == "":
                    sql += "NULL"
                else:
                    sql += row['GF']
                sql += ","
                if row['R'] == "":
                    sql += "NULL"
                else:
                    sql += row['R']
                sql += ","
                if row['SH'] == "":
                    sql += "NULL"
                else:
                    sql += row['SH']
                sql += ","
                if row['SF'] == "":
                    sql += "NULL"
                else:
                    sql += row['SF']
                sql += ","
                if row['GIDP'] == "":
                    sql += "NULL"
                else:
                    sql += row['GIDP']
                sql += "),"
    sql = sql[:-1] + ";"
    return sql

def pitchingCSVUpdate():
    sql = "INSERT INTO pitching (playerID,yearId,teamID,stint,p_W,p_L,p_G,p_GS,p_CG,p_SHO,p_SV, p_IPOuts, p_H, p_ER, p_HR,"
    sql += "p_BB, p_SO, p_BAOpp, p_ERA, p_IBB, p_WP, p_HBP, p_BK, p_BFP, p_GF, p_R, p_SH, p_SF, p_GIDP) VALUES"
    with open("Pitching.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
                sql += "("
                sql += "'" + row['playerID'] + "',"
                sql += row['yearID']
                sql += ","
                sql += "'" + row['teamID'] + "',"
                if row['stint'] == "":
                    sql += "NULL"
                else:
                    sql += row['stint']
                sql += ","
                if row['W'] == "":
                    sql += "NULL"
                else:
                    sql += row['W']
                sql += ","
                if row['L'] == "":
                    sql += "NULL"
                else:
                    sql += row['L']
                sql += ","
                if row['G'] == "":
                    sql += "NULL"
                else:
                    sql += row['G']
                sql += ","
                if row['GS'] == "":
                    sql += "NULL"
                else:
                    sql += row['GS']
                sql += ","
                if row['CG'] == "":
                    sql += "NULL"
                else:
                    sql += row['CG']
                sql += ","
                if row['SHO'] == "":
                    sql += "NULL"
                else:
                    sql += row['SHO']
                sql += ","
                if row['SV'] == "":
                    sql += "NULL"
                else:
                    sql += row['SV']
                sql += ","
                if row['IPouts'] == "":
                    sql += "NULL"
                else:
                    sql += row['IPouts']
                sql += ","
                if row['H'] == "":
                    sql += "NULL"
                else:
                    sql += row['H']
                sql += ","
                if row['ER'] == "":
                    sql += "NULL"
                else:
                    sql += row['ER']
                sql += ","
                if row['HR'] == "":
                    sql += "NULL"
                else:
                    sql += row['HR']
                sql += ","
                if row['BB'] == "":
                    sql += "NULL"
                else:
                    sql += row['BB']
                sql += ","
                if row['SO'] == "":
                    sql += "NULL"
                else:
                    sql += row['SO']
                sql += ","
                if row['BAOpp'] == "":
                    sql += "NULL"
                else:
                    sql += row['BAOpp']
                sql += ","
                if row['ERA'] == "":
                    sql += "NULL"
                elif row['ERA'] == "inf":
                    sql += "-1"
                else:
                    sql += row['ERA']
                sql += ","
                if row['IBB'] == "":
                    sql += "NULL"
                else:
                    sql += row['IBB']
                sql += ","
                if row['WP'] == "":
                    sql += "NULL"
                else:
                    sql += row['WP']
                sql += ","
                if row['HBP'] == "":
                    sql += "NULL"
                else:
                    sql += row['HBP']
                sql += ","
                if row['BK'] == "":
                    sql += "NULL"
                else:
                    sql += row['BK']
                sql += ","
                if row['BFP'] == "":
                    sql += "NULL"
                else:
                    sql += row['BFP']
                sql += ","
                if row['GF'] == "":
                    sql += "NULL"
                else:
                    sql += row['GF']
                sql += ","
                if row['R'] == "":
                    sql += "NULL"
                else:
                    sql += row['R']
                sql += ","
                if row['SH'] == "":
                    sql += "NULL"
                else:
                    sql += row['SH']
                sql += ","
                if row['SF'] == "":
                    sql += "NULL"
                else:
                    sql += row['SF']
                sql += ","
                if row['GIDP'] == "":
                    sql += "NULL"
                else:
                    sql += row['GIDP']
                sql += "),"
    sql = sql[:-1] + ";"
    return sql

def battingPostCSVUpdate():
    sql = "INSERT INTO battingpost (playerID, yearId, teamID, round, b_G, b_AB, b_R, b_H, b_2B, b_3B, b_HR, b_RBI,b_SB,b_CS,"
    sql +=      "b_BB, b_SO, b_IBB, b_HBP, b_SH, b_SF, b_GIDP) VALUES"
    with open("BattingPost.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID']
            sql += ","
            sql += "'" + row['teamID'] + "',"
            if row['round'] == "":
                sql += "NULL"
            else:
                sql += "'" + row['round'] + "'"
            sql += ","
            if row['G'] == "":
                sql += "NULL"
            else:
                sql += row['G']
            sql += ","
            if row['AB'] == "":
                sql += "NULL"
            else:
                sql += row['AB']
            sql += ","
            if row['R'] == "":
                sql += "NULL"
            else:
                sql += row['R']
            sql += ","
            if row['H'] == "":
                sql += "NULL"
            else:
                sql += row['H']
            sql += ","
            if row['2B'] == "":
                sql += "NULL"
            else:
                sql += row['2B']
            sql += ","
            if row['3B'] == "":
                sql += "NULL"
            else:
                sql += row['3B']
            sql += ","
            if row['HR'] == "":
                sql += "NULL"
            else:
                sql += row['HR']
            sql += ","
            if row['RBI'] == "":
                sql += "NULL"
            else:
                sql += row['RBI']
            sql += ","
            if row['SB'] == "":
                sql += "NULL"
            else:
                sql += row['SB']
            sql += ","
            if row['CS'] == "":
                sql += "NULL"
            else:
                sql += row['CS']
            sql += ","
            if row['BB'] == "":
                sql += "NULL"
            else:
                sql += row['BB']
            sql += ","
            if row['SO'] == "":
                sql += "NULL"
            else:
                sql += row['SO']
            sql += ","
            if row['IBB'] == "":
                sql += "NULL"
            else:
                sql += row['IBB']
            sql += ","
            if row['HBP'] == "":
                sql += "NULL"
            else:
                sql += row['HBP']
            sql += ","
            if row['SH'] == "":
                sql += "NULL"
            else:
                sql += row['SH']
            sql += ","
            if row['SF'] == "":
                sql += "NULL"
            else:
                sql += row['SF']
            sql += ","
            if row['GIDP'] == "":
                sql += "NULL"
            else:
                sql += row['GIDP']
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

def battingCSVUpdate():
    sql = "INSERT INTO batting (playerID, yearId, teamID, stint, b_G, b_AB, b_R, b_H, b_2B, b_3B, b_HR, b_RBI,b_SB,b_CS,"
    sql +=      "b_BB, b_SO, b_IBB, b_HBP, b_SH, b_SF, b_GIDP) VALUES"
    with open("Batting.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID']
            sql += ","
            sql += "'" + row['teamID'] + "',"
            if row['stint'] == "":
                sql += "NULL"
            else:
                sql += row['stint']
            sql += ","
            if row['G'] == "":
                sql += "NULL"
            else:
                sql += row['G']
            sql += ","
            if row['AB'] == "":
                sql += "NULL"
            else:
                sql += row['AB']
            sql += ","
            if row['R'] == "":
                sql += "NULL"
            else:
                sql += row['R']
            sql += ","
            if row['H'] == "":
                sql += "NULL"
            else:
                sql += row['H']
            sql += ","
            if row['2B'] == "":
                sql += "NULL"
            else:
                sql += row['2B']
            sql += ","
            if row['3B'] == "":
                sql += "NULL"
            else:
                sql += row['3B']
            sql += ","
            if row['HR'] == "":
                sql += "NULL"
            else:
                sql += row['HR']
            sql += ","
            if row['RBI'] == "":
                sql += "NULL"
            else:
                sql += row['RBI']
            sql += ","
            if row['SB'] == "":
                sql += "NULL"
            else:
                sql += row['SB']
            sql += ","
            if row['CS'] == "":
                sql += "NULL"
            else:
                sql += row['CS']
            sql += ","
            if row['BB'] == "":
                sql += "NULL"
            else:
                sql += row['BB']
            sql += ","
            if row['SO'] == "":
                sql += "NULL"
            else:
                sql += row['SO']
            sql += ","
            if row['IBB'] == "":
                sql += "NULL"
            else:
                sql += row['IBB']
            sql += ","
            if row['HBP'] == "":
                sql += "NULL"
            else:
                sql += row['HBP']
            sql += ","
            if row['SH'] == "":
                sql += "NULL"
            else:
                sql += row['SH']
            sql += ","
            if row['SF'] == "":
                sql += "NULL"
            else:
                sql += row['SF']
            sql += ","
            if row['GIDP'] == "":
                sql += "NULL"
            else:
                sql += row['GIDP']
            sql += "),"
    sql = sql[:-1] + ";"
    return sql

def appearancesCSVUpdate():
    sql = "INSERT INTO appearances (playerID, yearID, teamID, G_all, GS, G_batting, G_defense, G_p, G_c, G_1b,"
    sql += " G_2b, G_3b, G_ss, G_lf, G_cf, G_of, G_dh, G_ph, G_pr) VALUES "
    with open("Appearances.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
            sql += "("
            sql += "'" + row['playerID'] + "',"
            sql += row['yearID']
            sql += ","
            sql += "'" + row['teamID'] + "',"
            if row['G_all'] == "":
                sql += "NULL"
            else:
                sql += row['G_all']
            sql += ","
            if row['GS'] == "":
                sql += "NULL"
            else:
                sql += row['GS']
            sql += ","
            if row['G_batting'] == "":
                sql += "NULL"
            else:
                sql += row['G_batting']
            sql += ","
            if row['G_defense'] == "":
                sql += "NULL"
            else:
                sql += row['G_defense']
            sql += ","
            if row['G_p'] == "":
                sql += "NULL"
            else:
                sql += row['G_p']
            sql += ","
            if row['G_c'] == "":
                sql += "NULL"
            else:
                sql += row['G_c']
            sql += ","
            if row['G_1b'] == "":
                sql += "NULL"
            else:
                sql += row['G_1b']
            sql += ","
            if row['G_2b'] == "":
                sql += "NULL"
            else:
                sql += row['G_2b']
            sql += ","
            if row['G_3b'] == "":
                sql += "NULL"
            else:
                sql += row['G_3b']
            sql += ","
            if row['G_ss'] == "":
                sql += "NULL"
            else:
                sql += row['G_ss']
            sql += ","
            if row['G_lf'] == "":
                sql += "NULL"
            else:
                sql += row['G_lf']
            sql += ","
            if row['G_lf'] == "":
                sql += "NULL"
            else:
                sql += row['G_cf']
            sql += ","
            if row['G_of'] == "":
                sql += "NULL"
            else:
                sql += row['G_of']
            sql += ","
            if row['G_dh'] == "":
                sql += "NULL"
            else:
                sql += row['G_dh']
            sql += ","
            if row['G_ph'] == "":
                sql += "NULL"
            else:
                sql += row['G_ph']
            sql += ","
            if row['G_pr'] == "":
                sql += "NULL"
            else:
                sql += row['G_pr']
            sql += "),"
    sql = sql[:-1] + ";"
    return sql


con = pymysql.connect(host="localhost", user=cfg.mysql['user'], password=cfg.mysql['password'],
                      database="group3")

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

    finalSql = teamsCSVUpdate()
    cur.execute(finalSql)
    print("Teams table loaded")

    finalSql = salariesCSVUpdate()
    cur.execute(finalSql)
    print("Salary table loaded")

    finalSql = pitchingPostCSVUpdate()
    cur.execute(finalSql)
    print("PitchingPost table loaded")

    finalSql = pitchingCSVUpdate()
    cur.execute(finalSql)
    print("Pitching table loaded")

    finalSql = battingPostCSVUpdate()
    cur.execute(finalSql)
    print("BattingPost table loaded")

    finalSql = battingCSVUpdate()
    cur.execute(finalSql)
    print("Batting table loaded")

    finalSql = appearancesCSVUpdate()
    cur.execute(finalSql)
    print("Appearances table loaded")
except:
    con.rollback()
    print("Database exception")
    raise
else:
    con.commit()
finally:
    con.close()
