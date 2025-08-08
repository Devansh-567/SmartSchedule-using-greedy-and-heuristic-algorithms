import pytest
from scheduling.job_shop_scheduler import job_shop_greedy

def test_job_shop_greedy():
    jobs = [
        [(0, 3), (1, 2)],  # Job 0: Machine 0 (3 units), then Machine 1 (2 units)
        [(1, 4), (0, 1)]   # Job 1: Machine 1 (4 units), then Machine 0 (1 unit)
    ]

    schedule, makespan = job_shop_greedy(jobs)

    # Check makespan
    assert makespan == 7  # Expected from manual calculation

    # Validate machine 0
    m0_ops = schedule[0]
    assert len(m0_ops) == 2
    assert m0_ops[0].job_id == 0
    assert m0_ops[0].start == 0
    assert m0_ops[0].end == 3
    assert m0_ops[1].job_id == 1
    assert m0_ops[1].start == 3
    assert m0_ops[1].end == 4

    # Validate machine 1
    m1_ops = schedule[1]
    assert m1_ops[0].job_id == 0
    assert m1_ops[0].start == 3
    assert m1_ops[0].end == 5
    assert m1_ops[1].job_id == 1
    assert m1_ops[1].start == 0
    assert m1_ops[1].end == 4