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
from app.baseballModels.awardsplayers import AwardsPlayers
from app.baseballModels.halloffame import HallofFame
from app.baseballModels.allstarfull import AllstarFull
from app.baseballModels.appearances import Appearances
from app.baseballModels.pitching import Pitching


def createConnection():
	enginestr = "mysql+pymysql://" +cfg.mysql['user']+":" +cfg.mysql['password']+"@" +cfg.mysql['host']+":3306/" +cfg.mysql['db']

	engine = create_engine(enginestr)

	Session = sessionmaker(bind=engine)
	session = Session()
	return session


def getRoster(team, year):
	session = createConnection()
	players = session.query(People, Batting, Teams).distinct(People.playerid)\
		.filter(People.playerid == Batting.playerid, Teams.teamID == Batting.teamID, Teams.yearID == Batting.yearID,
				Teams.name == team, Batting.yearID == year).order_by(People.playerid).all()
	session.close()
	return players

def getAppearances(team, year):
	session = createConnection()
	players = session.query(Appearances).distinct(People.playerid)\
		.filter(People.playerid == Appearances.playerid, Teams.teamID == Appearances.teamID, Teams.yearID == Appearances.yearID,
				Teams.name == team, Appearances.yearID == year).order_by(People.playerid).all()
	session.close()
	return players


def getStandings(year, league, division):
	session = createConnection()
	teams = session.query(Teams)\
		.filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).all()
	session.close()
	return teams

def getWLofDivision(year, league, division):
	session = createConnection()
	topTeam = session.query(Teams)\
		.filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).limit(1)
	session.close()
	return topTeam


def getManagers(team):
	session = createConnection()
	managers = session.query(Managers, func.max(Managers.yearID), func.min(Managers.yearID), func.sum(Managers.W),
							 People, func.sum(Managers.G))\
		.filter(Managers.teamID == Teams.teamID, Teams.name == team, People.playerid == Managers.playerid)\
		.group_by(Managers.playerid).order_by(func.max(Managers.yearID).desc()).limit(10).all()
	session.close()
	return managers


def getTopSalaries(year):
	session = createConnection()
	salaries = session.query(People, Salaries, Teams, Fielding)\
		.filter(Salaries.playerid == People.playerid, Salaries.yearID == year, Teams.yearID == Salaries.yearID,
				Teams.teamID == Salaries.teamID, Fielding.teamID == Teams.teamID, Teams.yearID == Fielding.yearID,
				Fielding.playerid == Salaries.playerid, Fielding.G > 10)\
		.order_by(Salaries.salary.desc()).limit(10).all()
	session.close()
	return salaries


def getManagerAward(team, type):
	session = createConnection()
	tsnawards = session.query(AwardsManagers, Managers, People)\
		.filter(Managers.playerid == AwardsManagers.playerID, Managers.yearID == AwardsManagers.yearID, People.playerid == Managers.playerid,
				Managers.teamID == Teams.teamID, Managers.yearID == Teams.yearID, Teams.name == team,
				AwardsManagers.awardID == type)\
		.order_by(Managers.yearID.desc())
	session.close()
	return tsnawards


def getRound(year, rd):
	session = createConnection()
	teamWin = aliased(Teams)
	teamLoss = aliased(Teams)
	roundResults = session.query(SeriesPost, teamWin, teamLoss)\
		.filter(SeriesPost.yearID == year, SeriesPost.round == rd, SeriesPost.teamIDwinner == teamWin.teamID,
				SeriesPost.teamIDloser == teamLoss.teamID, SeriesPost.yearID == teamWin.yearID, SeriesPost.yearID == teamLoss.yearID)
	session.close()
	return roundResults


def getWSWins(team):
	session = createConnection()
	count = session.query(func.count(Teams.WSWin))\
		.filter(Teams.name == team, Teams.WSWin == 'Y')
	session.close()
	return count


def getDivWins(team):
	session = createConnection()
	count = session.query(func.count(Teams.DivWin))\
		.filter(Teams.name == team, Teams.DivWin == 'Y')
	session.close()
	return count


def getLgWins(team):
	session = createConnection()
	count = session.query(func.count(Teams.LgWin))\
		.filter(Teams.name == team, Teams.LgWin == 'Y')
	session.close()
	return count


def getWSWinInfo(team):
	session = createConnection()
	teamWin = aliased(Teams)
	teamLoss = aliased(Teams)
	roundResults = session.query(SeriesPost, teamLoss)\
		.filter(SeriesPost.round == "WS", SeriesPost.teamIDwinner == teamWin.teamID,
				SeriesPost.teamIDloser == teamLoss.teamID, SeriesPost.yearID == teamWin.yearID,
				SeriesPost.yearID == teamLoss.yearID, teamWin.name == team).order_by(SeriesPost.yearID.desc())
	session.close()
	return roundResults


def getStats(plyr_id, year, team):
	session = createConnection()
	stats = session.query(Batting, People.nameFirst, People.nameLast)\
		.filter(Batting.yearID == year, Batting.playerid == plyr_id, Batting.teamID == Teams.teamID, Batting.yearID == Teams.yearID,
				Teams.name == team, Batting.playerid == People.playerid).limit(1)
	session.close()
	return stats


def getHallofFame(year):
	session = createConnection()
	stats = session.query(People, HallofFame)\
		.filter(People.playerid == HallofFame.playerid, HallofFame.inducted == 'Y', HallofFame.yearid == year)
	session.close()
	return stats


def getAllstar(team, year):
	session = createConnection()
	allstar = session.query(People, AllstarFull)\
		.filter(People.playerid == AllstarFull.playerid, Teams.name == team, Teams.yearID == AllstarFull.yearID,
				Teams.teamID == AllstarFull.teamID, AllstarFull.yearID == year)
	session.close()
	return allstar


def getPlayerAwards(year, award):
	session = createConnection()
	awards = session.query(People, AwardsPlayers)\
		.filter(People.playerid == AwardsPlayers.playerid, AwardsPlayers.yearID == year, AwardsPlayers.awardID == award)\
		.order_by(AwardsPlayers.lgID)
	session.close()
	return awards


def getCurrentTeams():
	session = createConnection()
	teams = session.query(Teams.name)\
		.filter(Teams.yearID == 2019)\
		.order_by(Teams.name)
	session.close()
	return teams


def getHighestHR():
	session = createConnection()
	topHR = session.query(People.nameFirst, People.nameLast, Batting.HR)\
		.filter(Batting.yearID == 2019, People.playerid == Batting.playerid)\
		.order_by(Batting.HR.desc())
	session.close()
	return topHR


def getHighestBA():
	session = createConnection()
	topBA = session.query(People.nameFirst, People.nameLast, Batting.H, Batting.AB)\
		.filter(Batting.yearID == 2019, People.playerid == Batting.playerid, Batting.AB > 100)\
		.order_by(Batting.H/Batting.AB.desc())
	session.close()
	return topBA


def getHighestRBI():
	session = createConnection()
	topRBI = session.query(People.nameFirst, People.nameLast, Batting.RBI)\
		.filter(Batting.yearID == 2019, People.playerid == Batting.playerid)\
		.order_by(Batting.RBI.desc())
	session.close()
	return topRBI


def getHighestWins():
	session = createConnection()
	topWins = session.query(People.nameFirst, People.nameLast, Pitching.W)\
		.filter(Pitching.yearID == 2019, People.playerid == Pitching.playerid)\
		.order_by(Pitching.W.desc())
	session.close()
	return topWins


def getHighestSO():
	session = createConnection()
	topSO = session.query(People.nameFirst, People.nameLast, Pitching.SO)\
		.filter(Pitching.yearID == 2019, People.playerid == Pitching.playerid)\
		.order_by(Pitching.SO.desc())
	session.close()
	return topSO


def getHighestERA():
	session = createConnection()
	topERA = session.query(People.nameFirst, People.nameLast, Pitching.ER, Pitching.IPouts)\
		.filter(Pitching.yearID == 2019, People.playerid == Pitching.playerid, Pitching.IPouts/3 > 100)\
		.order_by(27*Pitching.ER/Pitching.IPouts)
	session.close()
	return topERA
