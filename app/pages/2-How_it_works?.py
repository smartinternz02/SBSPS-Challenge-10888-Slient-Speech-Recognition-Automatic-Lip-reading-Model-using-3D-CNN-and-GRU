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
    
st.header('How it works?', divider='blue')

points = [
    "The LipNet architecture operates through a meticulously designed sequence of operations.",
    "It begins with a series of three stages, each involving spatiotemporal convolutions, channel-wise dropout, and spatial max-pooling.",
    "This initial stage extracts crucial information from the input, encapsulating essential features.",
    "The architecture introduces two Bidirectional Gated Recurrent Units (Bi-GRUs), a pivotal element in the process.",
    "These Bi-GRUs facilitate the effective aggregation of outputs from the earlier spatiotemporal convolutions.",
    "Following this, each time-step undergoes a linear transformation.",
    "Subsequently, a softmax operation covers a vocabulary expanded to encompass the CTC blank symbol.",
    "The architecture's learning process is driven by the application of the Connectionist Temporal Classification (CTC) loss.",
    "Throughout the architecture, the Rectified Linear Unit (ReLU) serves as the activation function in all layers.",
    "This consistent choice of activation function contributes to the model's efficiency and performance.",
    "The orchestrated sequence of operations culminates in the LipNet architecture's proficiency in lip reading tasks."
]

for point in points:
    st.write(f"- {point}")

st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/image (1).jpg')

