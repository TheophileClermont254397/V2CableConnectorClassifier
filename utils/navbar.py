import streamlit as st

def render_navbar(active="home"):
    home_style = "background-color: #2563eb; color: #ffffff;" if active == "home" else ""
    classifier_style = "background-color: #2563eb; color: #ffffff;" if active == "classifier" else ""

    st.markdown(f"""
        <style>
            header[data-testid="stHeader"] {{
                display: none !important;
            }}

            .block-container {{
                padding-top: 70px !important;
            }}

            .custom-navbar {{
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                width: 100%;
                z-index: 999999;
                background-color: #1e3a5f;
                padding: 10px 20px;
                display: flex;
                flex-direction: row;
                gap: 10px;
                border-bottom: 2px solid #2563eb;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            }}

            .custom-navbar a {{
                color: #ffffff;
                text-decoration: none;
                font-size: 15px;
                font-weight: 600;
                padding: 8px 16px;
                border-radius: 8px;
                transition: background 0.2s ease;
            }}

            .custom-navbar a:hover {{
                background-color: #2563eb;
            }}

            @media (max-width: 600px) {{
                .custom-navbar {{
                    padding: 8px 12px;
                    gap: 8px;
                }}
                .custom-navbar a {{
                    font-size: 13px;
                    padding: 6px 12px;
                }}
            }}
        </style>

        <div class="custom-navbar">
            <a href="/" target="_self" style="{home_style}">📖 How to Use</a>
            <a href="/classifier" target="_self" style="{classifier_style}">🔌 Classifier</a>
        </div>
    """, unsafe_allow_html=True)
