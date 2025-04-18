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
        .project-filters {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-bottom: 3rem;
        }
        .filter-btn {
            background: none;
            border: 2px solid gold;
            color: gold;
            padding: 0.8rem 2rem;
            border-radius: 30px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .filter-btn.active, .filter-btn:hover {
            background: gold;
            color: #0f0f0f !important;
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            padding: 0 2rem;
        }
        .project-card {
            background: #1a1a1a;
            border-radius: 15px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-image {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-bottom: 3px solid gold;
        }
        .project-content {
            padding: 1.5rem;
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
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="projects-header">Recent Work</div>', unsafe_allow_html=True)
    
    # Project Filters
    st.markdown("""
    <div class="project-filters">
        <button class="filter-btn active">All</button>
        <button class="filter-btn">Graphic Design</button>
        <button class="filter-btn">Web Design</button>
        <button class="filter-btn">Software</button>
        <button class="filter-btn">Apps</button>
    </div>
    """, unsafe_allow_html=True)

    # Project Grid
    projects = [
        {
            "title": "E-commerce Platform",
            "category": "Web Design",
            "image": "url_to_image_1",
            "description": "Modern online shopping platform with integrated payment processing"
        },
        {
            "title": "Mobile Fitness App",
            "category": "Apps",
            "image": "url_to_image_2",
            "description": "AI-powered workout companion with progress tracking"
        },
        {
            "title": "Dashboard System",
            "category": "Software",
            "image": "url_to_image_3",
            "description": "Data visualization suite for enterprise analytics"
        },
        {
            "title": "Brand Identity",
            "category": "Graphic Design",
            "image": "url_to_image_4",
            "description": "Complete visual identity package for tech startup"
        }
    ]

    st.markdown('<div class="project-grid">', unsafe_allow_html=True)
    for project in projects:
        st.markdown(f"""
        <div class="project-card">
            <img src="{project['image']}" class="project-image">
            <div class="project-content">
                <div class="project-category">{project['category']}</div>
                <h3 class="project-title">{project['title']}</h3>
                <p class="project-description">{project['description']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Add to your app
projects_section()