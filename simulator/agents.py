import mesa
import numpy as np

STRATEGIES = ["cost_leader", "differentiator", "aggressive", "balanced"]

class CompanyAgent(mesa.Agent):
    def __init__(self, uid, model, strategy: str):
        super().__init__(uid, model)
        self.strategy = strategy
        self.cash = 1_000_000.0
        self.market_share = 0.1
        self.price = 100.0
        self.quality = 50.0
        self.marketing = 100_000.0
        self.alive = True
        self.history = []

    def step(self):
        if not self.alive:
            return
        self._adapt()
        self._economics()
        self._record()

    def _adapt(self):
        if self.strategy == "cost_leader":
            self.price *= 0.98
            self.marketing *= 0.95
        elif self.strategy == "differentiator":
            self.quality *= 1.02
            self.marketing *= 1.05
        elif self.strategy == "aggressive":
            self.marketing *= 1.10
            self.price *= 0.97
        elif self.strategy == "balanced":
            self.price *= 1.001
            self.quality *= 1.005

        self.price = max(10.0, self.price)
        self.quality = min(200.0, self.quality)

    def _economics(self):
        revenue = self.model.market_size * self.market_share * self.price
        cost = (self.model.market_size * self.market_share * self.model.unit_cost
                + self.marketing)
        self.cash += revenue - cost
        if self.cash <= 0:
            self.alive = False
            self.market_share = 0.0

    def _record(self):
        self.history.append({
            "step": self.model.schedule.steps,
            "cash": self.cash, "share": self.market_share,
            "price": self.price, "quality": self.quality,
            "alive": self.alive,
        })
