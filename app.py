# app.py
import streamlit as st
import base64

st.set_page_config(page_title="The Girl on the Train — A Gift for You", layout="centered")

# Elegant dark theme
theme_css = """
<style>
body {
    background-color: #1a1a1a;
}

html, body, [class*="css"] {
    font-family: 'Georgia', serif;
    color: #fdf0f5;
}

.stApp {
    background: linear-gradient(to bottom right, #2a1a1f, #1a0f12);
    padding: 2.5rem;
    border-radius: 1rem;
    box-shadow: 0 0 40px rgba(255, 182, 193, 0.08);
    max-width: 800px;
    margin: auto;
}

h1 {
    color: #ffccd5;
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

h3 {
    color: #f8bac2;
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 2rem;
}

.stMarkdown {
    font-size: 1.1rem;
    color: #f4e8ec;
    line-height: 1.6;
}

iframe {
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(255, 192, 203, 0.2);
}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# Headings
st.markdown("## 🌹 *The Girl on the Train*")
st.markdown("#### *A book I would’ve handed to you in person...*")

# Polished message
st.markdown(
"""
I really wanted to walk into a bookstore, scan the shelves, pick up different books, and hand you something that felt like *you*.  
But life had other plans.  

So instead — here’s the digital version of the story I picked just for you.  
One filled with shadows, intrigue, and everything you'd love sinking into on a quiet evening.  

Hope this brings a little thrill, a little calm, and a little *you time*.  
Happy World Book Day 💫
"""
)

# Load and show the book
PDF_PATH = "the-girl-on-the-train_compressed-compressed.pdf"

try:
    with open(PDF_PATH, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="700px" type="application/pdf"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
        st.success("Your story awaits. 📖")
except FileNotFoundError:
    st.error("Oops — the book file isn't found. Make sure it's named `the_girl_on_the_train.pdf`.")
