import streamlit as st
import pandas as pd

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

st.header('Neural Architecture', divider='blue')

st.image('/Users/chaitanyatandon/Desktop/LIPBUDDIES/image.jpg')


data = {
    "Layer (type)": ["conv3d_3 (Conv3D)", "activation_3 (Activation)", "max_pooling3d_3 (MaxPooling3D)",
                     "conv3d_4 (Conv3D)", "activation_4 (Activation)", "max_pooling3d_4 (MaxPooling3D)",
                     "conv3d_5 (Conv3D)", "activation_5 (Activation)", "max_pooling3d_5 (MaxPooling3D)",
                     "time_distributed_1 (TimeDistributed)", "bidirectional_2 (Bidirectional)",
                     "dropout_2 (Dropout)", "bidirectional_3 (Bidirectional)", "dropout_3 (Dropout)",
                     "dense (Dense)"],
    "Output Shape": ["(None, 75, 46, 140, 128)", "(None, 75, 46, 140, 128)", "(None, 75, 23, 70, 128)",
                     "(None, 75, 23, 70, 256)", "(None, 75, 23, 70, 256)", "(None, 75, 11, 35, 256)",
                     "(None, 75, 11, 35, 75)", "(None, 75, 11, 35, 75)", "(None, 75, 5, 17, 75)",
                     "(None, 75, 6375)", "(None, 75, 256)", "(None, 75, 256)", "(None, 75, 256)",
                     "(None, 75, 256)", "(None, 75, 41)"],
    "Param #": ["3584", "0", "0", "884992", "0", "0", "518475", "0", "0", "0", "6660096", "0", "394240",
                "0", "10537"]
}

df = pd.DataFrame(data)

st.table(df)

total_params = "8471924"
trainable_params = "8471924"
non_trainable_params = "0"

st.header("Model Parameters",divider='blue')
st.write("Total params:", total_params, "(", f"{int(total_params) / (1024 * 1024):.2f}", "MB)")
st.write("Trainable params:", trainable_params, "(", f"{int(trainable_params) / (1024 * 1024):.2f}", "MB)")
st.write("Non-trainable params:", non_trainable_params, "(", f"{int(non_trainable_params) / (1024 * 1024):.2f}", "Byte)")


