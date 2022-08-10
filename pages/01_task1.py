import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
import json

import imageio
import matplotlib.pyplot as plt


# url = "https://data.cdc.gov/resource/n8mc-b4w4.json"
# response = urlopen(url)
# data_json = json.loads(response.read())



#df = pd.read_csv(r".\Data\Adult.csv")

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





def Description():

    options, options_2, options_3, options_4, options_5, options_6 = None, None, None, None, None, None
    comment_1, comment_2, comment_3 = None, None, None


    st.markdown("# Description 🎈")
    st.markdown("Map biases (from a list of biases provided, with explanations, and the host there to elaborate or give example) to the use-case and then use a visualization (from Streamlit, a set of premade graphs or presets), giving justification for all this in Streamlit/a slide-deck")
    st.sidebar.markdown("# Description 🎈")



    st.markdown("""###### Your team has been presented with a Covid-19 Case Surveillance dataset. Each row in the dataset contains information about a de-identified patient. There are 19* columns in this dataset, 
There are (need to check after cleaning, dropping NANs) 20 million patients in this dataset. For the purpose of this task, this is considered a reasonable volume of data

For this use-case, you will audit the dataset for possible bias, and finally, propose a solution to a predictive model that was built upon this dataset.
Assume the model can only be deployed in a couple of months time after this use-case is completed

Your team has three tasks to complete, which involve auditing the dataset and model for bias, and finally, presenting a solution to reduce bias in the model’s predictions


**If your team see bias in a visualisation click the checkbox and please give a description of the bias seen**
 """)








    st.markdown("## visual 1")

    image = imageio.imread('figures/figure.jpg')

    st.image(image)

    bias_1 = st.checkbox("Bias?")

    if bias_1:
        st.markdown("Which possible bias did you see.")

        options = st.multiselect(
        'What bias did you see',
        ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
        "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
        "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias"], 
        key = "1")

        options_2 = (st.multiselect(
        'What bias did you see in this visulisation bias did you see',
        ['Data missingness', 'Demographic bias', "data balance bias"],
        key="1"))

        st.write("**Add reasons:**")
        st.write("could you give reasons for your first selection")
        comment_1 = st.text_area("reasons", height = 100, key="1")






    st.markdown("## visual 2")

    image = imageio.imread('figures/figure.jpg')

    st.image(image)

    st.markdown("Which possible bias did you see.")

    options_3 = st.multiselect(
     'What bias did you see',
     ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
     "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
     "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias"],
     key="2")

    options_4 = (st.multiselect(
     'What bias did you see in this visulisation bias did you see',
     ['Data missingness', 'Demographic bias', "data balance bias"],
     key="2"))


    st.write("**Add reasons:**")
    st.write("could you give reasons for your second selection")
    comment_2 = st.text_area("reasons", height = 100, key="2")
    





    st.markdown("## visual 3")



    image = imageio.imread('figures/figure.jpg')

    st.image(image)

    st.markdown("Which possible bias did you see.")

    options_5 = st.multiselect(
     'What bias did you see',
     ['Confirmation bias', 'Historical bias', "Mislabelling bias", 
     "Measurement bias", 'Selection bias' , "Association bias", "Exclusion bias", 
     "Aggregation bias", "Measurement bias", "Evaluation bias", "Algorithmic bias"],
     key="3")

    options_6 = (st.multiselect(
     'What bias did you see in this visulisation bias did you see',
     ['Data missingness', 'Demographic bias', "data balance bias"],
     key="3"))


    st.write("**Add reasons:**")
    st.write("could you give reasons for your third selection")
    comment_3 = st.text_area("reasons", height = 100, key="3")


    
    if st.button("save"):
        dict_items = {"bias_1" : options, "bias_2": options_2, "bias_3" : options_3, 
        "Comment_1" : comment_1, "Comment_2" : comment_2, "Comment_3" : comment_3}
        data = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dict_items.items() ]))
        
        st.session_state["task1_results"] = data
        
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
    "Description": Description,
    "Bias": Bias,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()