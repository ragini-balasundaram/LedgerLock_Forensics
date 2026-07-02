<div align="center">

# 🔍 Digital Forensics Case Management System

**A Flask Web App for Managing Digital Forensics Cases, Evidence Chain-of-Custody, and Audit-Ready Reporting.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

[Features](#-features) • [Tech Stack](#-tech-stack) • [Screenshots](#-screenshots) • [Setup](#-setup) • [Future Roadmap](#-future-roadmap)

</div>

---

## 🎯 Features

When handling digital evidence, standard spreadsheets are a liability. This application ensures every piece of evidence is tracked, hashed, and audited from seizure to court presentation.

- **Role-Based Access Control:** Granular permissions for Admin, Investigator, Analyst, and Auditor roles.
- **SHA-256 Integrity Verification:** Automatic hash generation on file upload to ensure evidence has not been tampered with.
- **Full Chain-of-Custody Logging:** Active tracking of all evidence handoffs between users, logging the "from," "to," and "purpose" for every transfer.
- **Append-Only Audit Trail:** An immutable backend log tracking every CREATE, UPDATE, and DELETE action for absolute non-repudiation.
- **Court-Ready Reporting:** Generate defensible PDF/HTML reports of cases and evidence history.

---

## 🛠️ Tech Stack

Built with a lightweight, robust architecture focusing on MVC design patterns:

- **Backend:** Python, Flask
- **Database & ORM:** SQLite, SQLAlchemy (Designed for easy PostgreSQL migration)
- **Frontend:** HTML5, Jinja2 Templates, Bootstrap
- **Testing & Deployment:** Pytest, Docker

---

## 📸 Screenshots


<div align="center">

  <p><i>Dashboard showing open cases and recent alerts.</i></p>
  
  <img width="959" height="500" alt="Screenshot 2026-07-01 000155" src="https://github.com/user-attachments/assets/0b6f80b5-7578-4165-88c4-42929c53acd1" />
  <br>


  <p><i>Initialise new secure evidence to establish chain of custody</i></p>
  <img width="958" height="503" alt="Screenshot 2026-07-01 000246" src="https://github.com/user-attachments/assets/a3becb97-bfef-4c5f-8073-7cb4291e172d" />
  
</div>

---

## 🚀 Setup

Follow these instructions to run the application locally.

### 1. Clone the repository
```bash
git clone [https://github.com/ragini-balasundaram/LedgerLock_Forensics.git](https://github.com/ragini-balasundaram/LedgerLock_Forensics.git)
cd LedgerLock_Forensics
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your secrets:
```bash
SECRET_KEY=your-random-secret-key-here
DATABASE_URL=sqlite:///instance/dfir.db
```

### 5. Run the application
```bash
flask --app run.py run --debug
```
> The application will be running at `http://127.0.0.1:5000`

---

## 🏗️ Architecture

Below is a high-level view of the application's Request Lifecycle:

```text
Browser sends request
   |
   ▼
Flask matches URL → route function (Controller)
   |
   ▼
Route queries Database via Model (SQLAlchemy)
   |
   ▼
Route renders Template (Jinja) with the data
   |
   ▼
HTML sent back to Browser
```

---

## 🛣️ Future Roadmap

- Integrate hash verification against the **VirusTotal API**.
- Implement Multi-Factor Authentication (MFA).
- Migrate from SQLite to **PostgreSQL** for high-concurrency environments.
- Migrate evidence file storage from local disk to **AWS S3**.
- Add digital signatures to generated PDF reports.

---
<div align="center">
  <i>Designed for security. Built for the courtroom.</i>
</div>
