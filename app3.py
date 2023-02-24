import streamlit as st
from pytube import YouTube
import os
from googletrans import Translator

def download_video(video_url):
    try:
        # create a YouTube object
        yt = YouTube(video_url)

        # get the highest resolution video stream
        stream = yt.streams.get_highest_resolution()

        # download the video
        video_path = stream.download()

        # show a success message
        st.success("Video downloaded successfully!")

        # display the downloaded video
        st.video(video_path)

    except Exception as e:
        # show an error message
        st.error(f"Error downloading video: {str(e)}")

def translate_text(text, language):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=language)
    return translation.text

def app1():
    st.title("YouTube Video Downloader")
    video_url = st.text_input("Enter the YouTube video URL:")
    if st.button("Download"):
        download_video(video_url)
    st.write("Current working directory:", os.getcwd())

def app2():
    st.title("Text Translator")
    text = st.text_area("Enter text to translate:")
    language = st.selectbox("Select language to translate to:", ("English", "Spanish", "French", "German", "Bengali"))
    language_dict = {"English": "en", "Spanish": "es", "French": "fr", "German": "de", "Bengali": "bn"}
    language_code = language_dict[language]
    if st.button("Translate"):
        if text:
            translation = translate_text(text, language_code)
            st.write("Translation:")
            st.write(translation)
        else:
            st.warning("Please enter some text to translate")

# Create the mult-page app
def main():
    st.set_page_config(page_title="My Streamlit App")

    pages = {
        "YouTube Video Downloader": app1,
        "Text Translator": app2,
    }

    st.sidebar.title("Select a page")
    selection = st.sidebar.radio("", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
