from fastapi import FastAPI,Depends
from app.core.db import Base, engine,SessionLocal
from app.v1.routes import user,projects,future
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.models.projects import Projects
from app.models.future import Future # example SQLAlchemy modell

app = FastAPI(title="Portfolio Backend")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/api/v1")
app.include_router(projects.router, prefix ="/api/v1")
app.include_router(future.router, prefix= "/api/v1")

@app.get("/projects")
def read_project(db: Session = Depends(get_db)):
    return db.query(Projects).all()

@app.get("/future")
def read_future(db: Session = Depends(get_db)):
    return db.query(Future).all()

