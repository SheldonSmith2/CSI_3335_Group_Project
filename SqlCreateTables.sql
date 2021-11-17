/*  File: SqlCreateTables
    Purpose: To create the tables for information to be saved in.
                Does not add any rows, only the tables

 */

-- creates new database
CREATE DATABASE NewBaseball IF NOT EXISTS;

--drop tables in order to start fresh
DROP TABLE People IF EXISTS;
DROP TABLE Team IF EXISTS;
DROP TABLE Awards IF EXISTS;
DROP TABLE AwardsShare IF EXISTS;
DROP TABLE AllStarFull IF EXISTS;
DROP TABLE LeagueDivisions IF EXISTS;
DROP TABLE HallOfFame IF EXISTS;
DROP TABLE Franchise IF EXISTS;
DROP TABLE School IF EXISTS;
DROP TABLE Manager IF EXISTS;
DROP TABLE Salary IF EXISTS;
DROP TABLE Batting IF EXISTS;
DROP TABLE BattingPost IF EXISTS;
DROP TABLE Pitching IF EXISTS;
DROP TABLE PitchingPost IF EXISTS;
DROP TABLE Fielding IF EXISTS;
DROP TABLE FieldingPost IF EXISTS;
DROP TABLE Appearances IF EXISTS;
DROP TABLE SeriesPost IF EXISTS;
DROP TABLE HomeGames IF EXISTS;
DROP TABLE Park IF EXISTS;

--create the people table with personal information about the person
--PK: playerID
CREATE TABLE People (playerID varchar(9) NOT NULL, birthYear int(12), birthMonth int(12), birthDay int(12),
 birthCountry varchar(255), birthState varchar(255), birthCity varchar(255), deathYear int(12), deathMonth int(12),
 deathDay int(12), deathCountry varchar(255), deathState varchar(255), deathCity varchar(255), nameFirst varchar(255),
 nameLast varchar(255), nameGiven varchar(255), weight int(10), height int(10), bats varchar(255), throws varchar(255),
 debutDate date, finalGameDate date, CONSTRAINT pk_people PRIMARY KEY (playerID));

--create the teams table with information about the team in a year
--PK: ID, FK: lgID, divID, franchID
CREATE TABLE Team (ID INT(12) NOT NULL AUTO_INCREMENT, teamID CHAR(3) NOT NULL, yearID smallint(6) NOT NULL, lgID char(2),
    divID char(1), franchID varchar(3), team_name VARCHAR(50), teamRank smallint(6), G smallint(6), G_home smallint(6),
    W smallint(6), L smallint(6), DivWin varchar(1), WCWin varchar(1), LgWin varchar(1), WSWin varchar(1), R smallint(6),
    AB smallint(6), H smallint(6), team_2B smallint(6), team_3B smallint(6), team_HR smallint(6), team_BB smallint(6),
    team_SO smallint(6), team_SB smallint(6), team_CS smallint(6), team_HBP smallint(6), team_SF smallint(6),
    team_RA smallint(6), team_ER smallint(6), team_ERA double, team_CG smallint(6), team_SHO smallint(6),
    team_SV smallint(6), team_IPouts int(11), team_HA smallint(6), team_HRA smallint(6), team_BBA smallint(6), team_SOA smallint(6),
    CONSTRAINT pk_team PRIMARY KEY (ID), CONSTRAINT fk_league FOREIGN KEY (lgID, divID) REFERENCES LeagueDivisions(lgID, divID),
    CONSTRAINT fk_franch FOREIGN KEY (franchID) REFERENCES Franchise(franchID));

--create the hallOfFame table with information about the members of the hall of fame
--PK: ID, FK: playerID
CREATE TABLE hallOfFame (ID INT(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, votedBy varchar(64) NOT NULL,
    ballots smallint(6), needed smallint(6), votes smallint(6), inducted varchar(1), category varchar(20), note varchar(25),
    CONSTRAINT pk_hof PRIMARY KEY (ID), CONSTRAINT fk_people FOREIGN KEY (playerID) REFERENCES People(playerID));

--create the league/division table. This is the combination all leagues and divisions
-- PK: lgID, divID
CREATE TABLE LeagueDivision (lgID char(2) NOT NULL, divID char(2) NOT NULL, leagueName varchar(50) NOT NULL,
    divisionName varchar(50) NOT NULL, active char(1), CONSTRAINT pk_league PRIMARY KEY (lgID, divID));

--create the franchise table with information about the franchise
--PK: franchID
CREATE TABLE franchises (franchID varchar(3) NOT NULL, franchName varchar(50), active char(1), NAassoc varchar(3),
    CONSTRAINT pk_franch PRIMARY KEY (franchID));

--create the school table that hold the information the schools players attended
--PK: schoolID
CREATE TABLE school (schoolId varchar(15) NOT NULL, name varchar(255), city varchar(55), state varchar(55),
    country varchar(55), CONSTRAINT pk_school PRIMARY KEY (schoolId));

--create the park table with information about the parks
--PK: ID
CREATE TABLE park (ID int(12) NOT NULL AUTO_INCREMENT, parkID varchar(255) NOT NULL, park_alias varchar(255), park_name
    varchar(255), city varchar(255), state varchar(255), country varchar(255), CONSTRAINT pk_park PRIMARY KEY (ID));

--create manager table that hold specialized information about managers inherits from people
--PK: ID, FK: playerID
CREATE TABLE manager (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearID smallint(6) NOT NULL,
    inSeason smallint(6) NOT NULL, manager_G smallint(6), manager_W smallint(6), manager_L smallint(6), teamRank
    smallint(6), plyrMgr varchar(1), CONSTRAINT pk_man PRIMARY KEY (ID), CONSTRAINT fk_man_person FOREIGN KEY (playerID)
    REFERENCES People(playerID));

--create awards table that hold information for both players and managers
--PK: ID, FK: playerID, lgID, divID
CREATE TABLE awards (ID int(12) NOT NULL AUTO_INCREMENT, awardID varchar(255) NOT NULL, yearID smallint(6) NOT NULL,
    playerID varchar(9) NOT NULL, lgID char(2) NOT NULL, divID char(2) NOT NULL, tie varchar(1), notes varchar(100),
    CONSTRAINT pk_awd PRIMARY KEY (ID), CONSTRAINT fk_awd_peo FOREIGN KEY (playerID) REFERENCES People(playerID),
    CONSTRAINT fk_awd_lg FOREIGN KEY (lgID, divID) REFERENCES LeagueDivision(lgID, divID));

--creates the shared awards table that holds information about everyone nominated for an award
--PK: ID, FK: playerID, lgID, divID
CREATE TABLE awardsShare (ID int(12) NOT NULL AUTO_INCREMENT, awardID varchar(255) NOT NULL, yearID smallInt(6) NOT NULL,
    playerID varchar(9) NOT NULL, lgID char(2) NOT NULL, divID char(2) NOT NULL, pointsWon double, pointsMax smallint,
    votesFirst double, CONSTRAINT pk_awdshr PRIMARY KEY (ID), CONSTRAINT fk_awdshr_peo FOREIGN KEY (playerID) REFERENCES People(playerID),
    CONSTRAINT fk_awdshr_lg FOREIGN KEY (lgID, divID) REFERENCES LeagueDivision(lgID, divID));

--creates the allstarfull table that holds information about all-star game players
--PK: ID, FK: playerID, lgID, divID
CREATE TABLE allStarFull (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, lgID char(2) NOT NULL, divID
    char(2) NOT NULL, yearID smallint(6) NOT NULL, gameNum smallint(6), gameID varchar(12), GP smallint(6), startingPos
    smallint(6), CONSTRAINT pk_allstar PRIMARY KEY (ID), CONSTRAINT fk_allstar_peo FOREIGN KEY (playerID) REFERENCES People(playerID),
    CONSTRAINT fk_allstar_lg FOREIGN KEY (lgID, divID) REFERENCES LeagueDivision(lgID, divID));

--creates the salary table that holds salary information for players, teams, and leagues
--PK: ID, FK: playerID, teamID, lgID, divID
CREATE TABLE salary (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, teamId char(3) NOT NULL,
    lgId char(2) NOT NULL, divId char(2) NOT NULL, yearId smallint(6) NOT NULL, salary double, CONSTRAINT
    pk_salary PRIMARY KEY (ID), CONSTRAINT fk_sal_peo FOREIGN KEY (playerID) REFERENCES People(playerID),
    CONSTRAINT fk_sal_team FOREIGN KEY (teamId) REFERENCES Team(teamID), CONSTRAINT fk_sal_lg FOREIGN KEY
    (lgID, divId) REFERENCES LeagueDivision(lgID, divID));

--create the batting table that holds data for batters during a stint
--PK: ID, FK: playerID, teamID
CREATE TABLE batting (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearId smallint(6) NOT NULL,
    teamId char(3) NOT NULL, stint smallint(4) NOT NULL, b_G smallint(6), b_AB smallint(6), b_R smallint(6), b_H smallint(6),
    b_2B smallint(6), b_3B smallint(6), b_HR smallint(6), b_RBI smallint(6), b_SB smallint(6), b_CS smallint(6), b_BB smallint(6),
    b_SO smallint(6), b_IBB smallint(6), b_HBP smallint(6), b_SH smallint(6), b_SF smallint(6), b_GIDP smallint(6),
    CONSTRAINT pk_batting PRIMARY KEY (ID), CONSTRAINT fk_bat_peo FOREIGN KEY (playerID) REFERENCES People(playerID),
    CONSTRAINT fk_bat_team FOREIGN KEY (teamId) REFERENCES Team(teamID));

--create the pitching table that holds data for pitchers during a stint
--PK: ID, FK: playerID, teamID
CREATE TABLE pitching (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearID smallint(6) NOT NULL,
    teamID char(3) NOT NULL, stint smallint(4) NOT NULL, p_W smallint(6), p_L smallint(6), p_G smallint(6), p_GS smallint(6),
    p_CG smallint(6), p_SHO smallint(6), p_SV smallint(6), p_IPOuts int(11), p_H smallint(6), p_ER smallint(6),
    p_HR smallint(6), p_BB smallint(6), p_SO smallint(6), p_BAOpp double, p_ERA double, p_IBB smallint(6), p_WP smallint(6),
    p_HBP smallint(6), p_BK smallint(6), p_BFP smallint(6), p_GF smallint(6), p_R smallint(6), p_SH smallint(6),
    p_SF smallint(6), p_GIDP smallint(6), CONSTRAINT pk_pitch PRIMARY KEY (ID), CONSTRAINT fk_pitch_peo FOREIGN KEY (playerID)
    REFERENCES People(playerID), CONSTRAINT fk_pitch_team FOREIGN KEY (teamID) REFERENCES Team(teamID));

--creates the fielding table that holds data for fielders during a stint
--PK: ID, FK: playerID, teamID
CREATE TABLE fielding (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearID smallint(6) NOT NULL,
    teamID char(3) NOT NULL, stint smallint(4) NOT NULL, position varchar(2), f_G smallint(6), f_GS smallint(6),
    f_InnOuts smallint(6), f_PO smallint(6), f_A smallint(6), f_E smallint(6), f_DP smallint(6), f_PB smallint(6),
    f_WP smallint(6), f_SB smallint(6), f_CS smallint(6), f_ZR double, CONSTRAINT pk_field PRIMARY KEY (ID),
    CONSTRAINT fk_field_peo FOREIGN KEY (playerID) REFERENCES People(playerID), CONSTRAINT fk_field_team
    FOREIGN KEY (teamID) REFERENCES Team(teamID));

--creates the appearances table which tracks the number of times a player has been in each position
--PK: ID, FK: playerID, teamID
CREATE TABLE appearances (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearID smallint(6) NOT NULL,
    teamId char(3) NOT NULL, G_all smallint(6), GS smallint(6), G_batting smallint(6), G_defense smallint(6), G_p smallint(6),
    G_c smallint(6), G_1b smallint(6), G_2b smallint(6), G_3b smallint(6), G_ss smallint(6), G_lf smallint(6), G_cf smallint(6),
    G_of smallint(6), G_dh smallint(6), G_ph smallint(6), G_pr smallint(6), CONSTRAINT pk_appe PRIMARY KEY (ID),
    CONSTRAINT fk_appe_peo FOREIGN KEY (playerID) REFERENCES People(playerID), CONSTRAINT fk_appe_team FOREIGN KEY (teamId)
    REFERENCES Team(teamID));

--creates the batting Post-season table which tracks the batting data for the post-season
--PK: ID, FK: playerID, teamID
CREATE TABLE battingPost (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearId smallint(6) NOT NULL,
    teamId char(3) NOT NULL, round varchar(10) NOT NULL, b_G smallint(6), b_AB smallint(6), b_R smallint(6), b_H smallint(6),
    b_2B smallint(6), b_3B smallint(6), b_HR smallint(6), b_RBI smallint(6), b_SB smallint(6), b_CS smallint(6), b_BB smallint(6),
    b_SO smallint(6), b_IBB smallint(6), b_HBP smallint(6), b_SH smallint(6), b_SF smallint(6), b_GIDP smallint(6),
    CONSTRAINT pk_batting PRIMARY KEY (ID), CONSTRAINT fk_bat_peo FOREIGN KEY (playerID) REFERENCES People(playerID),
    CONSTRAINT fk_bat_team FOREIGN KEY (teamId) REFERENCES Team(teamID));

--creates the pitching post-season table which tracks the pitching data for the post-season
--PK: ID, FK: playerID, teamID
CREATE TABLE pitchingPost (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearID smallint(6) NOT NULL,
    teamID char(3) NOT NULL, round varchar(10) NOT NULL, p_W smallint(6), p_L smallint(6), p_G smallint(6), p_GS smallint(6),
    p_CG smallint(6), p_SHO smallint(6), p_SV smallint(6), p_IPOuts int(11), p_H smallint(6), p_ER smallint(6),
    p_HR smallint(6), p_BB smallint(6), p_SO smallint(6), p_BAOpp double, p_ERA double, p_IBB smallint(6), p_WP smallint(6),
    p_HBP smallint(6), p_BK smallint(6), p_BFP smallint(6), p_GF smallint(6), p_R smallint(6), p_SH smallint(6),
    p_SF smallint(6), p_GIDP smallint(6), CONSTRAINT pk_pitch PRIMARY KEY (ID), CONSTRAINT fk_pitch_peo FOREIGN KEY (playerID)
    REFERENCES People(playerID), CONSTRAINT fk_pitch_team FOREIGN KEY (teamID) REFERENCES Team(teamID));

--creates the fielding post-season table which tracks the fielding data for the post-season
--PK: ID, FK: playerID, teamID
CREATE TABLE fieldingPost (ID int(12) NOT NULL AUTO_INCREMENT, playerID varchar(9) NOT NULL, yearID smallint(6) NOT NULL,
    teamID char(3) NOT NULL, round varchar(10) NOT NULL, position varchar(2), f_G smallint(6), f_GS smallint(6),
    f_InnOuts smallint(6), f_PO smallint(6), f_A smallint(6), f_E smallint(6), f_DP smallint(6), f_PB smallint(6),
    f_WP smallint(6), f_SB smallint(6), f_CS smallint(6), f_ZR double, CONSTRAINT pk_field PRIMARY KEY (ID),
    CONSTRAINT fk_field_peo FOREIGN KEY (playerID) REFERENCES People(playerID), CONSTRAINT fk_field_team
    FOREIGN KEY (teamID) REFERENCES Team(teamID));

--creates the seriesPost table that tracks teams wins in a series
--PK: ID, FK: teamIDWinner (teamID), teamIDLosser (teamID)
CREATE TABLE seriesPost (ID int(12) NOT NULL AUTO_INCREMENT, teamIDwinner char(3) NOT NULL, teamIDloser char(3) NOT NULL,
    yearID smallint(6) NOT NULL, round varchar(5) NOT NULL, wins smallint(6), loses smallint(6), ties smallint(6),
    CONSTRAINT pk_sp PRIMARY KEY (ID), CONSTRAINT fk_sp_tw FOREIGN KEY (teamIDwinner) REFERENCES Team(teamID),
    CONSTRAINT fk_sp_tl FOREIGN  KEY (teamIDloser) REFERENCES Team(teamID));

--creates the home games tables that holds information about the park and its relation to the team
--PK: ID, FK: teamID, parkID
CREATE TABLE homeGames (ID int(12) NOT NULL AUTO_INCREMENT, teamID char(3) NOT NULL, parkID varchar(255) NOT NULL,
    yearID smallint(6) NOT NULL, firstGame date, lastGame date, games int(11), openings int(11), attendence int(11),
    CONSTRAINT pk_hg PRIMARY KEY (ID), CONSTRAINT fk_hg_team FOREIGN KEY (teamID) REFERENCES Team(teamID),
    CONSTRAINT fk_hg_park FOREIGN KEY (parkID) REFERENCES park(parkID));


describe People;
describe Team;
describe awards;
describe awardsShare;
describe allStarFull;
describe LeagueDivision;
describe salary;
describe hallOfFame;
describe school;
describe franchises;
describe batting;
describe pitching;
describe fielding;
describe manager;
describe battingPost;
describe pitchingPost;
describe fieldingPost;
describe appearances;
describe park;
describe seriesPost;
describe homeGames;