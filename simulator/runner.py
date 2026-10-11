import pandas as pd
from simulator.model import MarketModel
from simulator.scenarios import SCENARIOS

def run_scenario(name: str) -> pd.DataFrame:
    cfg = SCENARIOS[name]
    steps = cfg.pop("steps")
    model = MarketModel(**cfg, seed=42)
    for _ in range(steps):
        model.step()
    return pd.DataFrame(model.history)

def run_custom(n_companies: int, market_size: float, unit_cost: float,
               steps: int, seed: int = 42) -> pd.DataFrame:
    model = MarketModel(n_companies=n_companies, market_size=market_size,
                        unit_cost=unit_cost, seed=seed)
    for _ in range(steps):
        model.step()
    return pd.DataFrame(model.history)

def summary(df: pd.DataFrame) -> dict:
    last = df[df.step == df.step.max()]
    return {
        "alive": int(last.alive.sum()),
        "total": len(last),
        "leader": last.loc[last.share.idxmax()].company,
        "leader_strategy": last.loc[last.share.idxmax()].strategy,
        "avg_price": float(last.price.mean()),
    }
