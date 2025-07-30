import streamlit as st
import numpy as np
import requests

# Replace 'service1' with the name defined in render.yaml
MATLAB_SERVICE_URL = "https://matlab-uxuj.onrender.com"

st.title("Magic Square Generator")
size = st.slider("Select size of magic square:", 1, 10, 3)
debug = st.checkbox("Debug")
if st.button("Generate Magic Square"):
    try:
        response = requests.post(f"{MATLAB_SERVICE_URL}/mymagic/mymagic", json={"rhs":size, "nargout":1})
        j = response.json()
        lhs = j['lhs'][0]
        # grab the data and size
        flat = lhs['mwdata']       # [8, 3, 4, 1, 5, 9, 6, 7, 2]
        rows, cols = lhs['mwsize'] # [3, 3]
        # make a NumPy array and reshape
        magic_square = np.array(flat).reshape(rows, cols)
        st.write("Magic Square of size", size)
        st.write(np.array(magic_square))
        if debug:
            st.sidebar.write("Response from MATLAB Service:", response.json())
    except Exception as e:
        st.error(f"Error connecting to MATLAB Service: {e}")