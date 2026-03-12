# NHL Player Tracker — Application Layer

This folder contains the **Application Layer** of the NHL Player Tracker project, which ties together the user interface, business logic, and data access layers to create a complete desktop application for exploring NHL player statistics.

---

## 📌 Project Overview

The NHL Player Tracker project is a multi-layered application designed to:

- Store and query NHL player statistics in a local database (SQLite)
- Provide business logic for filtering, sorting, and querying player performance
- Expose a simple graphical user interface (GUI) for browsing players, teams, and historical stats

This directory houses the **Application Layer**, which is responsible for orchestrating the other layers and presenting the functionality to the user.

---

## 🗂️ Folder Structure

- `DAL.py` — Data Access Layer: handles database connections and SQL queries.
- `BLL.py` — Business Logic Layer: processes data, applies rules, and provides abstractions used by the GUI.
- `GUI.py` — Graphical User Interface: provides an interactive interface to browse and search player stats.

> NOTE: For details on the database schema, table structure, and where the data comes from, see `../Data_Layer/README.md`.

---

## ▶️ Running the Application

1. Ensure you have Python installed (3.8+ recommended).
2. Make sure the database file exists and is populated (see `Data_Layer` documentation).
3. Run:

```bash
python GUI.py
```

---

## 📚 Data Sources

All NHL stats are sourced from the official NHL stats site:

- https://www.nhl.com/stats/

---

## 🛠️ Credits

Documentation and README updates were assisted by **GitHub Copilot (Raptor mini)**.
