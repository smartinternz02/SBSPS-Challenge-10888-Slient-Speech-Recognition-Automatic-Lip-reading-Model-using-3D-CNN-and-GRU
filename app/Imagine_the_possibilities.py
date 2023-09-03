import streamlit as st
from PIL import Image



phrases = [
    "Redefined privacy",
    "Enhanced Accessibility",
    "Shaping the future of Human Computer Interaction",
    "Pioneering the Future of Lipreading Technology",
    "Unleashing the Potential of Visual Communication",
    "Elevating Lipreading to Extraordinary Heights"
    
]

background_colors = ['#262730', 'white']

text_colors = ['#ffffff', '#000000']

st.set_page_config(
    page_title="LipSense",
    layout="wide"
)

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("https://www.dropbox.com/scl/fi/1diny80z7lfy9xnif7wa7/Screenshot_2023-08-30_at_11.47.40_PM.png?rlkey=30biilu3jrlpdjlird0itaco9&dl=0&raw=1");
                background-repeat: no-repeat;
                padding-top: 20px;
                background-size: 290px 80px;
                background-position: 20px 20px;
            }
            
        </style>
        """,
        unsafe_allow_html=True,
    )
st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/Screenshot 2023-08-31 at 2.22.51 AM.png')

for i, phrase in enumerate(phrases):
    st.markdown(
        f'<div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 300px; background-color: {background_colors[i%2]}"><h2 style="color: {text_colors[i%2]}; text-align: center;">{phrase}</h2></div>',
        unsafe_allow_html=True
    )




