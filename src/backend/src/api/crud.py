from sqlmodel import select
from src.models.models import Crew, Regatta

def create_crew(db, username: str, email: str, hashed_password: str, role_1, role_2, group):
    crew = Crew(username=username, email=email, hashed_password=hashed_password, role_1=role_1, role_2=role_2, group=group)
    db.add(crew)
    db.commit()
    db.refresh(crew)
    return crew

def create_regatta(db, name: str, date: str, status: str):
    regatta = Regatta(name=name, date=date, status=status)
    db.add(regatta)
    db.commit()
    db.refresh(regatta)
    return regatta

def get_crew(db):
    return db.execute(select(Crew)).scalars().all()

def get_regattas(db):
    return db.execute(select(Regatta)).scalars().all()
