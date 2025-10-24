import streamlit as st
import os
st.title("basics")
st.header("This is header")
st.subheader("this is subheader")
st.markdown("this is _markdown_")
st.caption("Small text")
code_example = """
def greet(name):
    print("hello")
"""
st.code(code_example,language="python")
st.divider() 
st.image(os.path.join(os.getcwd(),"static","i1.jpg"))
