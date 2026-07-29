from sqlalchemy import Boolean, Numeric
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.database.base import Base


class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(100), nullable=False)
    team_colour = Column(String(20))
    country = Column(String(50))

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    drivers = relationship("Driver", back_populates="team")

##############################################


class Driver(Base):
    __tablename__ = "drivers"
    driver_id = Column(Integer, primary_key=True)
    driver_number = Column(Integer, nullable=False)
    full_name = Column(String(100), nullable=False)
    name_acronym = Column(String(5), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.team_id"))
    country_code = Column(String(10))
    headshot_url = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )

    team = relationship("Team", back_populates="drivers")

###############################################


class Meeting(Base):
    __tablename__ = "meetings"
    meeting_id = Column(Integer, primary_key=True)
    season = Column(Integer, nullable=False)
    round = Column(Integer, nullable=False)
    meeting_name = Column(String(100), nullable=False)
    official_name = Column(Text)
    country_name = Column(String(50))
    country_code = Column(String(5))
    circuit_short_name = Column(String(100))
    location = Column(String(100))
    date_start = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )
    sessions = relationship(
        "Session",
        back_populates="meeting"
    )

################################################


class Session(Base):
    __tablename__ = "sessions"
    session_id = Column(Integer, primary_key=True)
    meeting_id = Column(
        Integer,
        ForeignKey("meetings.meeting_id")
    )
    session_name = Column(String(50))
    session_type = Column(String(20))
    date_start = Column(TIMESTAMP)
    date_end = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )
    meeting = relationship(
        "Meeting",
        back_populates="sessions"
    )
    race_results = relationship(
        "RaceResult",
        back_populates="session"
    )

################################################


class RaceResult(Base):
    __tablename__ = "race_results"
    result_id = Column(Integer, primary_key=True)
    session_id = Column(
        Integer,
        ForeignKey("sessions.session_id")
    )
    driver_id = Column(
        Integer,
        ForeignKey("drivers.driver_id")
    )
    position = Column(Integer)
    grid_position = Column(Integer)
    points = Column(Numeric(5, 2))
    status = Column(String(50))
    finish_time = Column(String(50))
    fastest_lap = Column(Boolean)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP,
        server_default=func.now(),
        onupdate=func.now()
    )
    session = relationship(
        "Session",
        back_populates="race_results"
    )
    driver = relationship("Driver")

###############################################


class DriverStanding(Base):
    __tablename__ = "driver_standings"
    season = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey(
        "drivers.driver_id"), primary_key=True)
    position = Column(Integer)
    points = Column(Numeric(6, 2))
    wins = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())

###############################################


class ConstructorStanding(Base):
    __tablename__ = "constructor_standings"
    season = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey("teams.team_id"), primary_key=True)
    position = Column(Integer)
    points = Column(Numeric(6, 2))
    wins = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.now())
