DAMAGE_FAST_TRACK_THRESHOLD = 25_000

ROUTE_FAST_TRACK = "Fast-track"
ROUTE_MANUAL_REVIEW = "Manual Review"
ROUTE_INVESTIGATION_FLAG = "Investigation Flag"
ROUTE_SPECIALIST_QUEUE = "Specialist Queue"
ROUTE_STANDARD_REVIEW = "Standard Review"

SUSPICIOUS_KEYWORDS = [
    "fraud",
    "inconsistent",
    "staged",
]

MANDATORY_FIELDS = [
    "policy_number",
    "policyholder_name",
    "effective_dates",
    "incident_date",
    "incident_time",
    "incident_location",
    "incident_description",
    "claimant",
    "contact_details",
    "asset_type",
    "asset_id",
    "estimated_damage",
    "claim_type",
    "attachments",
    "initial_estimate",
]