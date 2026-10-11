from pydantic import BaseModel, Field

class RunRequest(BaseModel):
    scenario: str = "baseline"

class CustomRunRequest(BaseModel):
    n_companies: int = Field(6, ge=2, le=30)
    market_size: float = Field(1_000_000, gt=0)
    unit_cost: float = Field(40, gt=0)
    steps: int = Field(60, ge=5, le=500)
    seed: int = 42
