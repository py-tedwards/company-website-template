import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title("The Best Company")

header_content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do 
eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

st.write(header_content)

st.header("Our Team")

df1 = pandas.read_csv('data.csv')

col1, empty_col1, col2, empty_col2, col3 = st.columns([1, 0.25, 1, 0.25, 1])

for index, row in df1[:4].iterrows():
    with col1:
        st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.image(f"images/{row['image']}")
        st.write(row['role'])

for index, row in df1[4:8].iterrows():
    with col2:
        st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.image(f"images/{row['image']}")
        st.write(row['role'])

for index, row in df1[8:].iterrows():
    with col3:
        st.subheader(f"{row['first_name'].title()} {row['last_name'].title()}")
        st.image(f"images/{row['image']}")
        st.write(row['role'])