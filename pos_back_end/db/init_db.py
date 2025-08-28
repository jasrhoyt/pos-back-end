import os
from pathlib import Path
from sqlalchemy import create_engine
from pos_back_end.db.base import Base
import os
from sqlalchemy import create_engine
from pos_back_end.db.base import Base  # import your declarative base

def init_db():
    # Get the database URL from environment variables (fallback to default)
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://jasonhoyt:password@localhost:5432/pos_systems_database"
    )

    # Create the engine
    engine = create_engine(DATABASE_URL)

    # Create all tables defined in your models
    Base.metadata.create_all(engine)

    print(f"Database initialized successfully at {DATABASE_URL}")


if __name__ == "__main__":
    init_db()
