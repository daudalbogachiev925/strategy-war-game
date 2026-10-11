from simulator.agents import CompanyAgent, STRATEGIES
from simulator.model import MarketModel

def test_agent_init():
    m = MarketModel(n_companies=3, seed=1)
    a = m.schedule.agents[0]
    assert a.strategy in STRATEGIES
    assert a.cash > 0
    assert a.alive is True

def test_agent_death():
    m = MarketModel(n_companies=2, seed=1)
    a = m.schedule.agents[0]
    a.cash = -100
    a.step()
    assert a.alive is False
