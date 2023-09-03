import streamlit as st

st.header('Deployment made easy with IBM Cloud',divider="blue")
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
st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/hero_animation.gif')
#st.video('/Users/chaitanyatandon/Desktop/LIPBUDDIES/hero_animation.mp4')

st.write('IBM Watson Machine Learning is a full-service IBM Cloud offering that makes it easy for developers and data scientists to work together to integrate predictive capabilities with their applications. The Watson Machine Learning service is a set of REST APIs that you can call from any programming language to develop applications that make smarter decisions, solve tough problems, and improve user outcomes.')

st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/Screenshot 2023-09-03 at 11.04.04 PM.png',use_column_width="always")
st.info('Using the IBM Watson Machine Learning API client')

