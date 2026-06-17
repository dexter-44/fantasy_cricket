# fantasy_cricket
# Desktop Fantasy Cricket Team Selector

A desktop Graphic User Interface (GUI) sport-management simulation engine built using **Python 3**, **PyQt5**, and an optimized **SQLite3** relational database database layer. This program enables users to create custom digital rosters under salary cap constraints, query real-time statistical metrics split by player roles, and store custom performance evaluation vectors.

---

## 🚀 Architectural & System Features

- **Relational Schema Partitioning:** Employs a structured 3-table layout inside `players.db` (`stats`, `teams`, and `match`) to manage lifetime variables alongside specific game-day data splits.
- **Dynamic Filter Binding:** Connects interactive toggle matrix controls (`BAT`, `BOW`, `AR`, `WK`) directly to structural database search cursors, minimizing background memory processing.
- **Automated State Tracking:** Automatically keeps tabs on available salary budget limits and spent team metrics as player blocks move dynamically between left and right selector lists.

---

## 📊 Relational Database Design Topology

The persistence model relies on three structural tables configured via `database.py`:

* **`stats` Table:** Anchors baseline primary identity data (`player`, `matches`, `runs`, `100s`, `50s`, `value`, `ctg`).
* **`teams` Table:** Tracks personalized user selections (`name`, `players`, `value`).
* **`match` Table:** Contains individual point-scoring granular variables used to run calculation scripts (`scored`, `faced`, `fours`, `sixes`, `wkts`, `catches`, etc.).

---

## 🛠️ System Prerequisites

Your environment requires a Python 3.x interpreter distribution alongside the PyQt5 layout module. Install the missing runtime blocks via pip:

pip install PyQt5

💻 How to Run the Program
1.Clone the Repository:
git clone [https://github.com/YOUR_USERNAME/Fantasy-Cricket-App.git](https://github.com/YOUR_USERNAME/Fantasy-Cricket-App.git)
cd Fantasy-Cricket-App

2.Initialize and Boot the Application:
Run the master view script directly through your console terminal window:
python main.py

3.Core Workflow Mapping:
a)New Roster Initialization: Use the "Manage Teams" menu header, click NEW Team, and feed a clean identifier handle inside the modal prompt input box.

b)Player Allocation Pools: Click the category radio selectors to load lists dynamically from players.db. Click names to transition items across vectors.

c)Performance Evaluations: Select EVALUATE Team to systematically audit final lineups against current point metric weighting modules.

⚙️ Project Component Manifest
a)main.py: Manages parent window parameters, list widget event bindings, error dialog boxes, and contextual calculations.

b)database.py: Dedicated structural pipeline component managing database file system verification checks, raw boilerplate inserts, and secure table schema definition generation.

c)players.db: Relational storage engine holding player stats, history tracking rows, and saved teams.
