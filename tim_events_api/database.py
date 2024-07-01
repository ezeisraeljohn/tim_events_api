from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
CA_CERT_PATH = os.getenv("CA_CERT_PATH")
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL,
    connect_args={
        "ssl": {
            "sslmode": "REQUIRED",
            "ca": CA_CERT_PATH,
        },
    },
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
