import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.db import Base
from app.models.projects import Projects

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./test.db"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)


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

        print(f"\nProject inserted successfully with ID: {new_project.id}")

    except Exception as e:
        db.rollback()
        print(f"Error inserting project: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    insert_project()