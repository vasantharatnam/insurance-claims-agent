from typing import Optional

from pydantic import BaseModel, Field


class ClaimFields(BaseModel):
    """
     Represents extracted fields from an FNOL document.

     These fields are optional because extraction call fail or the source
     document may not  contain all required information
    """

    # Policy Information
    policy_number: Optional[str] = Field(default=None, alias = "policyNumber")
    policyholder_name: Optional[str] = Field(default=None, alias = "policyholderName")
    effective_dates: Optional[str] = Field(default=None , alias = "effectiveDates")

      # Incident Information
    incident_date: Optional[str] = Field(default=None, alias="incidentDate")
    incident_time: Optional[str] = Field(default=None, alias="incidentTime")
    incident_location: Optional[str] = Field(default=None, alias="incidentLocation")
    incident_description: Optional[str] = Field(default=None, alias="incidentDescription")

    # Involved Parties
    claimant: Optional[str] = None
    third_parties: Optional[str] = Field(default=None, alias="thirdParties")
    contact_details: Optional[str] = Field(default=None, alias="contactDetails")

    # Asset Details
    asset_type: Optional[str] = Field(default=None, alias="assetType")
    asset_id: Optional[str] = Field(default=None, alias="assetId")
    estimated_damage: Optional[float] = Field(default=None, alias="estimatedDamage")

    # Other Mandatory Fields
    claim_type: Optional[str] = Field(default=None, alias="claimType")
    attachments: Optional[str] = None
    initial_estimate: Optional[float] = Field(default=None, alias="initialEstimate")

    class Config:
        populate_by_name = True