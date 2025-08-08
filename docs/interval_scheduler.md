# Interval Scheduling Algorithm

## Problem

Given a list of meetings with start and end times, select the **maximum number** of non-overlapping meetings.

Use Case: Scheduling meetings in a single conference room.

## Algorithm

- **Greedy Strategy**: Sort intervals by **end time**.
- Pick the earliest-ending meeting.
- Skip any that overlap with the last selected.

Why it works: By choosing the meeting that ends earliest, we leave the room free as soon as possible.

## Complexity

- Sorting: O(n log n)
- Iteration: O(n)
- Total: O(n log n)

## Example

Input: `[(1,3), (2,4), (3,5), (0,6)]`  
Output: `[(1,3), (3,5)]` → 2 meetings scheduled.
