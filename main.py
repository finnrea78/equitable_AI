# Contents of ~/my_app/streamlit_app.py
import streamlit as st
import pickle as pkle
import os.path
import pandas as pd
import imageio


df = pd.read_csv(r"https://raw.githubusercontent.com/finnrea78/equitable_AI/main/Data/Adult.csv")



next = st.sidebar.button('Next on list')
Last = st.sidebar.button('Last on list')


new_choice = ['Welcome','Data','Glossary']



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
choice = st.sidebar.radio("go to",('Welcome', 'Data', 'Glossary'), index=index)

# pickle the index associated with the value, to keep track if the radio button has been used
pkle.dump(new_choice.index(choice), open('next.p', 'wb'))

# finally get to whats on each page
if choice == 'Welcome':
    selected_page = "Welcome"
elif choice == 'Data':
    selected_page = "Data"
elif choice == 'Glossary':
    selected_page = "Glossary"


def main_page():
    st.markdown("# Welcome")
    st.sidebar.markdown("# Welcome")

    image = imageio.imread('figures/logo.JPG')
    st.image(image, width = 1000)


def page2():
    st.markdown("# Data")
    st.sidebar.markdown("# Data")
    st.text("Here is a snap shot of the data we will be using to detect bias.")
    st.dataframe(df, 2000, 500)

def page3():
    st.markdown("# Glossary ")
    st.sidebar.markdown("# Glossary ")

    st.markdown("""### **Bias**: 
    A systematic error. In the context of fairness, we are concerned with unwanted 
    bias that places privileged groups at systematic advantage and unprivileged 
    groups at systematic disadvantage.""")
    st.markdown("""### **Bias mitigation algorithm:**
    A procedure for reducing unwanted bias in training data or models.""")
    st.markdown("""### **Label:** 
    A value corresponding to an outcome.""")
    st.markdown("""### **Machine learning:** 
    A general approach for determining models from data.""")
    st.markdown("""### **Model:** 
    A function that takes features as input and predicts labels as output.""")
    st.markdown("""### **Training data:** 
    A dataset from which a model is learned.""")
    st.markdown("""### **Fairness metric:** 
    A quantification of unwanted bias in training data or models.""")

page_names_to_funcs = {
    "Welcome": main_page,
    "Data": page2,
    "Glossary": page3,
}

page_names_to_funcs[selected_page]()

