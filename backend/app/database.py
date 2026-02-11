from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
# Example:
# mysql+pymysql://username:password@localhost:3306/emowell

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
