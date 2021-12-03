from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Appearances(Base):
    __tablename__ = "appearances"  # required

    ID = Column(Integer, primary_key=True)  # required
    yearID = Column(Integer)
    teamId = Column(String(3))  # teamId = Column(String(3))
    #lgID = Column(String(2))
    playerID = Column(String(9))  # playerID = Column(String(9))
    G_all = Column(Integer)
    GS = Column(Integer)
    G_batting = Column(Integer)
    G_defense = Column(Integer)
    G_p = Column(Integer)
    G_c = Column(Integer)
    G_1b = Column(Integer)
    G_2b = Column(Integer)
    G_3b = Column(Integer)
    G_ss = Column(Integer)
    G_lf = Column(Integer)
    G_cf = Column(Integer)
    #G_rf = Column(Integer)
    G_of = Column(Integer)
    G_dh = Column(Integer)
    G_ph = Column(Integer)
    G_pr = Column(Integer)
