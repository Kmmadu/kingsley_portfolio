import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# ------------------ PAGE CONFIG ------------------ #
st.set_page_config(
    page_title="About | Kingsley Mmadubugwu",
    page_icon="🧠",
    layout="wide"
)

# ------------------ CUSTOM STYLE ------------------ #
st.markdown("""
    <style>
        .main {
            background-color: #0f0f0f;
            color: white;
        }
        .about-header {
            font-size: 2.5rem;
            color: gold;
            text-align: center;
            margin-bottom: 3rem;
        }
        .bio-text {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #cccccc;
        }
        .service-card {
            background: #1a1a1a;
            padding: 2rem;
            border-radius: 10px;
            text-align: center;
            margin: 1rem;
            transition: transform 0.3s;
        }
        .service-card:hover {
            transform: translateY(-5px);
        }
        .service-icon {
            font-size: 2.5rem;
            color: gold;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER SECTION ------------------ #
st.markdown("<h1 class='about-header'>ABOUT US</h1>", unsafe_html=True)

# ------------------ BIO SECTION ------------------ #
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    # Replace with your actual image path
    img = Image.open("assets/profile_photos/profile_image.png")
    st.image(img, caption="", width=350)

with col2:
    st.markdown("<h2 style='color: gold; margin-bottom: 2rem;'>WHO AM I?</h2>", unsafe_html=True)
    st.markdown("""
        <p class='bio-text'>
        Hi I'm Kingsley Mmadubugwu. I transform complex data into actionable insights that drive business growth. 
        With a unique blend of technical expertise and strategic thinking, I bridge the gap between raw data and 
        operational efficiency.
        </p>
        <p class='bio-text'>
        My journey in data science began with a passion for problem-solving and has evolved into a career marked by 
        successful projects across multiple industries. I specialize in creating robust data pipelines, developing 
        predictive models, and designing intuitive data visualizations.
        </p>
    """, unsafe_html=True)

# ------------------ SERVICES SECTION ------------------ #
st.markdown("<br><br>", unsafe_html=True)
st.markdown("<h2 style='color: gold; text-align: center; margin-bottom: 3rem;'>Core Services</h2>", unsafe_html=True)

# Service Cards
col3, col4, col5, col6 = st.columns(4)

services = [
    {"icon": "📊", "title": "Data Analysis", 
     "desc": "Advanced analytics and business intelligence solutions"},
    {"icon": "🐍", "title": "Python Development", 
     "desc": "Custom automation scripts and application development"},
    {"icon": "🗄️", "title": "Database Management", 
     "desc": "Optimized database architectures & cloud solutions"},
    {"icon": "🤖", "title": "ML Solutions", 
     "desc": "Predictive modeling & AI integration"}
]

with col3:
    components.html(f"""
        <div class='service-card'>
            <div class='service-icon'>{services[0]['icon']}</div>
            <h3>{services[0]['title']}</h3>
            <p>{services[0]['desc']}</p>
        </div>
    """, height=250)

with col4:
    components.html(f"""
        <div class='service-card'>
            <div class='service-icon'>{services[1]['icon']}</div>
            <h3>{services[1]['title']}</h3>
            <p>{services[1]['desc']}</p>
        </div>
    """, height=250)

with col5:
    components.html(f"""
        <div class='service-card'>
            <div class='service-icon'>{services[2]['icon']}</div>
            <h3>{services[2]['title']}</h3>
            <p>{services[2]['desc']}</p>
        </div>
    """, height=250)

with col6:
    components.html(f"""
        <div class='service-card'>
            <div class='service-icon'>{services[3]['icon']}</div>
            <h3>{services[3]['title']}</h3>
            <p>{services[3]['desc']}</p>
        </div>
    """, height=250)

# ------------------ FOOTER ------------------ #
st.markdown("---")
st.markdown("<p style='text-align:center; color: #888;'>© 2025 Kingsley Mmadubugwu</p>", unsafe_html=True)