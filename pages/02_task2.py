# Contents of ~/my_app/streamlit_app.py
from tkinter import N
import streamlit as st
import pandas as pd

solutions = pd.read_csv(r"C:\Users\reaf\EQ_AI\Data\solutions.csv", index_col="Solution")

def Task_2():
    st.markdown("# Task 2")
    st.sidebar.markdown("# Task 2")
    st.markdown("next we will look at some possible solutions ")
    st.dataframe(solutions, width = 1000)

page_names_to_funcs = {
    "Task 2": Task_2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()