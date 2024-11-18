from groq import Groq
from dotenv import load_dotenv
import os

class ResumeGenerator:
    def __init__(self):
        load_dotenv()
        self.client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    
    def generate(self, resume_text, job_desc_text):
        try:
            prompt = f"""
            Based on the following original resume and job description, create an optimized resume:
            
            Original Resume:
            {resume_text}
            
            Job Description:
            {job_desc_text}
            
            Please create a professional resume that highlights relevant experience and skills matching the job description.
            Format it professionally and ensure it's ATS-friendly.
            """
            
            completion = self.client.chat.completions.create(
                model="mixtral-8x7b-32768",  # or any other Groq model you prefer
                messages=[
                    {"role": "system", "content": "You are a professional resume writer."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )
            
            return completion.choices[0].message.content
            
        except Exception as e:
            raise Exception(f"Error generating resume: {str(e)}")