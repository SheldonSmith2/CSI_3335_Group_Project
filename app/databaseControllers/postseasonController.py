from sqlalchemy.orm import aliased
from sqlalchemy import func
from app.baseballModels.teams import Teams
from app.baseballModels.seriespostseason import SeriesPost
from app.databaseControllers.generalController import createConnection


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


def getWSWins(team):
    session = createConnection()
    count = session.query(func.count(Teams.WSWin)) \
        .filter(Teams.name == team, Teams.WSWin == 'Y')
    session.close()
    return count


def getDivWins(team):
    session = createConnection()
    count = session.query(func.count(Teams.DivWin)) \
        .filter(Teams.name == team, Teams.DivWin == 'Y')
    session.close()
    return count


def getLgWins(team):
    session = createConnection()
    count = session.query(func.count(Teams.LgWin)) \
        .filter(Teams.name == team, Teams.LgWin == 'Y')
    session.close()
    return count


def getWSWinInfo(team):
    session = createConnection()
    teamWin = aliased(Teams)
    teamLoss = aliased(Teams)
    roundResults = session.query(SeriesPost, teamLoss) \
        .filter(SeriesPost.round == "WS", SeriesPost.teamIDwinner == teamWin.teamID,
                SeriesPost.teamIDloser == teamLoss.teamID, SeriesPost.yearID == teamWin.yearID,
                SeriesPost.yearID == teamLoss.yearID, teamWin.name == team).order_by(SeriesPost.yearID.desc())
    session.close()
    return roundResults
