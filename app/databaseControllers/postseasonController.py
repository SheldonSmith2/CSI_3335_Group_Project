from sqlalchemy.orm import aliased
from sqlalchemy import func
from app.baseballModels.teams import Teams
from app.baseballModels.seriespostseason import SeriesPost
from app.databaseControllers.generalController import createConnection


# The function to get the postseason round information for a specific year
def getRound(year, rd):
    session = createConnection()
    teamWin = aliased(Teams)
    teamLoss = aliased(Teams)
    roundResults = session.query(SeriesPost, teamWin, teamLoss) \
        .filter(SeriesPost.yearID == year, SeriesPost.round == rd, SeriesPost.teamIDwinner == teamWin.teamID,
                SeriesPost.teamIDloser == teamLoss.teamID, SeriesPost.yearID == teamWin.yearID,
                SeriesPost.yearID == teamLoss.yearID)
    session.close()
    return roundResults


# The function to get number of world series wins for given team
def getWSWins(team):
    session = createConnection()
    count = session.query(func.count(Teams.WSWin)) \
        .filter(Teams.name == team, Teams.WSWin == 'Y')
    session.close()
    return count


# The function to get number of division wins for given team
def getDivWins(team):
    session = createConnection()
    count = session.query(func.count(Teams.DivWin)) \
        .filter(Teams.name == team, Teams.DivWin == 'Y')
    session.close()
    return count


# The function to get number of league wins for given team
def getLgWins(team):
    session = createConnection()
    count = session.query(func.count(Teams.LgWin)) \
        .filter(Teams.name == team, Teams.LgWin == 'Y')
    session.close()
    return count


# The function to get postseason information for given team
def getPostInfo(team):
    session = createConnection()
    teamWin = aliased(Teams)
    teamLoss = aliased(Teams)
    roundResults = session.query(SeriesPost, teamLoss) \
        .filter(SeriesPost.teamIDwinner == teamWin.teamID,
                SeriesPost.teamIDloser == teamLoss.teamID, SeriesPost.yearID == teamWin.yearID,
                SeriesPost.yearID == teamLoss.yearID, teamWin.name == team, SeriesPost.yearID > 2015)\
        .order_by(SeriesPost.yearID.desc(), SeriesPost.round.desc())
    session.close()
    return roundResults
