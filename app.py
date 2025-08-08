# app.py - User-friendly scheduling app

import sys
import os

# Add parent directory to path so we can import scheduling module
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from scheduling.interval_scheduler import schedule_intervals
from scheduling.job_shop_scheduler import job_shop_greedy


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
    print("      🧠 OPTISCHED: Smart Scheduling Assistant")
    print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
    print()


def menu():
    print("What would you like to schedule?")
    print("1️⃣  Meeting Rooms (Maximize non-overlapping meetings)")
    print("2️⃣  Factory Jobs (Job Shop Scheduling)")
    print("3️⃣  Exit")
    print()
    choice = input("👉 Enter 1, 2, or 3: ").strip()
    return choice


def run_interval_scheduler():
    print("\n🗓️  Meeting Room Scheduler")
    print("Enter meetings as 'start end' (e.g., 9 11). Type 'done' when finished.\n")

    intervals = []
    while True:
        inp = input("Meeting (start end) or 'done': ").strip()
        if inp.lower() == 'done':
            break
        try:
            start, end = map(int, inp.split())
            if start >= end:
                print("⚠️  Start must be less than end. Try again.")
                continue
            intervals.append((start, end))
        except:
            print("❌ Invalid format. Use two numbers like: 1 3")

    if not intervals:
        print("🚫 No meetings entered.")
        return

    scheduled = schedule_intervals(intervals)

    print("\n✅ Final Schedule:")
    print(f"📌 You can fit {len(scheduled)} meetings:")
    for i, (start, end) in enumerate(scheduled, 1):
        print(f"   {i}. 🕘 {start}:00 – {end}:00")

    print("\n💡 Tip: This schedule maximizes the number of meetings in one room.\n")


def run_job_shop_scheduler():
    print("\n🏭 Job Shop Scheduler")
    print("Schedule jobs across machines to minimize total time.")
    print("Each job has steps: (machine_id, duration)\n")

    jobs = []

    try:
        num_jobs = int(input("How many jobs? "))
    except:
        print("❌ Invalid number. Try again.")
        return

    for job_id in range(num_jobs):
        print(f"\n🔧 Job {job_id + 1}:")
        print("Enter steps as 'machine duration' (e.g., 0 3). Type 'done' when finished.")

        operations = []
        while True:
            inp = input(f"  Step for Job {job_id + 1}: ").strip()
            if inp.lower() == 'done':
                break
            try:
                machine, duration = map(int, inp.split())
                if duration <= 0:
                    print("⚠️  Duration must be positive.")
                    continue
                operations.append((machine, duration))
            except:
                print("❌ Format: 'machine_id duration' (e.g., 1 5)")

        if operations:
            jobs.append(operations)

    if not jobs:
        print("🚫 No jobs defined.")
        return

    schedule, makespan = job_shop_greedy(jobs)

    print("\n" + "="*50)
    print(f"✅ SCHEDULE COMPLETE! Total time: {makespan} units")
    print("="*50)

    for machine_id in sorted(schedule.keys()):
        print(f"\n🖥️  Machine {machine_id}:")
        for op in schedule[machine_id]:
            job_id = op.job_id
            print(f"   ⏱️  [{op.start} – {op.end}): Job {job_id + 1}")

    print("\n📋 Summary:")
    for job_id in range(len(jobs)):
        ops = [op for machine_ops in schedule.values() for op in machine_ops if op.job_id == job_id]
        if ops:
            start_time = ops[0].start
            end_time = ops[-1].end
            print(f"   Job {job_id + 1}: Starts at {start_time}, finishes at {end_time}")

    print("\n💡 This schedule minimizes idle time using a smart heuristic.\n")


def main():
    clear_screen()
    print_header()

    while True:
        choice = menu()

        if choice == '1':
            run_interval_scheduler()
        elif choice == '2':
            run_job_shop_scheduler()
        elif choice == '3':
            print("\n👋 Thank you for using OptiSched! See you next time.")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.\n")

        input("🔁 Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()