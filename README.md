# RESUME_SHORTLISTING_AI
🧠 AI Resume Shortlisting System

An intelligent web application that automatically analyzes and ranks resumes based on their similarity to a given job description using AI and NLP models.

🚀 Features

✅ Upload multiple resumes (PDF format).
✅ Automatically extract and process resume text using PyMuPDF and NLTK.
✅ Compare resumes against a job description using a machine learning model.
✅ Display ranked results with visually appealing score bars.
✅ Simple and elegant UI with glassmorphism design.

🛠️ Tech Stack

Frontend:

HTML5, CSS3, Bootstrap

Backend:

Python (Flask Framework)

AI / NLP Tools:

scikit-learn

nltk

PyMuPDF (fitz)

Others:

Jinja2 (for dynamic HTML rendering)

📁 Project Structure
RESUME_SHORTLISTING_AI/
│
├── app.py                     # Main Flask application
├── resume_model.pkl           # Trained ML model for shortlisting
├── requirements.txt           # Required dependencies
│
├── templates/                 # HTML templates
│   ├── index.html             # Upload page
│   └── result.html            # Result display page
│
├── static/                    # (Optional) CSS or JS files
│
├── utils/                     # Helper scripts
│   ├── text_extraction.py     # Extract text from PDF resumes
│   ├── preprocessing.py       # Clean and preprocess text
│
└── uploads/                   # Uploaded resumes (temporary storage)

⚙️ Installation

Clone this repository

git clone https://github.com/your-username/AI-Resume-Shortlisting.git
cd AI-Resume-Shortlisting


Create and activate virtual environment

python -m venv venv
venv\Scripts\activate     # For Windows
source venv/bin/activate  # For macOS/Linux


Install dependencies

pip install -r requirements.txt


Run the Flask app

python app.py


Open in browser

http://127.0.0.1:5000

📊 Output Preview

Upload resumes and a job description.

Get a ranked list with matching percentages and a Top Match badge for best candidates.

Visually interactive score bars for each candidate.
