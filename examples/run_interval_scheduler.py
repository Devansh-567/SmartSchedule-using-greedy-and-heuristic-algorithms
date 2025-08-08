"""
CLI script to demonstrate interval scheduling.
"""
from scheduling.interval_scheduler import schedule_intervals

if __name__ == "__main__":
    meetings = [
        (1, 3),
        (2, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (8, 9)
    ]

    print("All meetings:", meetings)
    scheduled = schedule_intervals(meetings)
    print("Selected meetings:", scheduled)
    print(f"Maximum {len(scheduled)} meetings can be scheduled.")