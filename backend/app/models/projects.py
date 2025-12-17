from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    project_type = Column(String)
    project_description = Column(String)