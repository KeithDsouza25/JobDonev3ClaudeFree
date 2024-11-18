import streamlit as st
from file_processor.pdf_reader import PDFReader
from file_processor.docx_reader import DocxReader
from file_processor.text_reader import TextReader
from analyzers.score_calculator import ScoreCalculator
from analyzers.word_cloud_generator import WordCloudGenerator
from analyzers.keyword_matcher import KeywordMatcher
from resume_generator.ai_generator import ResumeGenerator

def set_page_config():
    st.set_page_config(
        page_title="JobDone.AI Resume Analyzer",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={
            'Get Help': 'mailto:kdmusic2509@gmail.com',
            'Report a bug': 'mailto:kdmusic2509@gmail.com',
            'About': '''
            ## JobDone.AI Resume Analyzer
            An AI-powered tool to optimize your resume for job applications.
            
            Version: 1.0.0
            Contact: kdmusic2509@gmail.com
            '''
        }
    )

def load_css():
    with open('app/static/css/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

class ResumeBuilderApp:
    def __init__(self):
        self.supported_formats = ['.pdf', '.docx', '.txt']
        
    def run(self):
        set_page_config()
        load_css()
        
        # Update to use st.query_params instead of experimental_get_query_params
        page = st.query_params.get("page", "home")
        
        if page == "services":
            self.show_services_page()
        elif page == "about":
            self.show_about_page()
        else:
            self.show_main_page()

    def show_services_page(self):
        st.markdown('<h1 class="main-title">Our Services</h1>', unsafe_allow_html=True)
        # Add your services content here

    def show_about_page(self):
        st.markdown('<h1 class="main-title">About Us</h1>', unsafe_allow_html=True)
        # Add your about content here

    def show_main_page(self):
        # Your existing main page content
        st.markdown('<h1 class="main-title">Resume Analyzer</h1>', unsafe_allow_html=True)
        st.markdown('<h3 class="subtitle">Optimize your resume for your dream job</h3>', unsafe_allow_html=True)
        
        # Create two columns with spacing
        col1, space, col2 = st.columns([4, 1, 4])
        
        with col1:
            st.markdown('<div class="upload-section">', unsafe_allow_html=True)
            st.markdown('<p class="upload-label">📄 Upload Resume</p>', unsafe_allow_html=True)
            
            # File upload option first
            resume_file = st.file_uploader("Upload resume file", type=self.supported_formats, key="resume")
            
            # Text area below file upload
            st.markdown('<p class="text-label">Or paste resume text here:</p>', unsafe_allow_html=True)
            resume_text_input = st.text_area("", height=200, key="resume_text", label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="upload-section">', unsafe_allow_html=True)
            st.markdown('<p class="upload-label">📋 Upload Job Description</p>', unsafe_allow_html=True)
            
            # File upload option first
            job_desc_file = st.file_uploader("Upload job description file", type=self.supported_formats, key="job_desc")
            
            # Text area below file upload
            st.markdown('<p class="text-label">Or paste job description here:</p>', unsafe_allow_html=True)
            job_desc_text_input = st.text_area("", height=200, key="job_desc_text", label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

        # Update the processing logic to handle both file and text input
        resume_text = ""
        job_desc_text = ""
        
        if resume_file:
            resume_text = self._process_file(resume_file)
        elif resume_text_input:
            resume_text = resume_text_input
            
        if job_desc_file:
            job_desc_text = self._process_file(job_desc_file)
        elif job_desc_text_input:
            job_desc_text = job_desc_text_input

        # Process files and show analysis
        if (resume_text and job_desc_text):
            st.markdown("---")
            
            # Analysis results in columns
            col1, col2 = st.columns(2)
            
            with col1:
                score_calculator = ScoreCalculator()
                match_score = score_calculator.calculate_score(resume_text, job_desc_text)
                st.metric("Match Score", f"{match_score}/10")
                
                keyword_matcher = KeywordMatcher()
                matching_keywords = keyword_matcher.find_matches(resume_text, job_desc_text)
                st.write("#### Matching Keywords")
                st.write(", ".join(matching_keywords['found']))
            
            with col2:
                word_cloud = WordCloudGenerator()
                word_cloud_image = word_cloud.generate(job_desc_text)
                st.image(word_cloud_image, caption="Key Terms Word Cloud")
            
            if st.button("Generate Optimized Resume"):
                with st.spinner("Generating optimized resume..."):
                    resume_gen = ResumeGenerator()
                    optimized_resume = resume_gen.generate(resume_text, job_desc_text)
                    st.download_button(
                        "📥 Download Optimized Resume",
                        optimized_resume,
                        file_name="optimized_resume.docx"
                    )

    def _process_file(self, file):
        file_ext = file.name.split('.')[-1].lower()
        if file_ext == 'pdf':
            return PDFReader().read(file)
        elif file_ext == 'docx':
            return DocxReader().read(file)
        else:
            return TextReader().read(file)

if __name__ == "__main__":
    app = ResumeBuilderApp()
    app.run()