# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pandas as pd
import imageio

solutions = pd.read_csv(r"https://raw.githubusercontent.com/finnrea78/equitable_AI/main/Data/solutions.csv")

solutions_list = solutions["Solution"]


overall = imageio.imread(r"figures/overall.png")
sexes = imageio.imread(r"figures/sexes.png")
ages = imageio.imread(r"figures/ages.png")
ethnicities = imageio.imread(r"figures/ethnicities.png")

def Group_1():
    st.markdown("# Task 2")
    st.sidebar.markdown("# Task 2")
    st.markdown("""Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.
Assume the model can be deployed as soon as the use-case is completed, and that the sooner the model is out, the sooner it can be used to help """)

    st.markdown("""##### Use-case #1

Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.

Assume the model can be deployed as soon as the use-case is completed.

The model will be used with other systems to make decisions, so it’s overall performance may not be significant.
    """)




    st.markdown("**Summary of model performance**")

    st.image(overall)
    st.image(sexes)
    st.image(ages)
    st.image(ethnicities)

    st.markdown("Next we will look at some possible solutions ")
    #st.dataframe(solutions)

    for i, soultion, in enumerate(solutions.iterrows()):
        st.markdown("#### "+solutions["Solution"][i])
        st.markdown(solutions["Explanation"][i])
        st.markdown("**Time Cost:** " + solutions["Time-Cost"][i])
        st.markdown("**Positive:** " + solutions["Positive effect"][i])
        st.markdown("**Negative:** "+solutions["Negative effect"][i])
        #st.markdown("**Use-Case for** **which this solution** **is particularly problematic:** " + solutions["Issues"][i])
        

    st.markdown("#### Please pick first solution")
    solution_picks_1 = st.multiselect(
        "which solution is best for the bias you saw",
        solutions_list
    )

    st.markdown("#### Please pick second solution")
    solution_picks_2 = st.multiselect(
        "which solution is second best for the bias you saw",
        solutions_list
    )

    form = st.form("selected")
    comment_1 = form.text_area("Reasons for first solution picked", key=1)
    comment_2 = form.text_area("Reasons for second solution picked", key=2)
    submit = form.form_submit_button("Submit")

    if submit:
        st.write("Saved!")

        dict_solutions = {
            "solution 1" : {"pick" : solution_picks_1, "comment": comment_1 },
            "solution 2" : {"pick" : solution_picks_2, "comment": comment_2 },
        }

        st.session_state["solutions"] = dict_solutions








def Group_2():
    st.markdown("# Task 2")
    st.sidebar.markdown("# Task 2")
    st.markdown("""Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.
Assume the model can be deployed as soon as the use-case is completed, and that the sooner the model is out, the sooner it can be used to help """)

    st.markdown("""##### Use-case #2

Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.

For this use-case, you will audit the dataset for possible bias, and finally, propose a solution to a predictive model that was built upon this dataset.

Assume the model can only be deployed in several months time after this use-case is completed, but that the sooner the model is out, the sooner it can be used to help. 
    """)





    st.markdown("**Summary of model performance**")

    st.image(overall)
    st.image(sexes)
    st.image(ages)
    st.image(ethnicities)

    st.markdown("Next we will look at some possible solutions ")
    #st.dataframe(solutions)

    for i, soultion, in enumerate(solutions.iterrows()):
        st.markdown("#### "+solutions["Solution"][i])
        st.markdown(solutions["Explanation"][i])
        st.markdown("**Time Cost:** " + solutions["Time-Cost"][i])
        st.markdown("**Positive:** " + solutions["Positive effect"][i])
        st.markdown("**Negative:** "+solutions["Negative effect"][i])
        #st.markdown("**Use-Case for** **which this solution** **is particularly problematic:** " + solutions["Issues"][i])
        

    st.markdown("#### Please pick first solution")
    solution_picks_1 = st.multiselect(
        "which solution is best for the bias you saw",
        solutions_list
    )

    st.markdown("#### Please pick second solution")
    solution_picks_2 = st.multiselect(
        "which solution is second best for the bias you saw",
        solutions_list
    )

    form = st.form("selected")
    comment_1 = form.text_area("Reasons for first solution picked", key=1)
    comment_2 = form.text_area("Reasons for second solution picked", key=2)
    submit = form.form_submit_button("Submit")

    if submit:
        st.write("Saved!")

        dict_solutions = {
            "solution 1" : {"pick" : solution_picks_1, "comment": comment_1 },
            "solution 2" : {"pick" : solution_picks_2, "comment": comment_2 },
        }

        st.session_state["solutions"] = dict_solutions

































def Group_3():
    st.markdown("# Task 2")
    st.sidebar.markdown("# Task 2")
    st.markdown("""Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.
Assume the model can be deployed as soon as the use-case is completed, and that the sooner the model is out, the sooner it can be used to help """)


    st.markdown("""##### Use-case #2

Your team was also presented with a predictive model built upon this dataset. The model is being used to predict patients at risk for catching Covid, undergoing hospitalization and dying.

Assume the model can only be deployed in just a couple of months time after this use-case is completed, and that the sooner the model is out, the sooner it can be used to help.

The model will NOT be used with other systems to make decisions, so it’s overall performance is significant.

    """)





    st.markdown("**Summary of model performance**")

    st.image(overall)
    st.image(sexes)
    st.image(ages)
    st.image(ethnicities)

    st.markdown("Next we will look at some possible solutions ")
    #st.dataframe(solutions)

    for i, soultion, in enumerate(solutions.iterrows()):
        st.markdown("#### "+solutions["Solution"][i])
        st.markdown(solutions["Explanation"][i])
        st.markdown("**Time Cost:** " + solutions["Time-Cost"][i])
        st.markdown("**Positive:** " + solutions["Positive effect"][i])
        st.markdown("**Negative:** "+solutions["Negative effect"][i])
        #st.markdown("**Use-Case for** **which this solution** **is particularly problematic:** " + solutions["Issues"][i])
        

    st.markdown("#### Please pick first solution")
    solution_picks_1 = st.multiselect(
        "which solution is best for the bias you saw",
        solutions_list
    )

    st.markdown("#### Please pick second solution")
    solution_picks_2 = st.multiselect(
        "which solution is second best for the bias you saw",
        solutions_list
    )

    form = st.form("selected")
    comment_1 = form.text_area("Reasons for first solution picked", key=1)
    comment_2 = form.text_area("Reasons for second solution picked", key=2)
    submit = form.form_submit_button("Submit")

    if submit:
        st.write("Saved!")

        dict_solutions = {
            "solution 1" : {"pick" : solution_picks_1, "comment": comment_1 },
            "solution 2" : {"pick" : solution_picks_2, "comment": comment_2 },
        }

        st.session_state["solutions"] = dict_solutions







page_names_to_funcs = {
    "Group 1": Group_1,
    "Group 2": Group_2,
    "Group 3": Group_3
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()