import pytest
from scheduling.interval_scheduler import schedule_intervals

def test_schedule_intervals():
    intervals = [(1, 3), (2, 4), (3, 5), (0, 6)]
    result = schedule_intervals(intervals)
    assert result == [(1, 3), (3, 5)]

def test_empty_intervals():
    assert schedule_intervals([]) == []

def test_no_overlap():
    intervals = [(1, 2), (3, 4), (5, 6)]
    assert schedule_intervals(intervals) == [(1, 2), (3, 4), (5, 6)]

def test_all_overlap():
    intervals = [(1, 4), (2, 3), (3, 5)]
    assert schedule_intervals(intervals) == [(2, 3), (3, 5)]