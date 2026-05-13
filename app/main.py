import json
import sys
from pathlib import Path

from app.models.claim import ClaimFields
from app.models.output import ClaimProcessingResult
from app.services.document_loader import (
    DocumentNotFoundError,
    UnsupportedFileTypeError,
    load_document,
)


def demo_model_output() -> None:
    """
    Temporary model demo for Commit 4.
    This verifies that our Pydantic models generate assignment-compatible JSON.
    """

    extracted_fields = ClaimFields(
        policy_number="POL-2026-001",
        policyholder_name="Ratan Kumar",
        effective_dates="2026-01-01 to 2026-12-31",
        incident_date="2026-05-10",
        incident_time="10:30 AM",
        incident_location="Bengaluru, Karnataka",
        incident_description="Minor vehicle collision near Whitefield.",
        claimant="Ratan Kumar",
        third_parties="None",
        contact_details="+91-9876543210",
        asset_type="Vehicle",
        asset_id="KA01AB1234",
        estimated_damage=18000,
        claim_type="vehicle_damage",
        attachments="vehicle_photos, repair_estimate",
        initial_estimate=18000,
    )

    result = ClaimProcessingResult(
        extracted_fields=extracted_fields,
        missing_fields=[],
        recommended_route="Fast-track",
        reasoning="Estimated damage is below ₹25,000 and all mandatory fields are present.",
    )

    print(
        json.dumps(
            result.model_dump(by_alias=True),
            indent=2,
            ensure_ascii=False,
        )
    )


def main() -> None:
    """
    Temporary CLI entry point.

    For Commit 4:
    - If no file path is passed, show model JSON demo.
    - If a file path is passed, load and print document text.
    """

    if len(sys.argv) < 2:
        project_root = Path(__file__).resolve().parent.parent

        print("Autonomous Insurance Claims Processing Agent started.")
        print(f"Project root: {project_root}")
        print()
        print("Sample assignment-compatible output:")
        print("-" * 80)
        demo_model_output()
        print()
        print("Usage:")
        print("  python -m app.main <path-to-fnol-document>")
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
        print(f"Unexpected error while loading document: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()