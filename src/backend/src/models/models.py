from enum import Enum
from typing import List, Optional
from sqlalchemy import Column, TIMESTAMP
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

# User roles enumeration
class RoleEnum(str, Enum):
    driver = "Driver"
    main_trimmer = "Main Trimmer"
    headsail_trimmer = "Headsail Trimmer"
    pit = "Pit"
    mast = "Mast"
    bow = "Bow"
    squirrel = "Squirrel"

# User group enumeration
class GroupEnum(str, Enum):
    admin = "Admin"
    full_time_crew = "Full-time"
    part_time_crew = "Part-time"
    guest = "Guest"

# User model
class Crew(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(sa_column_kwargs={"unique": True}, index=True)
    email: str = Field(sa_column_kwargs={"unique": True})
    hashed_password: str
    role_1: RoleEnum
    role_2: RoleEnum
    group: GroupEnum

    regattas: List["Regatta"] = Relationship(back_populates="users")
    
    def __repr__(self):
        return f"<Crew(username={self.username}, role_1={self.role_1}, group={self.group})>"


# Regatta model
class Regatta(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    yacht_club: str
    name: str
    date: str  # you can use datetime if you want more granularity
    start: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), nullable=True))
    end: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), nullable=True))
    status: Optional[str] = None

    crew: List[Crew] = Relationship(back_populates="regattas")

    def __repr__(self):
        return f"<Regatta(name={self.name}, date={self.date}, status={self.status})>"


class CrewStatus(str, Enum):
    confirmed = "Confirmed"
    maybe = "Maybe"
    no_response = "No Response"
    no = "no"


# RegattaUserLink model for many-to-many relationship
class RegattaUserLink(SQLModel, table=True):
    event_id: int = Field(foreign_key="event.id", primary_key=True)
    user_id: int = Field(foreign_key="crew.id", primary_key=True)
    crew_status: CrewStatus = Field(default=CrewStatus.no_response)  # Confirmed, Maybe, or No
    attended: Optional[bool] = None  # Confirmed, Maybe, or No

