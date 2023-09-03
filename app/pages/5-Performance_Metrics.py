import streamlit as st
st.set_page_config(layout="wide")
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
st.header('Performance Metrics', divider='blue')

col1, col2, col3 = st.columns(3)
col1.metric("Outperforms human by", "4.1x")
col2.metric("Word Error Rate", "4.8%")
col3.metric("Sentence accuracy", "95.2%")

col1, col2, col3 = st.columns(3)
col1.metric("Training Videos", "450")
col2.metric("Unseen CER", "6.4%")
col3.metric("Vocabulary tokens", "41")

col1, col2, col3 = st.columns(3)
col1.metric("Trainable parameters", "8471924")
col2.metric("STCNN Layers", "x3")
col3.metric("Bi-GRU", "x2")

st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/ezgif.com-video-to-gif.gif',use_column_width="always")