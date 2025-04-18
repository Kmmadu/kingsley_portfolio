import streamlit as st

def education_page():
    st.markdown("""
        <style>
        .accordion-container {
            background: #f4f4f4;
            border: 1px solid #ddd;
            border-radius: 5px;
            margin-bottom: 10px;
            font-family: 'Segoe UI', sans-serif;
        }
        .accordion-header {
            background-color: #3498db;
            color: white;
            padding: 1rem;
            cursor: pointer;
            font-weight: bold;
            text-transform: uppercase;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .accordion-header:hover {
            background-color: #2980b9;
        }
        .accordion-content {
            background-color: white;
            padding: 1rem 1.5rem;
            color: #333;
            border-top: 1px solid #ddd;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🎓 Education")

    # Education data
    education_data = [
        {
            "title": "MASTER DEGREE GRAPHIC DESIGN",
            "text": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean."
        },
        {
            "title": "BACHELOR DEGREE OF COMPUTER SCIENCE",
            "text": "Completed with distinction, focused on software development, algorithms, and systems design."
        },
        {
            "title": "DIPLOMA IN INFORMATION TECHNOLOGY",
            "text": "Hands-on training in networking, IT infrastructure, and basic web development."
        },
        {
            "title": "DIPLOMA IN INFORMATION TECHNOLOGY",
            "text": "Advanced topics in cloud computing and database management."
        },
        {
            "title": "HIGH SCHOOL SECONDARY EDUCATION",
            "text": "Graduated with strong foundations in science and mathematics."
        }
    ]

    # State tracking using session_state
    if 'active_accordion' not in st.session_state:
        st.session_state.active_accordion = 0  # default open the first one

    # Accordion rendering
    for idx, item in enumerate(education_data):
        is_open = st.session_state.active_accordion == idx

        header_clicked = st.button(f"{item['title']} {'–' if is_open else '+'}", key=f"accordion-{idx}")

        if header_clicked:
            if is_open:
                st.session_state.active_accordion = -1  # collapse all
            else:
                st.session_state.active_accordion = idx

        if is_open:
            st.markdown(f"""
                <div class="accordion-container">
                    <div class="accordion-content">
                        {item['text']}
                    </div>
                </div>
            """, unsafe_allow_html=True)

# Run the function
education_page()
