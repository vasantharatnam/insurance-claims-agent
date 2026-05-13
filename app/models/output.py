from typing import Any

from pydantic import BaseModel, Field

from app.models.claim import ClaimFields


class ClaimProcessingResult(BaseModel):
    """
    Final response returned by the autonomous claims processing agent.

    This model follows the assignment-required JSON format.
    """

    extracted_fields: ClaimFields = Field(alias="extractedFields")
    missing_fields: list[str] = Field(default_factory=list , alias="missingFields")
    recommended_route: str = Field(alias="recommendedRoute")
    reasoning: str

    class Config:
        populate_by_name = True


class ValidationResult(BaseModel):
    """
     Internal validation result used before routing.
    """

    missing_fields: list[str] = Field(default_factory=list)
    inconsistencies: list[str] = Field(default_factory=list)
    suspicious_keywords: list[str] = Field(default_factory=list)

    @property
    def has_missing_fields(self) -> bool:
        return len(self.missing_fields) > 0

    @property
    def has_inconsistencies(self) -> bool:
        return len(self.inconsistencies) > 0

    @property
    def has_suspicious_keywords(self) -> bool:
        return len(self.suspicious_keywords) > 0