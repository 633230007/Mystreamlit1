import streamlit as st

st.title('My title ทดสอบด้วย streamlit')

st.header("Theerakan 633230007")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")

with col1:
    st.header("TKKiT0007")
    st.image("./pic/iris1.jpg")

with col2:
    st.header("TKKiT633230007")
    st.subheader("คณะวิทยาศาสตร์และเทคโนโลยี")
    st.text("เทคโนโลยีสารสนเทศ")
    st.write("หมู่เรียน 24.2")
    st.markdown("มหาวิทยาลัยราชภัฏนครปฐม")

html_1 = """
<div style="background-color:#335EFF;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

col1v, col2v,col3v = st.columns(3)
#col1.write("This is column 1")
#col2.write("This is column 2")

with col1v:
    st.header("flower01")
    st.image("./pic/iris1.jpg")

with col2v:
    st.header("flower02")
    st.image("./pic/iris2.jpg")
with col3v:
    st.header("flower03")
    st.image("./pic/iris3.jpg")
  #  st.image("")

st.header('My header')
st.subheader('My sub')

import pandas as pd
dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

st.button("showChart")

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()
dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])

if st.button("show Chart"):
    st.bar_chart(dx2)
    st.button("don't show Chart")
else:
    st.button("don't show Chart")

html_2 = """
<div style="background-color:#335EFF;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุณาเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal.width")
