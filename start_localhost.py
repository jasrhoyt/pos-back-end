#!/usr/bin/env python3
import subprocess
import sys


def start_localhost() -> None:
    """
    Run the Uvicorn server with reload enabled.
    """
    try:
        # Run uvicorn pos_back_end.main:app --reload
        subprocess.run(
            ["pipenv", "run", "uvicorn", "pos_back_end.main:app", "--reload"],
            check=True,
            text=True
        )
        print("Uvicorn server started successfully")

    except subprocess.CalledProcessError as e:
        print(f"Error starting Uvicorn server: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    start_localhost()
