# 🕰️ OptiSched – Smart Scheduling Algorithms for Real-World Problems

**OptiSched** is a modular, open-source Python library that solves real-world scheduling problems using classical and heuristic algorithms.

Unlike generic scheduling scripts, OptiSched brings together **algorithmic precision**, **real-world usability**, and **educational clarity** — all in a lightweight, zero-dependency package.

Built for developers, students, operations teams, and anyone who needs to make **smart scheduling decisions fast**.

---

## 📦 Features

| Feature                | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| 🗓️ Interval Scheduling | Maximize non-overlapping meetings using greedy algorithm              |
| 🏭 Job Shop Scheduling | Schedule multi-step jobs across machines to minimize makespan         |
| 🖥️ Interactive App     | User-friendly CLI via `app.py` — no coding needed                     |
| 🧪 Unit Tested         | Full test coverage with `pytest`                                      |
| 📚 Educational Docs    | Clear explanations of algorithms and complexity                       |
| 📊 Extensible Design   | Add your own algorithms (e.g., genetic, tabu search)                  |
| 🧩 Modular Structure   | Clean layout: `scheduling/`, `examples/`, `tests/`                    |
| 🔍 Input Validation    | Prevents invalid times (e.g., 12 → 1) with helpful messages           |
| 📈 Clear Output        | Displays who does what, when, and for how long                        |
| 🧠 Zero Dependencies   | Core runs on pure Python — extras only for notebooks or visualization |

---

## 🛠️ Installation

No installation required for basic use.

```bash
git clone https://github.com/Devansh-567/SmartSchedule-using-greedy-and-heuristic-algorithms.git
cd SmartSchedule-using-greedy-and-heuristic-algorithms
pip install -r requirements.txt  # Optional: for tests or notebooks
python app.py

```

> Requires Python **3.7+**

---

## 🚀 Quick Start

### 🔹 Run the Interactive App (No Coding Required)

```bash
python app.py
```

You'll see:

```
🧠 OPTISCHED: Smart Scheduling Assistant

1️⃣ Meeting Rooms (Maximize non-overlapping meetings)
2️⃣ Factory Jobs (Job Shop Scheduling)
3️⃣ Exit

👉 Enter 1, 2, or 3:
```

---

## 🧪 Developer Usage

### Interval Scheduling

```python
from scheduling.interval_scheduler import schedule_intervals

meetings = [(1, 3), (2, 4), (3, 5), (0, 6)]
scheduled = schedule_intervals(meetings)
print(scheduled)  # ➜ [(1, 3), (3, 5)]
```

### Job Shop Scheduling

```python
from scheduling.job_shop_scheduler import job_shop_greedy

jobs = [
    [(0, 3), (1, 2)],
    [(1, 4), (0, 1)]
]

schedule, makespan = job_shop_greedy(jobs)
print("Makespan:", makespan)  # ➜ 7
```

---

## 🧰 API Reference

### `schedule_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]`

- **Purpose:** Maximize non-overlapping meetings
- **Algorithm:** Greedy (sort by end time)
- **Time Complexity:** `O(n log n)`
- **Returns:** List of selected (start, end) intervals

---

### `job_shop_greedy(jobs: List[List[Tuple[int, int]]]) -> Tuple[Dict[int, List[Operation]], int]`

- **Purpose:** Schedule jobs across machines to minimize makespan
- **Algorithm:** Heuristic — schedule each operation as early as possible
- **Time Complexity:** `O(total_operations)`
- **Returns:** A machine-wise schedule and total makespan

---

## 🎯 Applications

### 🏢 Office & Team Scheduling

- Optimize meeting room usage
- Prevent double-booking
- Automate calendar planning

### 🏭 Manufacturing & Production

- Job scheduling for CNC, ovens, or assembly lines
- Kitchen workflows (cook → plate → serve)
- Minimize downtime

### 🏥 Healthcare & Clinics

- Patient time slot assignment
- OR room planning
- Therapist session scheduling

### 📦 Software & DevOps

- CI/CD pipeline slotting
- Build server load balancing
- Task prioritization

### 🎓 Education

- Teach algorithms (Greedy, NP-Hard heuristics)
- Demonstrate scheduling trade-offs
- Use for algorithm visualization in class

---

## ⚖️ Comparison with Other Tools

| Feature                | OptiSched | Google Calendar | Excel | OR-Tools | Custom Scripts |
| ---------------------- | --------- | --------------- | ----- | -------- | -------------- |
| Free & Open Source     | ✅        | ✅ UI / ❌ API  | ✅    | ✅       | ✅             |
| Algorithmic Clarity    | ✅        | ❌              | ❌    | ✅       | ⚠️             |
| No Dependencies (Core) | ✅        | ❌              | ❌    | ❌       | ✅             |
| Educational Value      | ✅        | ❌              | ⚠️    | ✅       | ⚠️             |
| Real-Time UI           | ❌        | ✅              | ✅    | ❌       | ❌             |
| Extensible Codebase    | ✅        | ❌              | ❌    | ✅       | ⚠️             |
| Input Validation       | ✅        | ✅              | ❌    | ✅       | ❌             |
| CLI / Scriptable       | ✅        | ❌              | ❌    | ✅       | ✅             |

✅ = Strong fit · ⚠️ = Partial · ❌ = Weak or missing

---

## 🧠 Design Philosophy

- **Simplicity First:** No over-engineering. One file, one job.
- **User-Centric:** `app.py` enables non-programmers to use it easily.
- **Educational:** Clear, teachable code with documentation.
- **Tested:** Every algorithm has unit tests.
- **Extensible:** Add new scheduling strategies in their own files.

---

## 📅 Input Format Rules

### 🗓️ For Interval Scheduling (Meetings)

- Format: `start end` (24-hour format)
- Requirement: `start < end`

Examples:

| Time     | Input |
| -------- | ----- |
| 9:00 AM  | 9     |
| 12:00 PM | 12    |
| 1:00 PM  | 13    |
| 6:00 PM  | 18    |
| 11:00 PM | 23    |

✅ Valid: `9 11`, `13 15`, `8 10`  
❌ Invalid: `12 1` (should be `12 13`), `10 9` (start > end)

---

### 🏭 For Job Shop Scheduling

Each job is a list of operations:  
`(machine_id, duration)` — ordered sequentially.

```python
# Example job:
job_0 = [(0, 3), (1, 2)]  # Use machine 0 for 3 units, then machine 1 for 2
```

---

## 🧪 Testing

To run all unit tests:

```bash
pytest tests/ -v
```

Expected:

```
✅ 5 passed in 0.12s
```

Tests cover:

- Empty inputs
- Overlapping intervals
- All-overlapping or non-overlapping edge cases
- Makespan correctness in job shop scheduling

---

## 📚 Documentation

Check the `docs/` folder for:

- `interval_scheduler.md` – Greedy approach, proof sketch, complexity
- `job_shop_scheduler.md` – Heuristic logic, scheduling visualization

Also see:

- `examples/job_shop_demo.ipynb` – Step-by-step walkthrough

---

## 🧩 Project Structure

```
optisched/
├── scheduling/
│   ├── interval_scheduler.py
│   └── job_shop_scheduler.py
├── examples/
│   ├── demo_interval.py
│   └── job_shop_demo.ipynb
├── tests/
│   ├── test_interval_scheduler.py
│   └── test_job_shop_scheduler.py
├── docs/
│   ├── interval_scheduler.md
│   └── job_shop_scheduler.md
├── data/
│   └── sample_jobs.json
├── app.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 🚀 Future Ideas

- 📊 Gantt chart visualization (matplotlib)
- 💾 Save/load schedules via JSON
- 🌐 Web UI with Streamlit or Flask
- 🔄 Add advanced algorithms: Genetic, Tabu Search
- ⏱️ Support deadlines and priorities
- 🏢 Multi-room scheduling
- 📤 Export to CSV or PDF
- 🐳 Docker support

---

## 🤝 Contributing

Pull requests welcome!

Ideas:

- Add algorithms (e.g., Simulated Annealing)
- Improve CLI/UX
- Add new time formats
- Web frontend integration
- More tests and notebooks

Open an issue or PR to get started.

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

See `LICENSE` file for details.

---

## 👤 Author

**Devansh Singh**  
GitHub: [@Devansh-567](https://github.com/Devansh-567)  
📧 Email: devansh.jay.singh@gmail.com
