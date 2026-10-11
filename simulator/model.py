import mesa
import numpy as np
from simulator.agents import CompanyAgent, STRATEGIES

class MarketModel(mesa.Model):
    def __init__(self, n_companies: int = 6, market_size: float = 1_000_000,
                 unit_cost: float = 40, seed: int = None):
        super().__init__(seed=seed)
        self.market_size = market_size
        self.unit_cost = unit_cost
        self.schedule = mesa.time.RandomActivation(self)
        self.history = []

        for i in range(n_companies):
            strat = np.random.choice(STRATEGIES)
            agent = CompanyAgent(i, self, strat)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()
        self._update_market_shares()
        self._record()

    def _update_market_shares(self):
        alive = [a for a in self.schedule.agents if a.alive]
        if not alive:
            return
        attract = {a.unique_id: (a.quality / a.price) * (1 + a.marketing / 1e6)
                   for a in alive}
        total = sum(attract.values())
        for a in alive:
            a.market_share = attract[a.unique_id] / total

    def _record(self):
        for a in self.schedule.agents:
            self.history.append({
                "step": self.schedule.steps,
                "company": a.unique_id,
                "strategy": a.strategy,
                "cash": a.cash,
                "share": a.market_share,
                "price": a.price,
                "quality": a.quality,
                "alive": a.alive,
            })
