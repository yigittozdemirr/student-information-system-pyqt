# Student Information System

[![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/GUI-PyQt5-41CD52?style=flat-square&logo=qt&logoColor=white)](https://www.riverbankcomputing.com/software/pyqt/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

A desktop application for managing student records and grades, built with Python and PyQt5 on a SQLite database. The interface is in Turkish.

## Features

**Administrator**

- Add, update and delete student records and grades
- Search students and view all records in a table

**Student**

- Register and sign in with a student ID and password
- View courses, midterm and final grades, and the calculated average
- See classmates in the same department
- Update personal information

**Grade calculation**

Each course grade is 40% midterm and 60% final. The overall average is the mean of the three courses, shown on both the 100-point and 4-point scales.

## Tech stack

| Area | Technology |
| --- | --- |
| Language | Python 3 |
| Interface | PyQt5, Qt Designer |
| Database | SQLite (`sqlite3` from the standard library) |

## Getting started

### 1. Clone and install

```bash
git clone https://github.com/yigittozdemirr/student-information-system-pyqt.git
cd student-information-system-pyqt
pip install PyQt5
```

### 2. Create the database

The database file is not stored in the repository. Create `database/veri.db`, for example with [DB Browser for SQLite](https://sqlitebrowser.org/), and run the following SQL:

```sql
CREATE TABLE bolumler (
  bolumid INTEGER PRIMARY KEY,
  bolumad TEXT NOT NULL
);
CREATE TABLE dersler (
  dersid  INTEGER PRIMARY KEY,
  dersad  TEXT NOT NULL,
  bolumid INTEGER NOT NULL REFERENCES bolumler(bolumid)
);
CREATE TABLE ogrenciler (
  ogrenciid    TEXT PRIMARY KEY,
  ogrenciad    TEXT NOT NULL,
  ogrencisoyad TEXT NOT NULL,
  sifre        TEXT NOT NULL,
  bolumid      INTEGER NOT NULL REFERENCES bolumler(bolumid)
);
CREATE TABLE notlar (
  ogrenciid TEXT PRIMARY KEY REFERENCES ogrenciler(ogrenciid),
  vizenot1 REAL, vizenot2 REAL, vizenot3 REAL,
  finalnot1 REAL, finalnot2 REAL, finalnot3 REAL
);

INSERT INTO bolumler VALUES
  (1, 'Yazılım Mühendisliği'),
  (2, 'Makine Mühendisliği'),
  (3, 'Endüstri Mühendisliği');

-- Each department needs at least three courses. Replace these sample names.
INSERT INTO dersler (dersad, bolumid) VALUES
  ('Ders 1', 1), ('Ders 2', 1), ('Ders 3', 1),
  ('Ders 1', 2), ('Ders 2', 2), ('Ders 3', 2),
  ('Ders 1', 3), ('Ders 2', 3), ('Ders 3', 3);

-- The account with ID 999 is the administrator. Choose your own password.
INSERT INTO ogrenciler VALUES ('999', 'Admin', 'User', 'change-me', 1);
```

### 3. Run

```bash
python src/uygulama_v1.py
```

> **Note:** This is an educational project. Passwords are stored as plain text, so do not use it with real credentials.

## Project structure

```text
.
├── src/
│   ├── uygulama_v1.py   # Application entry point and logic
│   ├── obs.py           # Interface generated from ui/obs.ui
│   └── don.py           # Regenerates the interface code
├── ui/
│   ├── obs.ui           # Qt Designer file
│   └── veri.sqbpro      # DB Browser for SQLite project
└── database/            # Create this folder for veri.db (not tracked by Git)
```

## Author

**Yiğit Özdemir**: [@yigittozdemirr](https://github.com/yigittozdemirr)
