import re

def clean_text(text):
    """Remove special characters and extra whitespace"""
    text = re.sub(r'[^\w\s]', '', text)
    text = ' '.join(text.split())
    return text

def extract_skills(text):
    """Extract common skills from text"""
    # Add your skill keywords dictionary here
    common_skills = ['python', 'java', 'javascript', 'sql', 'aws', 'docker', 'kubernetes']
    found_skills = []
    
    for skill in common_skills:
        if re.search(r'\b' + skill + r'\b', text.lower()):
            found_skills.append(skill)
    
    return found_skills