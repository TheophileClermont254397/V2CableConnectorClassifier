import streamlit as st

st.set_page_config(
    page_title="Cable Connector Classifier",
    page_icon="🔌",
    layout="wide"
)

# Force light theme via CSS
st.markdown("""
    <style>
        /* Force light background */
        .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
        
        .block-container {
            background-color: #ffffff !important;
        }
        
        /* Force dark text globally */
        .stMarkdown, .stMarkdown p, .stMarkdown h1, .stMarkdown h2, 
        .stMarkdown h3, .stMarkdown h4, .stMarkdown li, .stText,
        label, span, div {
            color: #000000 !important;
        }
        
        /* Sidebar light */
        [data-testid="stSidebar"] {
            background-color: #f0f2f6 !important;
        }
    </style>
""", unsafe_allow_html=True)

home_page = st.Page("pages/home.py", title="How to Use", icon="📖")
classifier_page = st.Page("pages/classifier.py", title="Classifier", icon="🔌")

pg = st.navigation(
    [home_page, classifier_page],
    position="hidden"
)
pg.run()
