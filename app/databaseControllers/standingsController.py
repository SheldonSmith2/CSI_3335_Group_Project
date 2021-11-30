from app.baseballModels.teams import Teams
from app.databaseControllers.generalController import createConnection


# The function to get the division standings of a given year and league
def getStandings(year, league, division):
    session = createConnection()
    teams = session.query(Teams) \
        .filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).all()
    session.close()
    return teams


# The function to get the current teams in the MLB
def getCurrentTeams():
    session = createConnection()
    teams = session.query(Teams.name) \
        .filter(Teams.yearID == 2019) \
        .order_by(Teams.name)
    session.close()
    return teams


# The function to get the top team of the division
def getWLofDivision(year, league, division):
    session = createConnection()
    topTeam = session.query(Teams) \
        .filter(Teams.lgID == league, Teams.divID == division, Teams.yearID == year).order_by(Teams.W.desc()).limit(1)
    session.close()
    return topTeam
