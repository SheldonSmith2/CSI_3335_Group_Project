from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import app.baseballModels.dbconfig as cfg
from app.baseballModels.people import People
from app.baseballModels.batting import Batting
from app.baseballModels.teams import Teams


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
