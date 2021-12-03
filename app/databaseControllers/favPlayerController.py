from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func, distinct
import app.baseballModels.mariadbconfig as cfg
from app.baseballModels.people import People
from app.baseballModels.batting import Batting
from app.baseballModels.appearances import Appearances
from app.baseballModels.pitching import Pitching
from app.baseballModels.battingpost import BattingPost
from app.baseballModels.pitchingpost import PitchingPost


# Create a connection to the database
def createConnection():
    enginestr = "mysql+pymysql://" + cfg.mysql['user'] + ":" + cfg.mysql['password'] + "@localhost:3306/group3"

    engine = create_engine(enginestr)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


# The function to get the career batting stats sum for a specific player
def careerBattingStats(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.sum(Batting.b_AB), func.sum(Batting.b_R), func.sum(Batting.b_H), func.sum(Batting.b_HR),
                          func.sum(Batting.b_RBI), func.sum(Batting.b_SO)) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1], People.playerID == Batting.playerID)
    return stats


# The function to get the batting stats of a given player per year
def battingStats(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(Batting) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1], People.playerID == Batting.playerID) \
        .order_by(Batting.yearId, Batting.stint)
    return stats


# The function to get the career pitching stats sum for a specific player
def careerPitchingStats(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.sum(Pitching.p_W), func.sum(Pitching.p_L), func.sum(Pitching.p_IPouts), func.sum(Pitching.p_SO),
                          func.sum(Pitching.p_ER), func.sum(Pitching.p_BB), func.sum(Pitching.p_H)) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1], People.playerID == Pitching.playerID)
    return stats


# The function to get the pitching stats of a given player per year
def pitchingStats(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(Pitching) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1], People.playerID == Pitching.playerID) \
        .order_by(Pitching.yearID, Pitching.stint)
    return stats


# Get the number of appearances for a given player
def getSumAppearances(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.sum(Appearances.G_p), func.sum(Appearances.G_batting),
                          func.count(distinct(Appearances.yearID))) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == Appearances.playerID)
    return stats


# The function to get the career batting postseason stats sum for a specific player
def careerBattingPost(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.sum(BattingPost.b_AB), func.sum(BattingPost.b_R), func.sum(BattingPost.b_H),
                          func.sum(BattingPost.b_HR), func.sum(BattingPost.b_RBI), func.sum(BattingPost.b_SO)) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == BattingPost.playerID)
    return stats


# The function to get the batting postseason stats of a given player per year
def battingPost(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(BattingPost) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == BattingPost.playerID) \
        .order_by(BattingPost.yearId, BattingPost.round)
    return stats


# The function to get the career pitching postseason stats sum for a specific player
def careerPitchingPost(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.sum(PitchingPost.p_W), func.sum(PitchingPost.p_L), func.sum(PitchingPost.p_IPouts),
                          func.sum(PitchingPost.p_SO), func.sum(PitchingPost.p_ER), func.sum(PitchingPost.p_BB), func.sum(PitchingPost.p_H)) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == PitchingPost.playerID)
    return stats


# The function to get the pitching postseason stats of a given player per year
def pitchingPost(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(PitchingPost) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == PitchingPost.playerID) \
        .order_by(PitchingPost.yearID, PitchingPost.round)
    return stats


# The function to get the postseason batting appearances of a given player
def postAppearancesBatting(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.count(BattingPost.yearId), func.count(distinct(BattingPost.yearId))) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == BattingPost.playerID)
    return stats


# The function to get the postseason pitching appearances of a given player
def postAppearancesPitching(playerName):
    splitName = playerName.split()
    session = createConnection()
    stats = session.query(func.count(PitchingPost.yearID), func.count(distinct(PitchingPost.yearID))) \
        .filter(People.nameFirst == splitName[0], People.nameLast == splitName[1],
                People.playerID == PitchingPost.playerID)
    return stats