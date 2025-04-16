import streamlit as st
from PIL import Image
import base64

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="Kingsley Mmadubugwu",
    page_icon="🧠",
    layout="wide"
)

def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
        
# Load images once and use base64 for HTML rendering
sidebar_image = get_image_base64("assets/profile_photos/sidebar_image.png")
homepage_image = get_image_base64("assets/profile_photos/profile_image.png")

# ------------------ CUSTOM STYLE ------------------ #
st.markdown("""
    <style>
        /* Existing styles remain the same */
        .profile-pic-container {
            width: 280px;
            height: 280px;
            border-radius: 50%;
            overflow: hidden;
            margin: 20px auto;
            border: 3px solid gold;
            box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
            position: relative;
            transition: transform 0.3s ease;
        }
        /* Add this new class for sidebar image */
        .sidebar-profile-img {
            width: 70% !important;
            height: auto;
            aspect-ratio: 1/1;
            max-width: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid gold;
            margin: 0 auto 20px auto;
             box-shadow: 0 0 15px rgba(255, 215, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR PROFILE ------------------ #
with st.sidebar:
    # Circular profile image using HTML/CSS
    st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{sidebar_image}" class="sidebar-profile-img">
    </div>
    <div style="text-align: center;">
        <h3 style="color: gold; margin: 10px 0 5px 0;">Kingsley</h3>
        <p style="color: white; margin: 0; text-transform: uppercase; 
           letter-spacing: 1px; font-size: 0.9rem;">
            Data Analyst
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
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
    # Use HTML/CSS for circular image with hover effect
    st.markdown(f"""
    <div class="profile-pic-container">
        <img class="circular-img" src="data:image/png;base64,{homepage_image}">
    </div>
    """, unsafe_allow_html=True)

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
