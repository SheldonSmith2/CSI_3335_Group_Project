from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import create_engine, func, or_
import app.baseballModels.dbconfig as cfg
from app.baseballModels.people import People
from app.baseballModels.batting import Batting
from app.baseballModels.teams import Teams
from app.baseballModels.salaries import Salaries
from app.baseballModels.managers import Managers
from app.baseballModels.fielding import Fielding
from app.baseballModels.seriespostseason import SeriesPost
from app.baseballModels.awardsmanagers import AwardsManagers

def createConnection():
	enginestr = "mysql+pymysql://" +cfg.mysql['user']+":" +cfg.mysql['password']+"@" +cfg.mysql['host']+":3306/" +cfg.mysql['db']

	engine = create_engine(enginestr)

	Session = sessionmaker(bind=engine)
	session = Session()
	return session


def getRoster(team, year):
	session = createConnection()
	players = session.query(People, Batting, Teams)\
		.filter(People.playerid == Batting.playerid, Teams.teamID == Batting.teamID, Teams.yearID == Batting.yearID,
				Teams.name == team, Batting.yearID == year).order_by(People.nameLast).all()
	return players


def getStandings(year, league, division):
	session = createConnection()
	teams = session.query(Teams)\
		.filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).all()
	return teams

def getWLofDivision(year, league, division):
	session = createConnection()
	topTeam = session.query(Teams)\
		.filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).limit(1)
	return topTeam


def getManagers(team):
	session = createConnection()
	managers = session.query(Managers, func.max(Managers.yearID), func.min(Managers.yearID), func.sum(Managers.W),
							 People, func.sum(Managers.G))\
		.filter(Managers.teamID == Teams.teamID, Teams.name == team, People.playerid == Managers.playerid)\
		.group_by(Managers.playerid).order_by(func.max(Managers.yearID).desc()).limit(10).all()
	return managers


def getTopSalaries(year):
	session = createConnection()
	salaries = session.query(People, Salaries, Teams, Fielding)\
		.filter(Salaries.playerid == People.playerid, Salaries.yearID == year, Teams.yearID == Salaries.yearID,
				Teams.teamID == Salaries.teamID, Fielding.teamID == Teams.teamID, Teams.yearID == Fielding.yearID,
				Fielding.playerid == Salaries.playerid, Fielding.A > 10)\
		.order_by(Salaries.salary.desc()).limit(10).all()
	return salaries


def getTSNAwards(team):
	session = createConnection()
	tsnawards = session.query(AwardsManagers, Managers, People)\
		.filter(Managers.playerid == AwardsManagers.playerID, Managers.yearID == AwardsManagers.yearID, People.playerid == Managers.playerid,
				Managers.teamID == Teams.teamID, Managers.yearID == Teams.yearID, Teams.name == team,
				AwardsManagers.awardID == "TSN Manager of the Year")\
		.order_by(Managers.yearID.desc())
	return tsnawards


def getBBWAAawards(team):
	session = createConnection()
	bbwaaawards = session.query(AwardsManagers, Managers, People)\
		.filter(Managers.playerid == AwardsManagers.playerID, Managers.yearID == AwardsManagers.yearID, People.playerid == Managers.playerid,
				Managers.teamID == Teams.teamID, Managers.yearID == Teams.yearID, Teams.name == team,
				AwardsManagers.awardID == "BBWAA Manager of the Year")\
		.order_by(Managers.yearID.desc())
	return bbwaaawards


def getLatestWSChamp():
	session = createConnection()
	teamWin = aliased(Teams)
	teamLoss = aliased(Teams)
	wschamp = session.query(SeriesPost, teamWin, teamLoss).filter(SeriesPost.yearID == 2019, SeriesPost.round == "WS",
													SeriesPost.teamIDwinner == teamWin.teamID, SeriesPost.teamIDloser == teamLoss.teamID,
																SeriesPost.yearID == teamWin.yearID, SeriesPost.yearID == teamLoss.yearID)
	return wschamp


def getWSWins(team):
	session = createConnection()
	count = session.query(func.count(Teams.WSWin))\
		.filter(Teams.name == team, Teams.WSWin == 'Y')
	return count
