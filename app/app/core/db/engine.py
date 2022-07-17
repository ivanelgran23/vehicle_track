from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_string = "postgresql+psycopg2://postgres:postgres@db:5432/postgres"

engine = create_engine(db_string)

Session = sessionmaker(bind=engine)