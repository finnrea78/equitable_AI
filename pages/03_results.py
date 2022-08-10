import streamlit as st 
import pandas as pd
import imageio


bias_data = st.session_state["task1_results"]
# pd.read_csv(r"C:\Users\reaf\EQ_AI\Data\bias.csv")

solutions = st.session_state["solutions"]


st.markdown("# Results")


st.markdown("## Task 1 results")

for i in range(1, 18):


    if bias_data["visual_" + str(i)] == True:

        st.markdown("### Visual " + str(i))
        fig = "fig_"+str(i)
        image = imageio.imread("figures/"+fig+".PNG")
        st.image(image)

        st.markdown("**Bias seen:**")



        if bias_data["bias_" + str(i)] == None:
            st.markdown("none")
        else:
            for bias in bias_data["bias_" + str(i)]:
                st.markdown(bias)
            st.markdown("**Comment:**")
            st.markdown(bias_data["comment_" + str(i)])


        
st.markdown("## Task 2 results")


st.markdown("### solution 1")

st.markdown("###### " + solutions["solution 1"]["pick"][0] + " : " )
st.markdown(solutions["solution 1"]["comment"])

st.markdown("### solution 2")
st.markdown("###### " + solutions["solution 2"]["pick"][0] + " : " )
st.markdown(solutions["solution 2"]["comment"])




