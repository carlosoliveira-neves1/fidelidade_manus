import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_SCHEMA = os.getenv("DATABASE_SCHEMA")

connect_args = {}
if DATABASE_SCHEMA:
    # Define o search_path no Postgres para criar/usar as tabelas nesse schema
    connect_args = {"options": f"-csearch_path={DATABASE_SCHEMA}"}

if not DATABASE_URL:
    # fallback local em SQLite
    DATABASE_URL = "sqlite:///db.sqlite3"
    connect_args = {}

engine = create_engine(DATABASE_URL, future=True, echo=False, connect_args=connect_args)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True))
Base = declarative_base()
