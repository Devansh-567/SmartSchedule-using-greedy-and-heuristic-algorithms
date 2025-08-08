# examples/test_job_shop.py

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scheduling.job_shop_scheduler import job_shop_greedy

if __name__ == "__main__":
    jobs = [
        [(0, 3), (1, 2)],  # Job 0: Machine 0 for 3 units, then Machine 1 for 2
        [(1, 4), (0, 1)]   # Job 1: Machine 1 for 4, then Machine 0 for 1
    ]

    schedule, makespan = job_shop_greedy(jobs)

    print(f"✅ Makespan: {makespan}")
    for machine_id in sorted(schedule.keys()):
        print(f"\n🔧 Machine {machine_id}:")
        for op in schedule[machine_id]:
            print(f"   Job {op.job_id}: [{op.start}, {op.end})")