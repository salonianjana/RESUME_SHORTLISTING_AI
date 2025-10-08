from flask import Flask, render_template, request
import os
from utils.text_extraction import extract_text
from utils.preprocessing import clean_text
from utils.keyword_matching import match_score

UPLOAD_FOLDER = 'uploads'
os.makedirs(os.path.join(UPLOAD_FOLDER, 'resumes'), exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shortlist', methods=['POST'])
def shortlist():
    jd_text = request.form['job_description']  # ✅ Direct text input
    jd_text = clean_text(jd_text)

    resumes = request.files.getlist('resumes')
    results = []

    for resume in resumes:
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resumes', resume.filename)
        resume.save(resume_path)
        resume_text = clean_text(extract_text(resume_path))
        score = match_score(jd_text, resume_text)
        results.append({'name': resume.filename, 'score': score})

    # Sort by match score descending
    results.sort(key=lambda x: x['score'], reverse=True)

    return render_template('result.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
