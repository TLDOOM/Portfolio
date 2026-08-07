from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.db import Base
from app.models.projects import Projects

SQLITE_URL = "sqlite:///./test.db"  # adjust path if find showed something different
POSTGRES_URL = "postgresql+psycopg2://portfolio:portfolio@localhost:5432/portfolio"

sqlite_engine = create_engine(SQLITE_URL)
postgres_engine = create_engine(POSTGRES_URL)

SqliteSession = sessionmaker(bind=sqlite_engine)
PostgresSession = sessionmaker(bind=postgres_engine)

Base.metadata.create_all(bind=postgres_engine)

src = SqliteSession()
dst = PostgresSession()

rows = src.query(Projects).all()
print(f"Found {len(rows)} rows in SQLite")

for row in rows:
    data = {c.name: getattr(row, c.name) for c in Projects.__table__.columns if c.name != "id"}
    dst.add(Projects(**data))

dst.commit()
print("Done — check Postgres now")