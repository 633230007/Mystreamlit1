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
    st.header("<center>flower01</center>")
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
