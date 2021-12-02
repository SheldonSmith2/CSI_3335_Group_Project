from app.baseballModels.people import People
from app.baseballModels.teams import Teams
from app.baseballModels.managers import Managers
from app.baseballModels.awardsmanagers import AwardsManagers # Remove
from app.baseballModels.awardsplayers import AwardsPlayers # Remove
from app.baseballModels.halloffame import HallofFame
from app.baseballModels.allstarfull import AllstarFull
from app.databaseControllers.generalController import createConnection
# from app.baseballModels.awards import Awards


# The function to get all the hall of fame inductees from the given year
def getHallofFame(year):
    session = createConnection()
    stats = session.query(People, HallofFame) \
        .filter(People.playerid == HallofFame.playerid, HallofFame.inducted == 'Y', HallofFame.yearid == year)
    #stats = session.query(People, HallofFame) \
    #    .filter(People.playerID == HallofFame.playerID, HallofFame.inducted == 'Y', HallofFame.yearID == year)
    session.close()
    return stats


# The function to get all the allstar players based on the given year and team
def getAllstar(team, year):
    session = createConnection()
    allstar = session.query(People, AllstarFull) \
        .filter(People.playerid == AllstarFull.playerid, Teams.name == team, Teams.yearID == AllstarFull.yearID,
                Teams.teamID == AllstarFull.teamID, AllstarFull.yearID == year)
    #allstar = session.query(People, AllstarFull) \
    #    .filter(People.playerID == AllstarFull.playerID, Teams.name == team, Teams.yearID == AllstarFull.yearID,
    #            Teams.teamID == AllstarFull.teamID, AllstarFull.yearID == year)
    session.close()
    return allstar


# The function to get the players who won a specific award in the given year
def getPlayerAwards(year, award):
    session = createConnection()
    awards = session.query(People, AwardsPlayers) \
        .filter(People.playerid == AwardsPlayers.playerid, AwardsPlayers.yearID == year,
                AwardsPlayers.awardID == award).order_by(AwardsPlayers.lgID)
    #awards = session.query(People, Awards) \
    #    .filter(People.playerid == Awards.playerid, Awards.yearID == year,
    #            Awards.awardID == award).order_by(Awards.lgID)
    session.close()
    return awards


# The function to get the managers who won a specific award on a given team
def getManagerAward(team, awardtype):
    session = createConnection()
    awards = session.query(AwardsManagers, Managers, People) \
        .filter(Managers.playerid == AwardsManagers.playerID, Managers.yearID == AwardsManagers.yearID,
                People.playerid == Managers.playerid,
                Managers.teamID == Teams.teamID, Managers.yearID == Teams.yearID, Teams.name == team,
                AwardsManagers.awardID == awardtype) \
        .order_by(Managers.yearID.desc())
    #awards = session.query(Awards, Managers, People) \
    #    .filter(Managers.playerid == Awards.playerID, Managers.yearID == Awards.yearID,
    #            People.playerid == Managers.playerid,
    #            Managers.teamID == Teams.teamID, Managers.yearID == Teams.yearID, Teams.name == team,
    #            Awards.awardID == awardtype) \
    #    .order_by(Managers.yearID.desc())
    session.close()
    return awards
