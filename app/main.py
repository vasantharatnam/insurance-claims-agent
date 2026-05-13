
from pathlib import Path

def main() -> None:
    """
    Entry point for the Autonomous Insurance claims Processing Agent

    For now,  this only verifies that the project setup is working
    In later commits , this file accepts a document path and process FNOL  files

    """

    project_root = Path(__file__).resolve().parent.parent

    print("Autonomous Insurance Claims Processing Agent stated.")
    print(f"Project root directory: {project_root}")
    print("status: setup successful")

if __name__ == "__main__":
    main()