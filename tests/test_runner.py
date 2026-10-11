from simulator.runner import run_custom, summary

def test_run_custom():
    df = run_custom(n_companies=3, market_size=500_000, unit_cost=40,
                    steps=20, seed=1)
    assert "company" in df.columns
    s = summary(df)
    assert "alive" in s
    assert "leader" in s
