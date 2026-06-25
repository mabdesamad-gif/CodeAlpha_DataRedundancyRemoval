# 🛡️ Data Redundancy Removal System

A cloud-based system that identifies, classifies, and prevents redundant data from being added to a PostgreSQL cloud database. Built with Flask and deployed on Railway.

---

## 🌐 Live Demo
🔗 [https://web-production-200e6.up.railway.app](https://web-production-200e6.up.railway.app)

---

## 📋 Features

- ✅ **Exact Duplicate Detection** — uses MD5 hashing to instantly detect identical entries
- ⚠️ **Similar Entry Detection** — uses string similarity scoring to catch near-duplicates
- 🔒 **Validation Mechanism** — classifies every entry as ACCEPTED, REJECTED, or FALSE POSITIVE
- ☁️ **Cloud Database** — data stored in PostgreSQL via Supabase (West Europe)
- 🚀 **Cloud Deployment** — live on Railway with environment variable protection

---

## 🧠 How It Works

| Status | Meaning |
|--------|---------|
| ✅ ACCEPTED | Unique data — added to the database |
| ❌ REJECTED | Exact duplicate — blocked by hash check |
| ⚠️ FALSE POSITIVE | Similar entry detected — flagged for review |

---

## 🗂️ Project StructureCodeAlpha_DataRedundancyRemoval/

│── database.py        # PostgreSQL connection & table initialization

│── detector.py        # Hash generation & similarity scoring

│── validator.py       # Validation logic (ACCEPTED/REJECTED/FALSE POSITIVE)

│── app.py             # Flask API & routes

│── templates/

│   └── index.html     # Frontend interface

│── Procfile           # Railway deployment config

│── requirements.txt   # Python dependencies

│── .env               # Environment variables (not pushed to GitHub)

---

## 🛠️ Tech Stack

- **Backend** — Python, Flask
- **Database** — PostgreSQL (Supabase Cloud)
- **Deployment** — Railway
- **Libraries** — psycopg2, python-dotenv, hashlib

---

## ⚙️ Installation (Local)

```bash
# Clone the repo
git clone https://github.com/mabdesamad-gif/CodeAlpha_DataRedundancyRemoval.git
cd CodeAlpha_DataRedundancyRemoval

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "DATABASE_URL=your_postgresql_url" > .env

# Run the app
python app.py
```

---

## 👨‍💻 Author

**Maissoum ABDESMAD**
CodeAlpha Internship — Task 1
