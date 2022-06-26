from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connect to database
SQLALCHEMY_DATABASE_URL = 'sqlite:///./wiki.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


LocalSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
# End of connecting to database