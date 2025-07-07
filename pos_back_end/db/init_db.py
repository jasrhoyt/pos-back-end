# pos_back_end/db/init_db.py
import os
from pathlib import Path
from sqlalchemy import create_engine
from pos_back_end.db.base import Base


def init_db():
    # Get the project root directory (parent of pos_back_end/)
    project_root = Path(__file__).parent.parent.parent  # Navigate up from db/ to project root

    # Define the database path
    db_dir = project_root / 'pos_back_end' / 'db'
    db_path = db_dir / 'pos_system_database.db'

    # Ensure the db directory exists
    os.makedirs(db_dir, exist_ok=True)

    # Create the database engine with absolute path
    engine = create_engine(f'sqlite:///{db_path}')

    # Create all tables defined in the models
    # Base.metadata.create_all(engine)
    print(f"Database initialized successfully at {db_path}")


if __name__ == '__main__':
    init_db()