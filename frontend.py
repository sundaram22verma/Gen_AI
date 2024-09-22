import streamlit as st # type: ignore
import backend as bk

st.title("Gen AI ")

if 'question_input' not in st.session_state:
    st.session_state['question_input'] = ''

input = st.text_input("What's Your Question !!!", key='question_input') 
go_btn = st.button("GO")

if go_btn:
    output = bk.get_text_stream_output(st.session_state['question_input'])
    st.write(output)

def clear_inputs():
    st.session_state['question_input'] = ''

clear_btn = st.button("Clear Inputs", on_click=clear_inputs)

