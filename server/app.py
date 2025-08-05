from flask import Flask, render_template, request
from utils.parser import extract_text_from_pdf
from utils.analyzer import analyze_resume, get_ai_feedback
from utils.matcher import match_jobs
from utils.real_jobs import fetch_real_jobs
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    else:
        return "Unsupported file type", 400

    found, missing = analyze_resume(text)
    feedback = get_ai_feedback(text)

    query_term = found[0] if found else "developer"
    real_jobs = fetch_real_jobs(query_term)

    return render_template('index.html',
                           found=found,
                           missing=missing,
                           feedback=feedback,
                           real_jobs=real_jobs)

if __name__ == '__main__':
    app.run(debug=True)
