"""
ORMTables.py - Models for ORM in SQLAlchemy.
"""

from logging import getLogger, debug, error
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from pathlib import Path

__author__ = 'Travis Risner'
__project__ = "Christmas-Labels"
__creation_date__ = "03/17/2019"

# "${Copyright.py}"

db_name = 'labels.db'

engine = create_engine(f'sqlite:///{db_name}', echo=True)
Base = declarative_base()


class Contact(Base):
    """
    Contacts - Contacts ORM declaration.
    """
    __tablename__ = 'Contact'

    ContactID = Column(Integer, primary_key=True)
    NameLine = Column(String)
    PrintLabel = Column(Boolean)
    WhichAddress = Column(Boolean)
    HomeStreet = Column(String)
    HomeCity = Column(String)
    HomeState = Column(String)
    HomeZip = Column(String)
    AwayStreet = Column(String)
    AwayState = Column(String)
    AwayZip = Column(String)
    SortName = Column(String)

    def __init__(self, NameLine, PrintLabel, WhichAddress, HomeStreet,
                 HomeCity, HomeState, HomeZip, AwayStreet, AwayState, AwayZip,
                 SortName):
        self.NameLine = NameLine
        self.PrintLabel = PrintLabel
        self.WhichAddress = WhichAddress
        self.HomeStreet = HomeStreet
        self.HomeCity = HomeCity
        self.HomeState = HomeState
        self.HomeZip = HomeZip
        self.AwayStreet = AwayStreet
        self.AwayState = AwayState
        self.AwayZip = AwayZip
        self.SortName = SortName


class State(Base):
    """
    State - State ORM declaration.
    """
    __tablename__ = 'State'

    StateID = Column(Integer, primary_key=True)
    StateCode = Column(String)
    StateName = Column(String)

    def __init__(self, StateCode, StateName):
        self.StateCode = StateCode
        self.StateName = StateName

def create_db(working_directory: Path) -> Boolean:
    """
    Create the database with no data in it.

    :param working_directory: working directory for Christmas Labels
    """
    new_database_created = False
    # check for prior existnce of database before creating a new one.
    full_db_path = working_directory / db_name
    if not full_db_path.exists():
        response = input('\a\a\a*** Database not found!  Do you want to '
                         'create a new one? [yes/No] ')
        if response == 'yes':
            Base.metadata.create_all(engine)
            new_database_created = True
    return new_database_created

# EOF
