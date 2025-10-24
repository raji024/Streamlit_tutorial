import streamlit as st
import pandas as pd
st.title("Stream lit elemnt demo")
df = pd.DataFrame({
    'Name':['Alice','bob','Charlie','David'],
     'Age':[25,32,37,45],
     'Occupation':['Enginner','Doctor','Artist','chef'
                   ]
    
})
st.dataframe(df)
st.subheader("data editor")
editable_df = st.data_editor(df)
# after writing that editable i can have the access to chaneg it and again i print(editable_df) it print the editable df which wechange it

st.subheader("Static Table")
st.table(df)
# json ad dictionary
st.subheader("JSON and dictionary")
sample_dict ={
    "name":"Alice",
    "age": 25,
    "Skills":["Python","Data science","Machine Learning"]

}
st.json(sample_dict)
# it is for simply wiriting it

st.write(sample_dict)


