from sqlmodel import Session
from fastapi import FastAPI, Depends
from src.api.database import get_db, create_db
from src.api.crud import create_crew, create_regatta, get_crew, get_regattas
from src.models.models import RoleEnum, GroupEnum

app = FastAPI()

# FastAPI event handlers for shutdown and startup
@app.on_event("startup")
async def on_startup():
    # Create database tables on startup
    create_db()
    print("Database tables created.")

@app.on_event("shutdown")
async def on_shutdown():
    # Logic to handle shutdown (e.g., cleanup)
    print("Shutting down the app.")

# Route to create a new user
@app.post("/crew/", response_model=dict)
async def create_new_user(username: str, email: str, hashed_password: str, role_1: RoleEnum, role_2: RoleEnum, group: GroupEnum, db: Session = Depends(get_db)):
    crew = create_crew(db, username, email, hashed_password, role_1, role_2, group)
    return {"id": crew.id, "username": crew.username}

# Route to create a new event
@app.post("/regattas/", response_model=dict)
async def create_new_event(name: str, date: str, status: str, db: Session = Depends(get_db)):
    event = create_regatta(db, name, date, status)
    return {"id": event.id, "name": event.name}

# Route to get a list of users
@app.get("/crew/", response_model=list)
async def read_crew(db: Session = Depends(get_db)):
    crew = get_crew(db)
    return crew

# Route to get a list of events
@app.get("/regattas/", response_model=list)
async def read_regattas(db: Session = Depends(get_db)):
    regattas = get_regattas(db)
    return regattas

