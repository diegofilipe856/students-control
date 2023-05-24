from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = 'sqlite:///./fastsql.db'

engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
