## 1. Integrate our Code with OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI # OPENAI API Import 

from langchain import PromptTemplate
from langchain.chains import LLMChain # Resp for executing LLM Chains - Linking & Creating Multiple Prompt Templates

# Problem is that it only shows the result of the last chain 
from langchain.chains import SimpleSequentialChain # Combines all the Sequences and when runned as a Parent Chain gives the results of all the chains together, instead of parallely running all the chains ind.
from langchain.chains import SequentialChain 

from langchain.memory import ConversationalBufferMemory

os.environ['OPENAI_API_KEY'] = openai_key

import streamlit as st

# Streamlit Framework

st.title('Celebrity Search Results')
input_text = st.text_input('Search the Topic you want !!') # text box is also created

## Openai LLMs
llm = OpenAI(temperature=0.8)

# Prompt Templates

# PT 1 -- first Para - Name [in the text box will give on celebrity Name]
first_input_prompt = PromptTemplate(input_variables = ['name'], template = "Tell me about celebrity whose name is {name}") # template on which it will search 
chain = LLMChain(llm=llm, prompt = first_input_prompt,verbose = True,output_key = 'person',memory = person_memory)

# Memory 
person_memory = ConversationalBufferMemory(input_key = 'name', memory_key = 'chat_history')
dob_memory = ConversationalBufferMemory(input_key = 'person', memory_key = 'chat_history')
descr_memory = ConversationalBufferMemory(input_key = 'dob', memory_key = 'description_history')

# PT 2 
sec_input_prompt = PromptTemplate(input_variables = ['person'], template = "When was {person} born")
chain2 = LLMChain(llm=llm, prompt = sec_input_prompt,verbose = True,output_key = 'dob',memory = dob_memory)

# PT 3
third_input_prompt = PromptTemplate(input_variables = ['dob'], template = "Mention 5 Major Events happened around {dob} in the world")
chain3 = LLMChain(llm=llm, prompt = third_input_prompt,verbose = True,output_key = 'description',memory = descr_memory)

parent_chain = SequentialChain(chains = [chain,chain2,chain3],input_variables = ['name'],output_variables = ['person','dob','description'],verbose=temperature)



if input_text:
    #st.write(llm(input_text))
    # st.write(chain.run(input_text))  -- celebrity name
    st.write(parent_chain({'name':input_text}))

    with st.expander('Celebrity Name & Brief Overview'):
        st.info('person_memory.buffer')

    with st.expander('Celebrity D.O.B'):
        st.info('dob_memory.buffer')

    with st.expander('Major Events that happen on this Date !!'):
        st.info('descr_memory.buffer')
        


