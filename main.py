# This is a sample Python script.

import streamlit as st
import numpy as np
import pandas as pd
import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with st.sidebar:
        st.write("SET YOUR VARIABLES HERE")
    st.write("WELCOME")
    import pandas as pd

    st.write("Here's our first attempt at using data to create a table:")
    df = pd.DataFrame({
        'first column': [1, 2, 13, 4],
        'second column': [30, 20, 30, 40]
    })

    st.write(df)
    st.dataframe(df.style.highlight_max(axis=0))
    st.line_chart(df)
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)

    x = st.slider('x')  # 👈 this is a widget
    st.write(x, 'squared is', x * x)

    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
    list=["Email", "Home phones", "Mobile phone"]
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        list)
    if add_selectbox=="Email":
        st.write("We will send you email shortly")

    with st.sidebar:

        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")