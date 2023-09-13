import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,emptycol, col2 = st.columns([0.5,0.1,2])

with col1:
    st.image("images/AniPhoto_Glasses_Croped.jpg")

with col2:
    st.title("Anirudh Kocherlakota")
    content = """Hi, I am Anirudh! I am a Python programmer.
     I am passionate about Machine Learning and Artificial Intelligence. 
     I am currently trying to get a deep understanding of basics of AI and ML.
     """
    st.info(content)

st.markdown("---")
content2 = '''Below apps are built in Python. Feel free to contact me!'''
st.info(content2)


col3, emptycol1, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.text("\n")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.text("\n")