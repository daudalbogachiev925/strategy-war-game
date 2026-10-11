from simulator.model import MarketModel

def test_model_run():
    m = MarketModel(n_companies=4, seed=42)
    for _ in range(10):
        m.step()
    assert len(m.history) >= 40

def test_market_shares_sum_to_one():
    m = MarketModel(n_companies=4, seed=42)
    for _ in range(5):
        m.step()
    alive = [a for a in m.schedule.agents if a.alive]
    total = sum(a.market_share for a in alive)
    if alive:
        assert abs(total - 1.0) < 1e-6
