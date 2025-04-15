import streamlit as st
from utils.load_lottie import load_lottieurl
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Kingsley Mmadubugwu",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="auto"
)

# Font Awesome Icons for footer
components.html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", height=0)

# Main Title with gold styling
st.markdown("""
<h1 style="text-align: center;">
I'm <span style="color: gold; font-weight: bold;">Kingsley Mmadubugwu</span>
</h1>
""", unsafe_allow_html=True)

st.subheader(" Data Analyst |  Python Developer |  Database Manager")

# Lottie Animation
lottie_url = "https://assets5.lottiefiles.com/packages/lf20_jtbfg2nb.json"
components.html(
    f"""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player 
        src="{lottie_url}" 
        background="transparent" 
        speed="1"
        style="width: 100%; max-width: 300px; margin: 0 auto;"
        loop 
        autoplay>
    </lottie-player>
    """,
    height=300,
)

st.markdown("---")

# Explore My Work Section (Responsive Grid)
components.html("""
<style>
  /* Hide on mobile */
  @media screen and (max-width: 768px) {
    .work-section {
      display: none;
    }
  }

  .work-title {
    color: white !important;
    font-weight: 700 !important;
    font-family: 'Source Sans Pro', sans-serif;
    text-align: center;
    margin-bottom: 1.5rem !important;
    font-size: 1.5rem !important;
  }

  .work-section {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 15px;
    text-align: center;
    margin: 0 auto 10px auto; /* Reduced bottom space here */
    max-width: 800px;
  }

  .work-link {
    display: block;
    padding: 12px;
    background-color: #f0f2f6;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 600;
    color: #262730;
    transition: 0.3s;
    font-family: 'Source Sans Pro', sans-serif;
  }

  .work-link:hover {
    background-color: #dbe6f5;
    transform: translateY(-2px);
  }
</style>

<h3 class="work-title"> Explore My Work</h3>
<div class="work-section">
  <a class="work-link" href="/About" target="_self"> About Me</a>
  <a class="work-link" href="/Projects" target="_self"> Projects</a>
  <a class="work-link" href="/Books" target="_self"> My Books</a>
  <a class="work-link" href="/Certifications" target="_self"> Certifications</a>
</div>
""", height=270)  # Reduced from 300 to 270

# Footer
st.markdown("---")

components.html("""
<div style="text-align: center; margin-top: 10px;">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

    <a href="https://wa.me/2349076055774" target="_blank" 
       style="display: inline-block; padding: 12px 20px; margin: 10px; background-color: #25D366; color: white; border-radius: 30px; text-decoration: none; font-weight: bold; font-family: sans-serif;">
        <i class="fab fa-whatsapp" style="margin-right: 8px;"></i> LET'S CHAT ON WHATSAPP
    </a>

    <a href="mailto:mmadubugwukingsley@gmail.com" target="_blank" 
       style="display: inline-block; padding: 12px 20px; margin: 10px; background-color: transparent; color: #EA4335; border: 2px solid #EA4335; border-radius: 30px; text-decoration: none; font-weight: bold; font-family: sans-serif;">
        <i class="fas fa-envelope" style="margin-right: 8px;"></i> OR SEND ME AN EMAIL
    </a>
</div>
""", height=150)
