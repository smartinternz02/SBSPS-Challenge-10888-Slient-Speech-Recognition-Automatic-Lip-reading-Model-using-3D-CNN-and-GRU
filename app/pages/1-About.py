import streamlit as st
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
#st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/Screenshot_2023-08-30_at_11.47.40_PM.png')
st.header('Description', divider='blue')

st.write("Lip reading, the ability to understand spoken language by observing lip movements, is an essential skill for individuals with hearing impairments and in scenarios where audio information is compromised. Automatic lip reading systems, powered by deep learning techniques, have shown promising results in converting lip movements into text. This project proposes an advanced lip reading model that combines 3D Convolutional Neural Networks (CNNs) and Gated Recurrent Units (GRUs) to improve the accuracy and robustness of lip reading.The project's approach involves leveraging the spatio-temporal characteristics of lip motion using 3D CNNs. This allows the model to analyze sequential frames of lip movements and capture both spatial and temporal features simultaneously. The GRU component is employed to learn long-term dependencies and capture temporal dynamics in the lip movement sequences.")



