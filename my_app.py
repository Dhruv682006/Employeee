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




















