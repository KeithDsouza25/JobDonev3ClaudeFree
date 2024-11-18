# JobDone.AI Resume Builder

An AI-powered resume builder and job match analyzer that helps users optimize their resumes for specific job descriptions.

## Features

- Upload resume and job description in various formats (PDF, DOCX, TXT)
- Calculate interview probability score
- Generate word cloud from job description
- Match keywords between resume and job description
- Generate optimized resume using AI

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your OpenAI API key
4. Install spacy model: `python -m spacy download en_core_web_sm`
5. Run the application: `streamlit run app/main.py`

## Requirements

- Python 3.8+
- See requirements.txt for full list of dependencies

## Usage

1. Upload your resume
2. Upload the job description
3. View analysis results
4. Generate optimized resume if desired