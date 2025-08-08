"""
Greedy algorithm for interval scheduling (max non-overlapping intervals).
Problem: Given meetings [start, end], select max number of non-overlapping.
Algorithm: Sort by end time, pick earliest-ending compatible meeting.
Complexity: O(n log n)
"""

from typing import List, Tuple

def schedule_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Schedule maximum non-overlapping intervals using greedy algorithm.

    Args:
        intervals: List of (start, end) times.

    Returns:
        List of selected non-overlapping intervals.
    """
    if not intervals:
        return []

    # Sort by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    selected = [sorted_intervals[0]]
    last_end = sorted_intervals[0][1]

    for start, end in sorted_intervals[1:]:
        if start >= last_end:  # No overlap
            selected.append((start, end))
            last_end = end

    return selected