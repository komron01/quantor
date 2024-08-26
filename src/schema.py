from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Drug(Base):
    __tablename__ = "drugs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    smiles = Column(String)

# Database connection setup
DATABASE_URL = "postgresql://postgres:123@postgres:5432/drugs"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)
