# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd
import imageio

solutions = pd.read_csv(r"https://raw.githubusercontent.com/finnrea78/equitable_AI/main/Data/solutions.csv")

solutions_list = solutions["Solution"]


overall = imageio.imread(r"figures\overall.PNG")
sexes = imageio.imread(r"figures\sexes.PNG")
ages = imageio.imread(r"figures\ages.PNG")
ethnicities = imageio.imread(r"figures\ethnicities.PNG")

def Task_2():
    st.markdown("# Task 2")
    st.sidebar.markdown("# Task 2")
    st.markdown("""Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.
Assume the model can be deployed as soon as the use-case is completed, and that the sooner the model is out, the sooner it can be used to help """)

    st.markdown("**Summary of model performance**")

    st.image(overall)
    st.image(sexes)
    st.image(ages)
    st.image(ethnicities)

    st.markdown("next we will look at some possible solutions ")
    #st.dataframe(solutions)

    for i, soultion, in enumerate(solutions.iterrows()):
        st.markdown("#### "+solutions["Solution"][i])
        st.markdown(solutions["Explanation"][i])
        st.markdown("**Time Cost:** " + solutions["Time-Cost"][i])
        st.markdown("**Positive:** " + solutions["Positive effect"][i])
        st.markdown("**Negative:** "+solutions["Negative effect"][i])
        #st.markdown("**Use-Case for** **which this solution** **is particularly problematic:** " + solutions["Issues"][i])
        

    st.markdown("#### please pick first possible solutions")
    solution_picks_1 = st.multiselect(
        "which solution is best for the bias you saw",
        solutions_list
    )

    st.markdown("#### please pick first possible solutions")
    solution_picks_2 = st.multiselect(
        "which solution is second best for the bias you saw",
        solutions_list
    )

    form = st.form("selected")
    form.write("why first pick")
    comment_1 = form.text_area("reason", key=1)
    form.write("why second pick")
    comment_2 = form.text_area("reason", key=2)
    submit = form.form_submit_button("Submit")

    if submit:
        st.write("Saved!")

        dict_solutions = {
            "solution 1" : {"pick" : solution_picks_1, "comment": comment_1 },
            "solution 2" : {"pick" : solution_picks_2, "comment": comment_2 },
        }

        st.session_state["solutions"] = dict_solutions

page_names_to_funcs = {
    "Task 2": Task_2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()