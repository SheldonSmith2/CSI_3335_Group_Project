from app.baseballModels.teams import Teams
from app.databaseControllers.generalController import createConnection


def getStandings(year, league, division):
    session = createConnection()
    teams = session.query(Teams) \
        .filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).all()
    session.close()
    return teams


def getCurrentTeams():
    session = createConnection()
    teams = session.query(Teams.name) \
        .filter(Teams.yearID == 2019) \
        .order_by(Teams.name)
    session.close()
    return teams


def getWLofDivision(year, league, division):
    session = createConnection()
    topTeam = session.query(Teams) \
        .filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).limit(1)
    session.close()
    return topTeam
