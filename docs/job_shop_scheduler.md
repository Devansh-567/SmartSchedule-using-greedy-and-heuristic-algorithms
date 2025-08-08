# Job Shop Scheduling (Greedy Heuristic)

## Problem

Schedule N jobs across multiple machines. Each job consists of a sequence of operations on specific machines.

Goal: Minimize **makespan** (time to complete all jobs).

Use Case: Factory production lines, software build pipelines.

## Algorithm

- **Greedy "As Early As Possible"**:
  - For each operation in job order:
    - Schedule it on its machine at the earliest possible time.
    - Respect:
      - Machine availability
      - Previous operation in the same job must finish

## Limitations

- Not optimal (Job Shop is NP-hard).
- Fast and practical for small instances.

## Complexity

O(total_operations × log machines) with priority queues (not implemented here). Our version is O(N) in operations.

## Example

Job 0: M0(3) → M1(2)  
Job 1: M1(4) → M0(1)  
→ Makespan = 7
