from fastapi import APIRouter, HTTPException
from api.schemas import RunRequest, CustomRunRequest
from simulator.runner import run_scenario, run_custom, summary
from simulator.scenarios import SCENARIOS

router = APIRouter()

@router.get("/scenarios")
def list_scenarios():
    return list(SCENARIOS.keys())

@router.post("/run")
def run(req: RunRequest):
    if req.scenario not in SCENARIOS:
        raise HTTPException(404, "Unknown scenario")
    df = run_scenario(req.scenario)
    return {"history": df.to_dict(orient="records"), "summary": summary(df)}

@router.post("/run/custom")
def run_custom_endpoint(req: CustomRunRequest):
    df = run_custom(req.n_companies, req.market_size, req.unit_cost,
                    req.steps, req.seed)
    return {"history": df.to_dict(orient="records"), "summary": summary(df)}
