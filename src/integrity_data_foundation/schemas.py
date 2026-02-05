from __future__ import annotations

from pydantic import BaseModel, Field
from typing import Optional

class IntegrityRecord(BaseModel):
    unit_id: str = Field(..., description="Unit identifier, e.g., 612")
    circuit_tag: str = Field(..., description="Circuit or equipment tag")
    equipment_id: str = Field(..., description="Equipment identifier")
    damage_mechanism: str = Field(..., description="Primary damage mechanism label")
    design_pressure_kpag: Optional[float] = Field(None, ge=0)
    design_temperature_c: Optional[float] = Field(None)
    last_inspection_date: Optional[str] = Field(None, description="YYYY-MM-DD")
    max_stcr_mpy: Optional[float] = Field(None, ge=0)
    max_ltcr_mpy: Optional[float] = Field(None, ge=0)
    risk_rank: Optional[str] = Field(None, description="Low/Medium/High or similar")
