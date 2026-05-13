
import sys
from pathlib import Path

from app.services.document_loader import (
    DocumentNotFoundError,
    UnsupportedFileTypeError,
    load_document,
)

def main() -> None:
    """
    Temporary CLI entry point.

    For Commit 3, this only loads and prints document text.
    In later commits, we will pass this text to the claim processor  pipeline
    """

    if len(sys.argv) < 2 :
       project_root = Path(__file__).resolve().parent.parent

       print("Autonomous Insurance Claims Processing Agent started.")
       print(f"Project root: {project_root}")
       print()
       print("Usage:")
       print("  python -m app.main <path-to-fnol-document>")
       print()
       print("Example:")
       print("  python -m app.main samples/fnol_1.txt")
       return
    
    file_path = sys.argv[1]

    try:
        document_text = load_document(file_path)

        print("Document loaded successfully.")
        print("-" * 80)
        print(document_text)

    except DocumentNotFoundError as error:
        print(f"Error: {error}")
        sys.exit(1)
    
    except UnsupportedFileTypeError as error:
        print(f"Error: {error}")
        sys.exit(1)
    
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()