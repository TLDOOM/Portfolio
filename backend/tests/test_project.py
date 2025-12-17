from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.projects import Projects # Your SQLAlchemy model
from app.core.db import Base

# -----------------------
# DATABASE CONFIGURATION
# -----------------------
DB_HOST = "portfolio-db"      # or Docker container name if connecting from another container
DB_PORT = 5432             # default PostgreSQL port
DB_NAME = "portfolio"
DB_USER = "portfolio"
DB_PASSWORD = "portfolio"

DATABASE_URL = "postgresql+psycopg2://portfolio:portfolio@db:5432/portfolio"


# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Make sure tables exist
Base.metadata.create_all(bind=engine)

# -----------------------
# SCRIPT TO INSERT PROJECT
# -----------------------
def insert_project():
    db = SessionLocal()
    try:
        print("Enter your project details:\n")
        name = input("Project Name: ").strip()
        project_type = input("Project Type: ").strip()
        project_description = input("Project Description: ").strip()

        new_project = Projects(
            name=name,
            project_type=project_type,
            project_description=project_description
        )

        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        print(f"\n✅ Project inserted successfully with ID: {new_project.id}")

    except Exception as e:
        db.rollback()
        print(f" Error inserting project: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    insert_project()
