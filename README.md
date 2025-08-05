# Resume Analyzer

A smart resume analyzer and job matcher built using **Python (Flask)**. This tool parses resumes, analyzes skills, matches job roles, and displays relevant job recommendations.

---

## 🚀 Features

- 📝 **Resume Parsing** – Extracts data from uploaded resumes (PDF/DOCX)
- 🧠 **Skill & Job Role Analyzer** – Matches resume contents with predefined job roles
- 🔎 **Real Job Fetching** – Retrieves and recommends real-time job opportunities (from JSON or APIs)
- 💡 **User-Friendly Interface** – Built with HTML/CSS and Flask templating

---

## 📁 Project Structure

```
resume-analyzer/
└── server/
    ├── app.py                    # Main Flask application
    ├── data/
    │   └── job_roles.json        # Static job roles data
    ├── static/
    │   └── style.css             # Styling for frontend
    ├── templates/
    │   └── index.html            # Web UI template
    └── utils/
        ├── analyzer.py           # Core logic to analyze resumes
        ├── matcher.py            # Matches skills to job roles
        ├── parser.py             # Resume parsing script
        └── real_jobs.py          # Optional: integration with job data source
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer/server
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate   # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not available, manually install Flask:
```bash
pip install flask
```

---

## ▶️ Running the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 📌 Future Improvements

- Integration with real job APIs (e.g., Indeed, LinkedIn)
- ATS (Applicant Tracking System) score prediction
- Admin panel to manage job roles

---


## 🙌 Contributing

Feel free to fork this repo and raise PRs. Suggestions and improvements are welcome!

