"""
Simplified Job Shop Scheduler using greedy heuristic.
Each job has a list of (machine_id, duration) operations.
We schedule each operation as early as possible on its machine.
Minimizes makespan (total completion time).
"""

from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Operation:
    job_id: int
    machine_id: int
    duration: int
    start: int = -1
    end: int = -1

def job_shop_greedy(jobs: List[List[Tuple[int, int]]]) -> Tuple[Dict[int, List[Operation]], int]:
    """
    Schedule jobs in job shop using greedy "earliest available" heuristic.

    Args:
        jobs: List of jobs; each job is list of (machine_id, duration).

    Returns:
        Dictionary of machine schedules and total makespan.
    """
    num_jobs = len(jobs)
    operations = []
    for job_id, job in enumerate(jobs):
        for machine_id, duration in job:
            operations.append(Operation(job_id, machine_id, duration))

    # Track when each machine becomes free
    machine_free_time: Dict[int, int] = {}
    # Track job completion times to enforce order
    job_completion_time: Dict[int, int] = {i: 0 for i in range(num_jobs)}

    # Group operations by machine
    machine_schedule: Dict[int, List[Operation]] = {}

    for op in operations:
        machine_id = op.machine_id
        job_id = op.job_id
        duration = op.duration

        # When can this operation start?
        machine_available = machine_free_time.get(machine_id, 0)
        job_available = job_completion_time[job_id]
        start_time = max(machine_available, job_available)

        end_time = start_time + duration

        # Update operation
        op.start = start_time
        op.end = end_time

        # Update machine and job state
        machine_free_time[machine_id] = end_time
        job_completion_time[job_id] = end_time

        if machine_id not in machine_schedule:
            machine_schedule[machine_id] = []
        machine_schedule[machine_id].append(op)

    makespan = max(job_completion_time.values()) if job_completion_time else 0
    return machine_schedule, makespan