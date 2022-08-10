import streamlit as st 
import pandas as pd
import imageio


bias_data = st.session_state["task1_results"]
# pd.read_csv(r"C:\Users\reaf\EQ_AI\Data\bias.csv")


st.markdown("# Results")

st.markdown("#### bias selections: ")

st.markdown("##### visual 1")

image = imageio.imread('figures/figure.jpg')

st.image(image)


st.write("bias")

for bias in bias_data["bias_1"].dropna():
    st.text(bias)

st.write("reasons")


for comment in bias_data["Comment_1"].dropna():
    st.markdown(comment)

st.markdown("##### visual 2")

image = imageio.imread('figures/figure.jpg')

st.image(image)

st.write("bias")
for bias in bias_data["bias_2"].dropna():
    st.text(bias)
st.write("reasons")

for comment in bias_data["Comment_2"].dropna():
    st.markdown(comment)



st.markdown("##### visual 3")

image = imageio.imread('figures/figure.jpg')

st.image(image)

st.write("bias")
for bias in bias_data["bias_3"].dropna():
    st.text(bias)

st.write("reasons")

for comment in bias_data["Comment_3"].dropna():
    st.markdown(comment)
