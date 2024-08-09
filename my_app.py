import streamlit as st

st.write("Hello Word: Getting Bore, Hello Brothe")

st.title("Display Title use st.title")

st.write("To write text use st.write()")

st.header("I am header to write header use st.header")

st.subheader("I am subheader to write subheader use st.subheder")

st.text("Hey I am simpele text to write simpel text use st.text")

# to create hyperlink
st.markdown("[streamlit](https://streamlit.io/)")

st.markdown("[streamlit Cheatsheet](https://cheat-sheet.streamlit.app/)")

st.success("success!")

st.info("Information")

st.warning("This is a warning")

st.error("this is an error!")

from PIL import Image
img = Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayate")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://youtu.be/kYcu17Eci0A?si=XW0qZR3clwCb0USh")

audio_file = open("song.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")



st.header("Button widgets")

if st.button("Play1"):
    st.text("Hello word")
    
if st.button("play2"):
    st.text("Enjoy Music")
    st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox selected")
st.video("https://youtu.be/R3SHDFssDwg?si=iXDV7HWPbzOXiJre")
st.video("https://youtu.be/yWAA2Y9bZ40?si=SNswYVCzRsNlvCze")


if st.checkbox("checkbox"):
    st.text("checkbox selection")
#------------today--------------#

radio_but = st.radio("Youe Selection", ["Male","Female"])
if radio_but == "Male":
    st.info("you are Male")
else:
    st.info("you are Female")

    
City = st.selectbox("your City", ["Dman","Div","Valsad"])
if City == "Daman":
    st.info("I love Daman")
elif City == "Div":
    st.info("I love Div")
else:
    st.info("I love Valsad")
    

#--------Pandas DataFrame----------#
import streamlit as st
import pandas as pd

auto_data= pd.read_csv("auto.csv")
st.dataframe(auto_data.head())

st.table(auto_data.head(10))

st.area_chart(auto_data[["mpg","cylinders"]])
st.area_chart(auto_data[["mpg","cylinders"]].head(20))

st.bar_chart(auto_data[["mpg","cylinders"]])
st.bar_chart(auto_data[["mpg","cylinders"]].head(20))


st.line_chart(auto_data[["mpg","cylinders"]])
st.line_chart(auto_data[["mpg","cylinders"]].head(20))

import datetime
import time

today = st.date_input("Today is",datetime.datetime.now())
hour = st.time_input("The time is",datetime.time(12,30))

st.code("import pandas as pd")
st.code("print(WeLcome to NIELIT Daman)")

import pandas as pd 
import numpy as np

st.title("Area")
df=pd.DataFrame(np.random.randn(40,4),columns=["c1","c2","c3","c4"])
st.bar_chart(df)

st.title("Line chart")
df=pd.DataFrame(np.random.randn(40,4),columns=["c1","c2","c3","c4"])
st.line_chart(df)

st.title("Area")
df=pd.DataFrame(np.random.randn(40,4),columns=["c1","c2","c3","c4"])
st.area_chart(df)












