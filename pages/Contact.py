import streamlit as st

def contact_section():
    st.markdown("""
    <style>
        .contact-header {
            font-size: 2.5rem;
            color: gold;
            text-align: center;
            margin: 3rem 0;
            text-transform: uppercase;
        }
        .contact-info {
            background: #1a1a1a;
            padding: 2rem;
            border-radius: 10px;
            border-left: 4px solid gold;
            margin-bottom: 2rem;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .info-title {
            color: gold;
            margin: 1rem 0;
            font-size: 1.1rem;
            padding: 0.8rem;
            border-radius: 8px;
            background: rgba(255, 215, 0, 0.1);
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .info-title:hover {
            background: rgba(255, 215, 0, 0.2) !important;
        }
        .info-title a {
            color: inherit;
            text-decoration: none;
        }
        .stTextInput>div>div>input, 
        .stTextArea>div>textarea {
            background-color: #1a1a1a !important;
            color: white !important;
            border: 1px solid #333 !important;
        }
        .stTextInput>label, 
        .stTextArea>label {
            color: #ddd !important;
        }
        .form-button {
            background: gold !important;
            color: #0f0f0f !important;
            padding: 12px 30px !important;
            border: none !important;
            border-radius: 5px !important;
            font-weight: bold !important;
            transition: all 0.3s ease !important;
        }
        .form-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(255, 215, 0, 0.3) !important;
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

    st.markdown('<div class="contact-header">Get in Touch</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="contact-info">
            <h4 class="info-title">
                <i class="fas fa-envelope"></i>
                <a href="mailto:mmadubugwukingsley@gmail.com">mmadubugwukingsley@gmail.com</a>
            </h4>
            
            <h4 class="info-title">
                <i class="fas fa-map-marker-alt"></i>
                14b Ibironke, Lagos
            </h4>
            
            <h4 class="info-title">
                <i class="fas fa-phone"></i>
                <a href="tel:+2349076055774">+234 907 605 5774</a>
            </h4>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name*")
            email = st.text_input("Email*")
            subject = st.text_input("Subject*")
            message = st.text_area("Message*", height=150)
            submitted = st.form_submit_button("SEND MESSAGE")
        
        if submitted:
            if name and email and subject and message:
                mailto_link = f"mailto:mmadubugwukingsley@gmail.com?subject={subject}&body=From: {name} <{email}>%0A%0A{message}"
                st.success("📬 Message sent successfully!")
                st.markdown(f"""
                    <div style="margin-top: 1rem;">
                        <a href="{mailto_link}" target="_blank" 
                           style="color: gold; text-decoration: none;">
                           <i class="fas fa-external-link-alt"></i> Open email client
                        </a>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ Please fill all required fields!")

contact_section()