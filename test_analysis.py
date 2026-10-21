from analysis import amortized_costs, append_costs, bank_balances


def test_first_nine_costs_match_the_cost_table() -> None:
    assert append_costs(9) == [1, 2, 3, 1, 5, 1, 1, 1, 9]


def test_aggregate_total_cost_never_passes_three_n() -> None:
    total = 0
    for n, cost in enumerate(append_costs(10_000), start=1):
        total += cost
        assert total <= 3 * n


def test_accounting_charge_of_three_never_runs_out_of_credit() -> None:
    balances = bank_balances(append_costs(10_000), charge=3)
    assert min(balances) >= 0


def test_accounting_charge_of_two_runs_out_at_the_fifth_append() -> None:
    balances = bank_balances(append_costs(100), charge=2)
    first_negative = next(i for i, b in enumerate(balances, start=1) if b < 0)
    assert first_negative == 5


def test_potential_method_gives_an_amortized_cost_of_three() -> None:
    assert set(amortized_costs(10_000)) == {3}


def test_fixed_growth_costs_far_more_per_append_than_doubling() -> None:
    n = 10_000
    doubling = sum(append_costs(n)) / n
    fixed = sum(append_costs(n, grow=lambda capacity: capacity + 10)) / n
    assert doubling < 3
    assert fixed > 100
