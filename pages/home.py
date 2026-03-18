import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from utils.navbar import render_navbar
render_navbar(active="home")

st.title("📖 Welcome to Cable Connector Classifier")
st.write("This app helps you identify cable connectors using AI.")

if st.button("🔌 Go to Classifier"):
    st.switch_page("pages/classifier.py")

st.divider()

st.subheader("🚀 How to Use the App")

with stylable_container(
    key="step1",
    css_styles="""
        {
            background-color: #f0f4ff;
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #2563eb;
            margin-bottom: 10px;
        }
    """
):
    st.markdown("### Step 1: Choose Input Method")
    st.write("Go to the **Classifier** page. Choose between:")
    st.write("- 📁 **Upload from gallery** — select an existing image from your device")
    st.write("- 📸 **Take a photo** — use your camera to capture the connector")

with stylable_container(
    key="step2",
    css_styles="""
        {
            background-color: #f5f0ff;
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #7c3aed;
            margin-bottom: 10px;
        }
    """
):
    st.markdown("### Step 2: Crop (Optional)")
    st.write("- ✂️ Enable the **Crop image** checkbox to focus on the connector")
    st.write("- Drag the crop box around the connector for better accuracy")

with stylable_container(
    key="step3",
    css_styles="""
        {
            background-color: #f0fdf4;
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #16a34a;
            margin-bottom: 10px;
        }
    """
):
    st.markdown("### Step 3: Predict")
    st.write("- Click the **Predict** button to classify the connector")
    st.write("- The app will show the predicted class and confidence score")

with stylable_container(
    key="step4",
    css_styles="""
        {
            background-color: #fff7ed;
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #ea580c;
            margin-bottom: 10px;
        }
    """
):
    st.markdown("### Step 4: Read the Results")
    st.write("- 📖 **Description** — learn what the connector is")
    st.write("- 🛠️ **How to Use** — instructions for using it")
    st.write("- 🔗 **Compatible With** — see which connectors it pairs with")

st.divider()

st.subheader("🔌 Supported Connectors")

col1, col2, col3 = st.columns(3)

with col1:
    with stylable_container(
        key="hdmi_card",
        css_styles="""
            {
                background-color: #f0f4ff;
                border-radius: 10px;
                padding: 15px;
                text-align: center;
            }
        """
    ):
        st.markdown("### 🖥️ HDMI")
        st.write("Male & Female")

with col2:
    with stylable_container(
        key="usba_card",
        css_styles="""
            {
                background-color: #f0f4ff;
                border-radius: 10px;
                padding: 15px;
                text-align: center;
            }
        """
    ):
        st.markdown("### 💾 USB-A")
        st.write("Male & Female")

with col3:
    with stylable_container(
        key="usbc_card",
        css_styles="""
            {
                background-color: #f0f4ff;
                border-radius: 10px;
                padding: 15px;
                text-align: center;
            }
        """
    ):
        st.markdown("### ⚡ USB-C")
        st.write("Male & Female")

st.divider()

with stylable_container(
    key="go_button",
    css_styles="""
        button {
            display: block;
            margin: 0 auto;
            width: 150%;
            font-size: 18px;
            font-weight: bold;
            height: 55px;
            border-radius: 10px;
            background-color: #2563eb;
            color: white;
        }
    """
):
    if st.button("🔌 Go to Classifier "):
        st.switch_page("pages/classifier.py")
