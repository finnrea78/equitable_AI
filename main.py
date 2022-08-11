# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pickle as pkle
import os.path
import pandas as pd
import imageio

next = st.sidebar.button('Next on list')
Last = st.sidebar.button('Last on list')


new_choice = ['Welcome', 'Glossary']



# This is what makes this work, check directory for a pickled file that contains
# the index of the page you want displayed, if it exists, then you pick up where the
#previous run through of your Streamlit Script left off,
# if it's the first go it's just set to 0
if os.path.isfile('next.p'):
    index = pkle.load(open('next.p', 'rb'))
    # check if you are at the end of the list of pages
    if index == len(new_choice):
        index = 0 # go back to the beginning i.e. homepage
    if index == -1:
        index = len(new_choice)
else:
    index = 0 #the start


# this is the second tricky bit, check to see if the person has clicked the
# next button and increment our index tracker (next_clicked)
if next:
    #increment value to get to the next page
    index = index +1
    # check if you are at the end of the list of pages again
    if index == len(new_choice):
        index = 0 # go back to the beginning i.e. homepage

if Last:
    index = index - 1
    if index < 0:
        index = len(new_choice)-1 

# create your radio button with the index that we loaded
choice = st.sidebar.radio("go to",('Welcome', 'Glossary'), index=index)

# pickle the index associated with the value, to keep track if the radio button has been used
pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

# finally get to whats on each page
if choice == 'Welcome':
    selected_page = "Welcome"
elif choice == 'Glossary':
    selected_page = "Glossary"


def main_page():
    st.markdown("# Welcome")
    st.sidebar.markdown("# Welcome")

    image = imageio.imread('figures/logo.JPG')
    st.image(image, width = 500)

def page3():
    st.markdown("# Glossary ")
    st.sidebar.markdown("# Glossary ")

    st.markdown("""### **Bias**: 
    A systematic error. In the context of fairness, we are concerned with 
    unwanted bias that places privileged groups at systematic advantage and 
    unprivileged groups at systematic disadvantage.""")
    st.markdown("""### **Bias mitigation algorithm:**
    A procedure for reducing unwanted bias in training data or models.""")
    st.markdown("""### **Label:** 
    The attribute that a model tries to predict. A diagnostic model may assign 
    the labels "Healthy" or "Not healthy" to each patient, ideally with high accuracy.""")
    st.markdown("""### **Machine learning:** 
    The process of a program or algorithm learning from the data it is provided
    in order to identify patterns, make decisions and improve itself over time.""")
    st.markdown("""### **Model:** 
    A program or algorithm that takes in data as an input and predicts 
    something about this data. For example, given a patient dataset, 
    predicting whether that patient is likely to have lung cancer.""")
    st.markdown("""### **Training data:** 
    A dataset from which a model is learned.""")
    st.markdown("""### **Fairness metric:** 
    A numeric representation of unwanted bias in training data or models. 
    For example, overall accuracy of a model for prediction could be 80%, 
    but if you check demographic parity, to see accuracy for each demographic 
    (e.g accuracy for African Americans), this accuracy may be significantly 
    lower for certain demographics.""")

page_names_to_funcs = {
    "Welcome": main_page,
    "Glossary": page3,
}

page_names_to_funcs[selected_page]()

