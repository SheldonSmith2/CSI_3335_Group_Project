from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
import app.baseballModels.dbconfig as cfg
from app.baseballModels.people import People
from app.baseballModels.batting import Batting
from app.baseballModels.teams import Teams
from app.baseballModels.salaries import Salaries
from app.baseballModels.managers import Managers
from app.baseballModels.fielding import Fielding
from app.baseballModels.appearances import Appearances


def createConnection():
    enginestr = "mysql+pymysql://" + cfg.mysql['user'] + ":" + cfg.mysql['password'] + "@" + cfg.mysql[
        'host'] + ":3306/" + cfg.mysql['db']

    engine = create_engine(enginestr)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def getRoster(team, year):
    session = createConnection()
    players = session.query(People, Batting, Teams).distinct(People.playerid) \
        .filter(People.playerid == Batting.playerid, Teams.teamID == Batting.teamID, Teams.yearID == Batting.yearID,
                Teams.name == team, Batting.yearID == year).order_by(People.playerid).all()
    session.close()
    return players


def getAppearances(team, year):
    session = createConnection()
    players = session.query(Appearances).distinct(People.playerid) \
        .filter(People.playerid == Appearances.playerid, Teams.teamID == Appearances.teamID,
                Teams.yearID == Appearances.yearID,
                Teams.name == team, Appearances.yearID == year).order_by(People.playerid).all()
    session.close()
    return players


def getManagers(team):
    session = createConnection()
    managers = session.query(Managers, func.max(Managers.yearID), func.min(Managers.yearID), func.sum(Managers.W),
                             People, func.sum(Managers.G)) \
        .filter(Managers.teamID == Teams.teamID, Teams.name == team, People.playerid == Managers.playerid) \
        .group_by(Managers.playerid).order_by(func.max(Managers.yearID).desc()).limit(10).all()
    session.close()
    return managers


def getTopSalaries(year):
    session = createConnection()
    salaries = session.query(People, Salaries, Teams, Fielding) \
        .filter(Salaries.playerid == People.playerid, Salaries.yearID == year, Teams.yearID == Salaries.yearID,
                Teams.teamID == Salaries.teamID, Fielding.teamID == Teams.teamID, Teams.yearID == Fielding.yearID,
                Fielding.playerid == Salaries.playerid, Fielding.G > 10) \
        .order_by(Salaries.salary.desc()).limit(10).all()
    session.close()
    return salaries


def getStats(plyr_id, year, team):
    session = createConnection()
    stats = session.query(Batting, People.nameFirst, People.nameLast) \
        .filter(Batting.yearID == year, Batting.playerid == plyr_id, Batting.teamID == Teams.teamID,
                Batting.yearID == Teams.yearID,
                Teams.name == team, Batting.playerid == People.playerid).limit(1)
    session.close()
    return stats
