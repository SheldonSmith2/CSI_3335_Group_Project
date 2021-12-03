from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
import app.baseballModels.mariadbconfig as cfg
from app.baseballModels.people import People
from app.baseballModels.batting import Batting
from app.baseballModels.teams import Teams
from app.baseballModels.salaries import Salaries
from app.baseballModels.managers import Managers
from app.baseballModels.fielding import Fielding
from app.baseballModels.appearances import Appearances
from app.baseballModels.pitching import Pitching


# Create a connection to the database
def createConnection():
    enginestr = "mysql+pymysql://" + cfg.mysql['user'] + ":" + cfg.mysql['password'] + "@localhost:3306/group3"

    engine = create_engine(enginestr)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


# The function to get the roster of the given team based on the year
def getRoster(team, year):
    session = createConnection()
    players = session.query(People, Batting, Teams).distinct(People.playerID) \
        .filter(People.playerID == Batting.playerID, Teams.teamID == Batting.teamID, Teams.yearID == Batting.yearId,
                Teams.name == team, Batting.yearId == year).order_by(People.playerID).all()
    session.close()
    return players


# The function to get the appearances of players on the given team in the year
def getAppearances(team, year):
    session = createConnection()
    players = session.query(Appearances).distinct(People.playerID) \
        .filter(People.playerID == Appearances.playerID, Teams.teamID == Appearances.teamId,
                Teams.yearID == Appearances.yearID,
                Teams.name == team, Appearances.yearID == year).order_by(People.playerID).all()
    session.close()
    return players


# The function to get the last 10 managers for a specific team
def getManagers(team):
    session = createConnection()
    managers = session.query(Managers, func.max(Managers.yearID), func.min(Managers.yearID), func.sum(Managers.manager_W),
                             People, func.sum(Managers.manager_G)) \
        .filter(Managers.teamID == Teams.teamID, Teams.name == team, People.playerID == Managers.playerID) \
        .group_by(Managers.playerID).order_by(func.max(Managers.yearID).desc()).limit(10).all()
    session.close()
    return managers


# The function to get the top 10 salaries of a given year
def getTopSalaries(year):
    session = createConnection()
    salaries = session.query(People, Salaries, Teams, Fielding) \
        .filter(Salaries.playerID == People.playerID, Salaries.yearId == year, Teams.yearID == Salaries.yearId,
                Teams.teamID == Salaries.teamID, Fielding.teamID == Teams.teamID, Teams.yearID == Fielding.yearID,
                Fielding.playerID == Salaries.playerID, Fielding.f_G > 10) \
        .order_by(Salaries.salary.desc()).limit(10).all()
    session.close()
    return salaries


# The function to get the states of a player based on the playerid, year, and team
def getStats(plyr_id, year, team):
    session = createConnection()
    stats = session.query(Batting, People.nameFirst, People.nameLast) \
        .filter(Batting.yearId == year, Batting.playerID == plyr_id, Batting.teamID == Teams.teamID,
                Batting.yearId == Teams.yearID,
                Teams.name == team, Batting.playerID == People.playerID).limit(1)
    session.close()
    return stats


# The function to get the pitching information for a team and year
def getPitchingInfo(team, year):
    session = createConnection()
    players = session.query(Pitching) \
        .filter(Pitching.yearID == year, Pitching.teamID == Teams.teamID, Teams.name == team) \
        .order_by(Pitching.playerID).all()
    session.close()
    return players


# The function the get all the player names
def getPlayers():
    session = createConnection()
    players = session.query(People).distinct(People.playerID)
    return players
