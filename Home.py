import streamlit as st
from PIL import Image

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="Kingsley Mmadubugwu",
    page_icon="🧠",
    layout="wide"
)

# ------------------ LOAD IMAGES ------------------ #
homepage_image = Image.open("assets/profile_photos/profile_image.png")  # Homepage
sidebar_image = Image.open("assets/profile_photos/sidebar_image.png")   # Sidebar

# ------------------ CUSTOM STYLE ------------------ #
st.markdown("""
    <style>
        .main {
            background-color: #0f0f0f;
            color: white;
        }
        h1, h3, p {
            font-family: 'Segoe UI', sans-serif;
        }
        .work-title {
            color: gold;
            font-size: 1.8rem;
            text-align: center;
            font-weight: bold;
            margin-top: 3rem;
        }
        .profile-pic-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 30px;
        }
        .circular-img {
            border-radius: 50%;
            width: 280px;
            height: 280px;
            object-fit: cover;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR PROFILE ------------------ #
# Add to sidebar
with st.sidebar:
    # Profile Image
    st.image(sidebar_image, width=150)  # Adjust width as needed
    
    # Name and Title
    st.markdown("""
    <div style="text-align: center;">
        <h3 style="color: gold; margin: 10px 0 5px 0;">Kingsley</h3>
        <p style="color: white; margin: 0;">Data Analyst</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------ HERO SECTION ------------------ #
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("""
        <h3 style='color: gold;'>Data Analyst | Python Developer | Database Manager</h3>
        <h1 style='font-size: 3rem; font-weight: bold; color: white;'>Hi, I am Kingsley</h1>
        <p style='font-size: 1.2rem; color: #dddddd;'>
            I help businesses and organizations make better decisions using data-driven insights.<br>
            My mission is to design data systems and tools that are beautiful, functional, and effective.
        </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""<div class="profile-pic-container">""", unsafe_allow_html=True)
    st.image(homepage_image, width=280)
    st.markdown("""</div>""", unsafe_allow_html=True)

# ------------------ CONTACT BUTTONS ------------------ #
st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <a href="https://wa.me/2349076055774" target="_blank"
           style="display: inline-block; padding: 12px 24px; background-color: #25D366; color: white; border-radius: 30px; text-decoration: none; font-weight: bold; margin-right: 15px;">
            <i class="fab fa-whatsapp"></i> LET'S CHAT ON WHATSAPP
        </a>
        <a href="mailto:mmadubugwukingsley@gmail.com" target="_blank"
           style="display: inline-block; padding: 12px 24px; border: 2px solid white; color: white; border-radius: 30px; text-decoration: none; font-weight: bold;">
            <i class="fas fa-envelope"></i> OR SEND ME AN EMAIL
        </a>
    </div>
""", unsafe_allow_html=True)

# ------------------ FOOTER ------------------ #
st.markdown("---")
st.markdown("<p style='text-align:center; color: #888;'>© 2025 Kingsley Mmadubugwu</p>", unsafe_allow_html=True)
