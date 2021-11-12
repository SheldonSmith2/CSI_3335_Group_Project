from app.baseballModels.people import People
from app.baseballModels.batting import Batting
from app.baseballModels.pitching import Pitching
from app.databaseControllers.generalController import createConnection


def getHighestHR():
    session = createConnection()
    topHR = session.query(People.nameFirst, People.nameLast, Batting.HR) \
        .filter(Batting.yearID == 2019, People.playerid == Batting.playerid) \
        .order_by(Batting.HR.desc())
    session.close()
    return topHR


def getHighestBA():
    session = createConnection()
    topBA = session.query(People.nameFirst, People.nameLast, Batting.H, Batting.AB) \
        .filter(Batting.yearID == 2019, People.playerid == Batting.playerid, Batting.AB > 100) \
        .order_by(Batting.H / Batting.AB.desc())
    session.close()
    return topBA


def getHighestRBI():
    session = createConnection()
    topRBI = session.query(People.nameFirst, People.nameLast, Batting.RBI) \
        .filter(Batting.yearID == 2019, People.playerid == Batting.playerid) \
        .order_by(Batting.RBI.desc())
    session.close()
    return topRBI


def getHighestWins():
    session = createConnection()
    topWins = session.query(People.nameFirst, People.nameLast, Pitching.W) \
        .filter(Pitching.yearID == 2019, People.playerid == Pitching.playerid) \
        .order_by(Pitching.W.desc())
    session.close()
    return topWins


def getHighestSO():
    session = createConnection()
    topSO = session.query(People.nameFirst, People.nameLast, Pitching.SO) \
        .filter(Pitching.yearID == 2019, People.playerid == Pitching.playerid) \
        .order_by(Pitching.SO.desc())
    session.close()
    return topSO


def getHighestERA():
    session = createConnection()
    topERA = session.query(People.nameFirst, People.nameLast, Pitching.ER, Pitching.IPouts) \
        .filter(Pitching.yearID == 2019, People.playerid == Pitching.playerid, Pitching.IPouts / 3 > 100) \
        .order_by(27 * Pitching.ER / Pitching.IPouts)
    session.close()
    return topERA
