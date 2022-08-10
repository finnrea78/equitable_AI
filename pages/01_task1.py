import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
import json

import imageio
import matplotlib.pyplot as plt

data_bias_desc = ["This caused by poor sampling and real randomization is not achieved. A small sample of similar cases are selected excluding a large part of the population. This often leads to one part of the population being undersampled where we cannot make reliable predictions. Some examples of this are when one class size is too large to give reasonable comparison to other classes. Or when one is so small it cannot be used to make reliable predictions.",
"where coincidental correlations between features are found and labeled as significant. This can cause real correlations and relations to be missed. Correlation does not equal causation. ", 
"Relevant data is missing from the dataset. This could be because this information was never collected, or because it has since been discounted as irrelevant. This could cause important correlations to be missed in the data. ",
"occurs when distinct populations are inappropriately combined. An AI model is unlikely to fit all groups and populations. E.g. Hispanics have higher rates of diabetes and diabetes-related complications than non-Hispanic whites. If building AI to diagnose or monitor diabetes, it is important to make the system sensitive to these ethnic differences, by either including ethnicity as a feature in the data, or building separate models for different ethnic groups.",
"This is bias that occurs from initial measurements and instruments for gathering data. This is unreliable data. Another type of measurement bias is the problem of inconsistent data labeling by humans, which can be called recall bias."]

dict_data = {
        "Description" : data_bias_desc
    }


human_bias_desc = ["Where observers see what they want to see in the dataset. Researchers may deliberately or subconsciously let their subjective thoughts and prior knowledge influence their generation of hypotheses and data analysis and consequently, influence their research findings.",
"already existing bias and socio-technical issues in the world. An example of this type of bias can be found in a 2018 image search result where searching for women CEOs ultimately resulted in fewer female CEO images due to the fact that only 5\% of Fortune 500 CEOs were woman—which would cause the search results to be biased towards male CEOs. These search results were of course reflecting the reality, but whether or not the search algorithms should reflect this reality is an issue worth considering.",
"Another related common problem with human bias occurs in the context of supervised machine learning, where humans oftentimes label the data that is used to train a model. Even if they are well-intentioned and do not mean any harm, their unconscious biases could sneak into the training sample. ",
"This is bias that occurs from initial measurements and instruments for gathering data. This is unreliable data. Another type of measurement bias is the problem of inconsistent data labeling by humans, which can be called recall bias."]

dict_human = { 
    "Description" : human_bias_desc
}

algo_bias_desc = ["models are trained on data, then evaluated against certain benchmarks. Bias occurs when these benchmarks don't represent the whole population or appropriate way for the model to be used. By only measuring a model against an unrepresentative class it can cause the AI model to neglect other classes. ",
"not present in the input data and is added purely by the algorithm. The algorithmic design choices, such as use of certain optimization functions, regularizations, choices in applying regression models on the data as a whole or considering subgroups, and the general use of statistically biased estimators in"]

dict_algo = {
    "description" : algo_bias_desc
}


df_human = pd.DataFrame(data = dict_human,
index=["Confirmation bias", "Historical bias", "Mislabelling bias", "Measurement bias"])

df_data = pd.DataFrame(data=dict_data, 
index = ["Selection bias", "Association bias", "Exclusion bias/ missing data", "Aggregation bias", "Measurement bias"])

df_algo = pd.DataFrame(data=dict_algo,
index = ["Evaluation bias", "Algorithmic bias"])

#df_data = pd.DataFrame.from_dict(dict_data, index=["Selection bias", "Association bias", "Exclusion bias/ missing data", "Aggregation bias", "Measurement bias"])





def Group_1():

    options_1, options_2, options_3, options_4, options_5, options_6 = None, None, None, None, None, None, 
    options_7, options_8, options_9, options_10, options_11, options_12 = None, None, None, None, None, None,
    options_13, options_14, options_15, options_16, options_17 = None, None, None, None, None

    comment_1, comment_2, comment_3, comment_4, comment_5 = None, None, None, None, None
    comment_6, comment_7, comment_8, comment_9, comment_10 = None, None, None, None, None,
    comment_11, comment_12, comment_13, comment_14, comment_15 = None, None, None, None, None,
    comment_16, comment_17 = None, None


    st.markdown("# Task 1")
    st.markdown("Map biases (from a list of biases provided, with explanations, and the host there to elaborate or give example) to the use-case and then use a visualization (from Streamlit, a set of premade graphs or presets), giving justification for all this in Streamlit/a slide-deck")
    st.sidebar.markdown("# Task 1")



    st.markdown("""###### Your team has been presented with a Covid-19 Case Surveillance dataset. Each row in the dataset contains information about a de-identified patient. There are 19* columns in this dataset, 
There are (need to check after cleaning, dropping NANs) 20 million patients in this dataset. For the purpose of this task, this is considered a reasonable volume of data

For this use-case, you will audit the dataset for possible bias, and finally, propose a solution to a predictive model that was built upon this dataset.
Assume the model can only be deployed in a couple of months time after this use-case is completed

Your team has three tasks to complete, which involve auditing the dataset and model for bias, and finally, presenting a solution to reduce bias in the model’s predictions


**If your team see bias in a visualisation click the checkbox and please give a description of the bias seen**
 """)




    st.markdown("## visual 1")

    image = imageio.imread('figures/fig_1.png')
    st.image(image)

    bias_1 = st.checkbox("Bias?", key=1)

    if bias_1:
        st.markdown("Which possible bias did you see.")

        options_1 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "1")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_1 = st.text_area("reasons", height = 100, key="1")



    st.markdown("## visual 2")

    image = imageio.imread('figures/fig_2.png')

    st.image(image)

    bias_2 = st.checkbox("Bias?", key=2)

    if bias_2:
        st.markdown("Which possible bias did you see.")

        options_2 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "2")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_2 = st.text_area("reasons", height = 100, key="2")

    



    st.markdown("## visual 3")

    image = imageio.imread('figures/fig_3.png')

    st.image(image)

    bias_3 = st.checkbox("Bias?", key=3)

    if bias_3:
        st.markdown("Which possible bias did you see.")

        options_3 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "3")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_3 = st.text_area("reasons", height = 100, key="3")



    st.markdown("## visual 4")

    image = imageio.imread('figures/fig_4.png')

    st.image(image)

    bias_4 = st.checkbox("Bias?", key=4)

    if bias_4:
        st.markdown("Which possible bias did you see.")

        options_4 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "4")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_4 = st.text_area("reasons", height = 100, key="4")


    st.markdown("## visual 5")

    image = imageio.imread('figures/fig_5.png')

    st.image(image)

    bias_5 = st.checkbox("Bias?", key=5)

    if bias_5:
        st.markdown("Which possible bias did you see.")

        options_5 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "5")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_5 = st.text_area("reasons", height = 100, key="5")




    
    st.markdown("## visual 6")

    image = imageio.imread('figures/fig_6.png')

    st.image(image)

    bias_6 = st.checkbox("Bias?", key=6)

    if bias_6:
        st.markdown("Which possible bias did you see.")

        options_6 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "6")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_6 = st.text_area("reasons", height = 100, key="6")

    


    st.markdown("## visual 7")

    image = imageio.imread('figures/fig_7.png')

    st.image(image)

    bias_7 = st.checkbox("Bias?", key=7)

    if bias_7:
        st.markdown("Which possible bias did you see.")

        options_7 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "7")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_7 = st.text_area("reasons", height = 100, key="7")


    
    st.markdown("## visual 8")

    image = imageio.imread('figures/fig_8.png')

    st.image(image)

    bias_8 = st.checkbox("Bias?", key=8)

    if bias_8:
        st.markdown("Which possible bias did you see.")

        options_8 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "8")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_8 = st.text_area("reasons", height = 100, key="8")





    st.markdown("## visual 9")

    image = imageio.imread('figures/fig_9.png')

    st.image(image)

    bias_9 = st.checkbox("Bias?", key=9)

    if bias_9:
        st.markdown("Which possible bias did you see.")

        options_9 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "9")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_9 = st.text_area("reasons", height = 100, key="9")


    st.markdown("## visual 10")

    image = imageio.imread('figures/fig_10.png')

    st.image(image)

    bias_10 = st.checkbox("Bias?", key=10)

    if bias_10:
        st.markdown("Which possible bias did you see.")

        options_10 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "10")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_10 = st.text_area("reasons", height = 100, key="10")



    st.markdown("## visual 11")

    image = imageio.imread('figures/fig_11.png')

    st.image(image)

    bias_11 = st.checkbox("Bias?", key=11)

    if bias_11:
        st.markdown("Which possible bias did you see.")

        options_11 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "11")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_11 = st.text_area("reasons", height = 100, key="11")



    st.markdown("## visual 12")

    image = imageio.imread('figures/fig_12.png')

    st.image(image)

    bias_12 = st.checkbox("Bias?", key=12)

    if bias_12:
        st.markdown("Which possible bias did you see.")

        options_12 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "12")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_12 = st.text_area("reasons", height = 100, key="12")


    st.markdown("## visual 13")

    image = imageio.imread('figures/fig_13.png')

    st.image(image)

    bias_13 = st.checkbox("Bias?", key=13)

    if bias_13:
        st.markdown("Which possible bias did you see.")

        options_13 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "13")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_13 = st.text_area("reasons", height = 100, key="13")



    st.markdown("## visual 14")

    image = imageio.imread('figures/fig_14.png')

    st.image(image)

    bias_14 = st.checkbox("Bias?", key=14)

    if bias_14:
        st.markdown("Which possible bias did you see.")

        options_14 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "14")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_14 = st.text_area("reasons", height = 100, key="14")



    st.markdown("## visual 15")

    image = imageio.imread('figures/fig_15.png')

    st.image(image)

    bias_15 = st.checkbox("Bias?", key=15)

    if bias_15:
        st.markdown("Which possible bias did you see.")

        options_15 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "15")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_15 = st.text_area("reasons", height = 100, key="15")



    
    st.markdown("## visual 16")

    image = imageio.imread('figures/fig_16.png')

    st.image(image)

    bias_16 = st.checkbox("Bias?", key=16)

    if bias_16:
        st.markdown("Which possible bias did you see.")

        options_16 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "16")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_16 = st.text_area("reasons", height = 100, key="16")

    
    st.markdown("## visual 17")

    image = imageio.imread('figures/fig_17.png')

    st.image(image)

    bias_17 = st.checkbox("Bias?", key=17)

    if bias_17:
        st.markdown("Which possible bias did you see.")

        options_17 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "17")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_17 = st.text_area("reasons", height = 100, key="17")

    
    if st.button("save"):
        dict_items = {"bias_1" : options_1, "bias_2": options_2, "bias_3" : options_3, 
        "bias_4" : options_4, "bias_5": options_5, "bias_6" : options_6, "bias_7": options_7, 
        "bias_8" : options_8, "bias_9" : options_9, "bias_10": options_10, "bias_11" : options_11,
        "bias_12": options_12, "bias_13" : options_13, "bias_14" : options_14, "bias_15": options_15,
        "bias_16" : options_16, "bias_17": options_17,
        "comment_1" : comment_1, "comment_2" : comment_2, "comment_3" : comment_3,
        "comment_4" : comment_4 , "comment_5" : comment_5, "comment_6" : comment_6, "comment_7" : comment_7, "comment_8" : comment_8,
        "comment_9" : comment_9 , "comment_9" : comment_9, "comment_10" : comment_10, "comment_11" : comment_11, "comment_12" : comment_12,
        "comment_13" : comment_13 , "comment_14" : comment_14, "comment_15" : comment_15, "comment_16" : comment_16, "comment_17" : comment_17,
        "visual_1": bias_1, "visual_2": bias_2, "visual_3": bias_3, 
        "visual_4": bias_4, "visual_5": bias_5, "visual_6": bias_6, "visual_7": bias_7, "visual_8": bias_8, 
        "visual_9": bias_9, "visual_10": bias_10,"visual_11": bias_11, "visual_12": bias_12, "visual_13": bias_13, 
        "visual_14": bias_14, "visual_15": bias_15,"visual_16": bias_16, "visual_17": bias_17
        }
        #data = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_items.items() ]))
        
        st.session_state["task1_results"] = dict_items
        
        #data.to_csv(r'C:\Users\reaf\EQ_AI\Data\bias.csv') 
        st.markdown("SAVED!")











def Group_2():

    options_1, options_2, options_3, options_4, options_5, options_6 = None, None, None, None, None, None, 
    options_7, options_8, options_9, options_10, options_11, options_12 = None, None, None, None, None, None,
    options_13, options_14, options_15, options_16, options_17 = None, None, None, None, None

    comment_1, comment_2, comment_3, comment_4, comment_5 = None, None, None, None, None
    comment_6, comment_7, comment_8, comment_9, comment_10 = None, None, None, None, None,
    comment_11, comment_12, comment_13, comment_14, comment_15 = None, None, None, None, None,
    comment_16, comment_17 = None, None


    st.markdown("# Task 1")
    st.markdown("Map biases (from a list of biases provided, with explanations, and the host there to elaborate or give example) to the use-case and then use a visualization (from Streamlit, a set of premade graphs or presets), giving justification for all this in Streamlit/a slide-deck")
    st.sidebar.markdown("# Task 1")



    st.markdown("""###### Your team has been presented with a Covid-19 Case Surveillance dataset. Each row in the dataset contains information about a de-identified patient. There are 19* columns in this dataset, 
There are (need to check after cleaning, dropping NANs) 20 million patients in this dataset. For the purpose of this task, this is considered a reasonable volume of data

For this use-case, you will audit the dataset for possible bias, and finally, propose a solution to a predictive model that was built upon this dataset.
Assume the model can only be deployed in a couple of months time after this use-case is completed

Your team has three tasks to complete, which involve auditing the dataset and model for bias, and finally, presenting a solution to reduce bias in the model’s predictions


**If your team see bias in a visualisation click the checkbox and please give a description of the bias seen**
 """)




    st.markdown("## visual 1")

    image = imageio.imread('figures/fig_1.png')
    st.image(image)

    bias_1 = st.checkbox("Bias?", key=1)

    if bias_1:
        st.markdown("Which possible bias did you see.")

        options_1 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "1")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_1 = st.text_area("reasons", height = 100, key="1")



    st.markdown("## visual 2")

    image = imageio.imread('figures/fig_2.png')

    st.image(image)

    bias_2 = st.checkbox("Bias?", key=2)

    if bias_2:
        st.markdown("Which possible bias did you see.")

        options_2 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "2")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_2 = st.text_area("reasons", height = 100, key="2")

    



    st.markdown("## visual 3")

    image = imageio.imread('figures/fig_3.png')

    st.image(image)

    bias_3 = st.checkbox("Bias?", key=3)

    if bias_3:
        st.markdown("Which possible bias did you see.")

        options_3 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "3")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_3 = st.text_area("reasons", height = 100, key="3")



    st.markdown("## visual 4")

    image = imageio.imread('figures/fig_4.png')

    st.image(image)

    bias_4 = st.checkbox("Bias?", key=4)

    if bias_4:
        st.markdown("Which possible bias did you see.")

        options_4 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "4")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_4 = st.text_area("reasons", height = 100, key="4")


    st.markdown("## visual 5")

    image = imageio.imread('figures/fig_5.png')

    st.image(image)

    bias_5 = st.checkbox("Bias?", key=5)

    if bias_5:
        st.markdown("Which possible bias did you see.")

        options_5 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "5")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_5 = st.text_area("reasons", height = 100, key="5")




    
    st.markdown("## visual 6")

    image = imageio.imread('figures/fig_6.png')

    st.image(image)

    bias_6 = st.checkbox("Bias?", key=6)

    if bias_6:
        st.markdown("Which possible bias did you see.")

        options_6 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "6")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_6 = st.text_area("reasons", height = 100, key="6")

    


    st.markdown("## visual 7")

    image = imageio.imread('figures/fig_7.png')

    st.image(image)

    bias_7 = st.checkbox("Bias?", key=7)

    if bias_7:
        st.markdown("Which possible bias did you see.")

        options_7 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "7")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_7 = st.text_area("reasons", height = 100, key="7")


    
    st.markdown("## visual 8")

    image = imageio.imread('figures/fig_8.png')

    st.image(image)

    bias_8 = st.checkbox("Bias?", key=8)

    if bias_8:
        st.markdown("Which possible bias did you see.")

        options_8 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "8")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_8 = st.text_area("reasons", height = 100, key="8")





    st.markdown("## visual 9")

    image = imageio.imread('figures/fig_9.png')

    st.image(image)

    bias_9 = st.checkbox("Bias?", key=9)

    if bias_9:
        st.markdown("Which possible bias did you see.")

        options_9 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "9")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_9 = st.text_area("reasons", height = 100, key="9")


    st.markdown("## visual 10")

    image = imageio.imread('figures/fig_10.png')

    st.image(image)

    bias_10 = st.checkbox("Bias?", key=10)

    if bias_10:
        st.markdown("Which possible bias did you see.")

        options_10 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "10")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_10 = st.text_area("reasons", height = 100, key="10")



    st.markdown("## visual 11")

    image = imageio.imread('figures/fig_11.png')

    st.image(image)

    bias_11 = st.checkbox("Bias?", key=11)

    if bias_11:
        st.markdown("Which possible bias did you see.")

        options_11 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "11")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_11 = st.text_area("reasons", height = 100, key="11")



    st.markdown("## visual 12")

    image = imageio.imread('figures/fig_12.png')

    st.image(image)

    bias_12 = st.checkbox("Bias?", key=12)

    if bias_12:
        st.markdown("Which possible bias did you see.")

        options_12 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "12")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_12 = st.text_area("reasons", height = 100, key="12")


    st.markdown("## visual 13")

    image = imageio.imread('figures/fig_13.png')

    st.image(image)

    bias_13 = st.checkbox("Bias?", key=13)

    if bias_13:
        st.markdown("Which possible bias did you see.")

        options_13 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "13")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_13 = st.text_area("reasons", height = 100, key="13")



    st.markdown("## visual 14")

    image = imageio.imread('figures/fig_14.png')

    st.image(image)

    bias_14 = st.checkbox("Bias?", key=14)

    if bias_14:
        st.markdown("Which possible bias did you see.")

        options_14 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "14")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_14 = st.text_area("reasons", height = 100, key="14")



    st.markdown("## visual 15")

    image = imageio.imread('figures/fig_15.png')

    st.image(image)

    bias_15 = st.checkbox("Bias?", key=15)

    if bias_15:
        st.markdown("Which possible bias did you see.")

        options_15 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "15")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_15 = st.text_area("reasons", height = 100, key="15")



    
    st.markdown("## visual 16")

    image = imageio.imread('figures/fig_16.png')

    st.image(image)

    bias_16 = st.checkbox("Bias?", key=16)

    if bias_16:
        st.markdown("Which possible bias did you see.")

        options_16 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "16")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_16 = st.text_area("reasons", height = 100, key="16")

    
    st.markdown("## visual 17")

    image = imageio.imread('figures/fig_17.png')

    st.image(image)

    bias_17 = st.checkbox("Bias?", key=17)

    if bias_17:
        st.markdown("Which possible bias did you see.")

        options_17 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "17")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_17 = st.text_area("reasons", height = 100, key="17")

    
    if st.button("save"):
        dict_items = {"bias_1" : options_1, "bias_2": options_2, "bias_3" : options_3, 
        "bias_4" : options_4, "bias_5": options_5, "bias_6" : options_6, "bias_7": options_7, 
        "bias_8" : options_8, "bias_9" : options_9, "bias_10": options_10, "bias_11" : options_11,
        "bias_12": options_12, "bias_13" : options_13, "bias_14" : options_14, "bias_15": options_15,
        "bias_16" : options_16, "bias_17": options_17,
        "comment_1" : comment_1, "comment_2" : comment_2, "comment_3" : comment_3,
        "comment_4" : comment_4 , "comment_5" : comment_5, "comment_6" : comment_6, "comment_7" : comment_7, "comment_8" : comment_8,
        "comment_9" : comment_9 , "comment_9" : comment_9, "comment_10" : comment_10, "comment_11" : comment_11, "comment_12" : comment_12,
        "comment_13" : comment_13 , "comment_14" : comment_14, "comment_15" : comment_15, "comment_16" : comment_16, "comment_17" : comment_17,
        "visual_1": bias_1, "visual_2": bias_2, "visual_3": bias_3, 
        "visual_4": bias_4, "visual_5": bias_5, "visual_6": bias_6, "visual_7": bias_7, "visual_8": bias_8, 
        "visual_9": bias_9, "visual_10": bias_10,"visual_11": bias_11, "visual_12": bias_12, "visual_13": bias_13, 
        "visual_14": bias_14, "visual_15": bias_15,"visual_16": bias_16, "visual_17": bias_17
        }
        #data = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_items.items() ]))
        
        st.session_state["task1_results"] = dict_items
        
        #data.to_csv(r'C:\Users\reaf\EQ_AI\Data\bias.csv') 
        st.markdown("SAVED!")









def Group_3():

    options_1, options_2, options_3, options_4, options_5, options_6 = None, None, None, None, None, None, 
    options_7, options_8, options_9, options_10, options_11, options_12 = None, None, None, None, None, None,
    options_13, options_14, options_15, options_16, options_17 = None, None, None, None, None

    comment_1, comment_2, comment_3, comment_4, comment_5 = None, None, None, None, None
    comment_6, comment_7, comment_8, comment_9, comment_10 = None, None, None, None, None,
    comment_11, comment_12, comment_13, comment_14, comment_15 = None, None, None, None, None,
    comment_16, comment_17 = None, None


    st.markdown("# Task 1")
    st.markdown("Map biases (from a list of biases provided, with explanations, and the host there to elaborate or give example) to the use-case and then use a visualization (from Streamlit, a set of premade graphs or presets), giving justification for all this in Streamlit/a slide-deck")
    st.sidebar.markdown("# Task 1")



    st.markdown("""###### Your team has been presented with a Covid-19 Case Surveillance dataset. Each row in the dataset contains information about a de-identified patient. There are 19* columns in this dataset, 
There are (need to check after cleaning, dropping NANs) 20 million patients in this dataset. For the purpose of this task, this is considered a reasonable volume of data

For this use-case, you will audit the dataset for possible bias, and finally, propose a solution to a predictive model that was built upon this dataset.
Assume the model can only be deployed in a couple of months time after this use-case is completed

Your team has three tasks to complete, which involve auditing the dataset and model for bias, and finally, presenting a solution to reduce bias in the model’s predictions


**If your team see bias in a visualisation click the checkbox and please give a description of the bias seen**
 """)




    st.markdown("## visual 1")

    image = imageio.imread('figures/fig_1.png')
    st.image(image)

    bias_1 = st.checkbox("Bias?", key=1)

    if bias_1:
        st.markdown("Which possible bias did you see.")

        options_1 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "1")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_1 = st.text_area("reasons", height = 100, key="1")



    st.markdown("## visual 2")

    image = imageio.imread('figures/fig_2.png')

    st.image(image)

    bias_2 = st.checkbox("Bias?", key=2)

    if bias_2:
        st.markdown("Which possible bias did you see.")

        options_2 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "2")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_2 = st.text_area("reasons", height = 100, key="2")

    



    st.markdown("## visual 3")

    image = imageio.imread('figures/fig_3.png')

    st.image(image)

    bias_3 = st.checkbox("Bias?", key=3)

    if bias_3:
        st.markdown("Which possible bias did you see.")

        options_3 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "3")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_3 = st.text_area("reasons", height = 100, key="3")



    st.markdown("## visual 4")

    image = imageio.imread('figures/fig_4.png')

    st.image(image)

    bias_4 = st.checkbox("Bias?", key=4)

    if bias_4:
        st.markdown("Which possible bias did you see.")

        options_4 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "4")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_4 = st.text_area("reasons", height = 100, key="4")


    st.markdown("## visual 5")

    image = imageio.imread('figures/fig_5.png')

    st.image(image)

    bias_5 = st.checkbox("Bias?", key=5)

    if bias_5:
        st.markdown("Which possible bias did you see.")

        options_5 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "5")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_5 = st.text_area("reasons", height = 100, key="5")




    
    st.markdown("## visual 6")

    image = imageio.imread('figures/fig_6.png')

    st.image(image)

    bias_6 = st.checkbox("Bias?", key=6)

    if bias_6:
        st.markdown("Which possible bias did you see.")

        options_6 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "6")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_6 = st.text_area("reasons", height = 100, key="6")

    


    st.markdown("## visual 7")

    image = imageio.imread('figures/fig_7.png')

    st.image(image)

    bias_7 = st.checkbox("Bias?", key=7)

    if bias_7:
        st.markdown("Which possible bias did you see.")

        options_7 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "7")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_7 = st.text_area("reasons", height = 100, key="7")


    
    st.markdown("## visual 8")

    image = imageio.imread('figures/fig_8.png')

    st.image(image)

    bias_8 = st.checkbox("Bias?", key=8)

    if bias_8:
        st.markdown("Which possible bias did you see.")

        options_8 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "8")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_8 = st.text_area("reasons", height = 100, key="8")





    st.markdown("## visual 9")

    image = imageio.imread('figures/fig_9.png')

    st.image(image)

    bias_9 = st.checkbox("Bias?", key=9)

    if bias_9:
        st.markdown("Which possible bias did you see.")

        options_9 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "9")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_9 = st.text_area("reasons", height = 100, key="9")


    st.markdown("## visual 10")

    image = imageio.imread('figures/fig_10.png')

    st.image(image)

    bias_10 = st.checkbox("Bias?", key=10)

    if bias_10:
        st.markdown("Which possible bias did you see.")

        options_10 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "10")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_10 = st.text_area("reasons", height = 100, key="10")



    st.markdown("## visual 11")

    image = imageio.imread('figures/fig_11.png')

    st.image(image)

    bias_11 = st.checkbox("Bias?", key=11)

    if bias_11:
        st.markdown("Which possible bias did you see.")

        options_11 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "11")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_11 = st.text_area("reasons", height = 100, key="11")



    st.markdown("## visual 12")

    image = imageio.imread('figures/fig_12.png')

    st.image(image)

    bias_12 = st.checkbox("Bias?", key=12)

    if bias_12:
        st.markdown("Which possible bias did you see.")

        options_12 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "12")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_12 = st.text_area("reasons", height = 100, key="12")


    st.markdown("## visual 13")

    image = imageio.imread('figures/fig_13.png')

    st.image(image)

    bias_13 = st.checkbox("Bias?", key=13)

    if bias_13:
        st.markdown("Which possible bias did you see.")

        options_13 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "13")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_13 = st.text_area("reasons", height = 100, key="13")



    st.markdown("## visual 14")

    image = imageio.imread('figures/fig_14.png')

    st.image(image)

    bias_14 = st.checkbox("Bias?", key=14)

    if bias_14:
        st.markdown("Which possible bias did you see.")

        options_14 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "14")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_14 = st.text_area("reasons", height = 100, key="14")



    st.markdown("## visual 15")

    image = imageio.imread('figures/fig_15.png')

    st.image(image)

    bias_15 = st.checkbox("Bias?", key=15)

    if bias_15:
        st.markdown("Which possible bias did you see.")

        options_15 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "15")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_15 = st.text_area("reasons", height = 100, key="15")



    
    st.markdown("## visual 16")

    image = imageio.imread('figures/fig_16.png')

    st.image(image)

    bias_16 = st.checkbox("Bias?", key=16)

    if bias_16:
        st.markdown("Which possible bias did you see.")

        options_16 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "16")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_16 = st.text_area("reasons", height = 100, key="16")

    
    st.markdown("## visual 17")

    image = imageio.imread('figures/fig_17.png')

    st.image(image)

    bias_17 = st.checkbox("Bias?", key=17)

    if bias_17:
        st.markdown("Which possible bias did you see.")

        options_17 = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias",
        'Data missingness', 'Demographic bias', "data balance bias"], 
        key = "17")

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_17 = st.text_area("reasons", height = 100, key="17")

    
    if st.button("save"):
        dict_items = {"bias_1" : options_1, "bias_2": options_2, "bias_3" : options_3, 
        "bias_4" : options_4, "bias_5": options_5, "bias_6" : options_6, "bias_7": options_7, 
        "bias_8" : options_8, "bias_9" : options_9, "bias_10": options_10, "bias_11" : options_11,
        "bias_12": options_12, "bias_13" : options_13, "bias_14" : options_14, "bias_15": options_15,
        "bias_16" : options_16, "bias_17": options_17,
        "comment_1" : comment_1, "comment_2" : comment_2, "comment_3" : comment_3,
        "comment_4" : comment_4 , "comment_5" : comment_5, "comment_6" : comment_6, "comment_7" : comment_7, "comment_8" : comment_8,
        "comment_9" : comment_9 , "comment_9" : comment_9, "comment_10" : comment_10, "comment_11" : comment_11, "comment_12" : comment_12,
        "comment_13" : comment_13 , "comment_14" : comment_14, "comment_15" : comment_15, "comment_16" : comment_16, "comment_17" : comment_17,
        "visual_1": bias_1, "visual_2": bias_2, "visual_3": bias_3, 
        "visual_4": bias_4, "visual_5": bias_5, "visual_6": bias_6, "visual_7": bias_7, "visual_8": bias_8, 
        "visual_9": bias_9, "visual_10": bias_10,"visual_11": bias_11, "visual_12": bias_12, "visual_13": bias_13, 
        "visual_14": bias_14, "visual_15": bias_15,"visual_16": bias_16, "visual_17": bias_17
        }
        #data = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_items.items() ]))
        
        st.session_state["task1_results"] = dict_items
        
        #data.to_csv(r'C:\Users\reaf\EQ_AI\Data\bias.csv') 
        st.markdown("SAVED!")





def Bias():
    st.markdown("# Bias 🎉")
    st.sidebar.markdown("# Bias 🎉")

    st.markdown("### Human bias")

    st.table(df_human)


   


    st.markdown("### Data bias")

    st.table(df_data)

    

    st.markdown("### Algorithmic bias")

    st.table(df_algo)
         
page_names_to_funcs = {
    "Group 1": Group_1,
    "Group 2": Group_2,
    "Group 3": Group_3,
    "Bias": Bias,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()