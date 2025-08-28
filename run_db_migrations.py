#!/usr/bin/env python3
import subprocess
import sys


def run_db_migrations(message: str) -> None:
    """
    Run Alembic migration commands with the provided message.

    Args:
        message (str): The message to use for the Alembic revision.
    """
    try:
        # Run alembic revision --autogenerate
        subprocess.run(
            ["pipenv", "run", "alembic", "revision", "--autogenerate", "-m", message],
            check=True,
            text=True
        )
        print(f"Successfully created revision with message: {message}")

        # Run alembic upgrade head
        subprocess.run(
            ["pipenv", "run", "alembic", "upgrade", "head"],
            check=True,
            text=True
        )
        print("Successfully upgraded database to head revision")

    except subprocess.CalledProcessError as e:
        print(f"Error running migration: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_db_migrations.py <migration_message>")
        sys.exit(1)

    migration_message = sys.argv[1]
    run_db_migrations(migration_message)