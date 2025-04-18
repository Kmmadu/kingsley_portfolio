import streamlit as st

def projects_section():
    st.markdown("""
    <style>
        .projects-header {
            font-size: 2.5rem;
            color: gold;
            text-align: center;
            margin: 3rem 0 2rem 0;
            text-transform: uppercase;
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            padding: 0 1rem;
        }
        .project-card {
            background: #1a1a1a;
            border-radius: 15px;
            overflow: hidden;
            transition: transform 0.3s ease;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-bottom: 3px solid gold;
            transition: transform 0.3s ease-in-out;
        }
        .project-image:hover {
            transform: scale(1.05);
        }
        .project-content {
            padding: 1.2rem;
        }
        .project-category {
            color: gold;
            font-size: 0.9rem;
            text-transform: uppercase;
        }
        .project-title {
            color: white;
            margin: 0.5rem 0;
            font-size: 1.3rem;
        }
        .project-description {
            color: #ddd;
            font-size: 0.95rem;
            line-height: 1.5;
        }
        @media (max-width: 600px) {
            .project-title {
                font-size: 1.1rem;
            }
            .project-description {
                font-size: 0.9rem;
            }
        }
        /* Highlight selected filter */
        div[data-baseweb="radio"] > div > div {
            justify-content: center;
            gap: 1.5rem;
        }
        div[data-baseweb="radio"] label[data-selected="true"] {
            color: gold !important;
            font-weight: bold;
            border-bottom: 2px solid gold;
            padding-bottom: 2px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="projects-header">Recent Work</div>', unsafe_allow_html=True)
    
    # Add spacing above filter
    st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)

    # Filter Options
    filter_options = ["All", "Data Analysis", "Dashboards", "Database Management", "Python Projects", "Collaborations"]
    selected_filter = st.radio("Filter by category:", filter_options, horizontal=True, label_visibility="collapsed")

    # Projects
    projects = [
        {
            "title": "Internet Companies Data Analysis",
            "category": "Data Analysis",
            "image": "https://raw.githubusercontent.com/Kmmadu/internet-companies-dashboard/main/images/preview.png",
            "description": "Interactive dashboard analyzing top global internet companies using Streamlit.",
            "url": "https://kmmadu-internet-companies-dashboard.streamlit.app/"
        },
        {
            "title": "NCC Bandwidth Report",
            "category": "Dashboards",
            "image": "https://placehold.co/600x400?text=NCC+Dashboard",
            "description": "Power BI dashboard for bandwidth allocation and customer segmentation.",
            "url": "https://app.powerbi.com/view?r=some_fake_link"
        },
        {
            "title": "Router_base DB System",
            "category": "Database Management",
            "image": "https://placehold.co/600x400?text=Router+DB",
            "description": "Designed and managed a two-table structure for ISP data storage.",
            "url": "https://github.com/Kmmadu/router_base"
        },
        {
            "title": "Web Scraping Project",
            "category": "Python Projects",
            "image": "https://placehold.co/600x400?text=Web+Scraping",
            "description": "Scraped and cleaned market data using Python (requests, BeautifulSoup, pandas).",
            "url": "https://github.com/Kmmadu/web-scraping-internet-companies"
        },
        {
            "title": "ALX Capstone Collaboration",
            "category": "Collaborations",
            "image": "https://placehold.co/600x400?text=ALX+Teamwork",
            "description": "Teamed up to deliver an end-to-end data storytelling project for scholarship program.",
            "url": "https://github.com/Kmmadu/alx-capstone"
        }
    ]

    # Filter projects
    filtered_projects = projects if selected_filter == "All" else [p for p in projects if p["category"] == selected_filter]

    # Display filtered projects
    st.markdown('<div class="project-grid">', unsafe_allow_html=True)
    for project in filtered_projects:
        st.markdown(f"""
        <a href="{project['url']}" target="_blank" style="text-decoration: none;">
            <div class="project-card">
                <img src="{project['image']}" class="project-image">
                <div class="project-content">
                    <div class="project-category">{project['category']}</div>
                    <h3 class="project-title">{project['title']}</h3>
                    <p class="project-description">{project['description']}</p>
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Call the function in your Streamlit app
projects_section()
