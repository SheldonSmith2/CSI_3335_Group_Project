import csv
def pitchingCSVUpdate():
    sql = "INSERT INTO salary(playerID,yearId,teamID,stint, p_W, p_L, p_G,p_GS, p_CG, p_SHO, p_IPOuts, p_H, p_ER, p_HR,"
    sql += "p_BB, p_SO, p_BAOpp, p_ERA, p_IBB, p_WP, p_ HBP, p_BK, p_BFP, p_GF, p_R, p_SH, p_SF, p_GIDP) VALUES"
    with open("Pitching.csv", mode='r') as csvfile:
        teamsreader = csv.DictReader(csvfile)
        for row in teamsreader:
                sql = "("
                if row['playerID'] == "":
                    sql += "NULL"
                else:
                    sql += "'" + row['playerID'] + "'"
                sql += ","
                if row['yearID'] == "":
                    sql += "NULL"
                else:
                    sql += row['yearID']
                sql += ","
                if row['teamID'] == "":
                    sql += "NULL"
                else:
                    sql += "'" + row['teamID'] + "'"
                sql += ","
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
                sql += "), "
    sql = sql[:-2] + ";"
    return sql