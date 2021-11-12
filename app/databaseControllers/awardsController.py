from app.baseballModels.people import People
from app.baseballModels.teams import Teams
from app.baseballModels.managers import Managers
from app.baseballModels.awardsmanagers import AwardsManagers
from app.baseballModels.awardsplayers import AwardsPlayers
from app.baseballModels.halloffame import HallofFame
from app.baseballModels.allstarfull import AllstarFull
from app.databaseControllers.generalController import createConnection


def getHallofFame(year):
    session = createConnection()
    stats = session.query(People, HallofFame) \
        .filter(People.playerid == HallofFame.playerid, HallofFame.inducted == 'Y', HallofFame.yearid == year)
    session.close()
    return stats


def getAllstar(team, year):
    session = createConnection()
    allstar = session.query(People, AllstarFull) \
        .filter(People.playerid == AllstarFull.playerid, Teams.name == team, Teams.yearID == AllstarFull.yearID,
                Teams.teamID == AllstarFull.teamID, AllstarFull.yearID == year)
    session.close()
    return allstar


def getPlayerAwards(year, award):
    session = createConnection()
    awards = session.query(People, AwardsPlayers) \
        .filter(People.playerid == AwardsPlayers.playerid, AwardsPlayers.yearID == year,
                AwardsPlayers.awardID == award).order_by(AwardsPlayers.lgID)
    session.close()
    return awards


def getManagerAward(team, awardtype):
    session = createConnection()
    tsnawards = session.query(AwardsManagers, Managers, People) \
        .filter(Managers.playerid == AwardsManagers.playerID, Managers.yearID == AwardsManagers.yearID,
                People.playerid == Managers.playerid,
                Managers.teamID == Teams.teamID, Managers.yearID == Teams.yearID, Teams.name == team,
                AwardsManagers.awardID == awardtype) \
        .order_by(Managers.yearID.desc())
    session.close()
    return tsnawards
