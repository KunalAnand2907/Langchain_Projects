## 1. Integrate our Code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI # OPENAI API Import 

os.environ['OPENAI_API_KEY'] = openai_key

import streamlit as st

# Streamlit Framework

st.title('Langchain Demo with OpenAI API')
input_text = st.text_input('Search the Topic you want !!') # text box is also created

## Basic Openai LLMs - Using the Open api to create the search a topic functionality

llm = OpenAI(temperature=0.8)  # temp -- def value as 0.8, agent should have how much control in responsing - values range from 0 to 1, less value ~ 0.2 agent will lose control

if input_text: # !=''
    st.write(llm(input_text))
