import streamlit as st
from IPython.display import YouTubeVideo
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import base64

genai.configure(api_key="YOUR_KEY")

##I use model gemini-pro
model = genai.GenerativeModel("gemini-pro")


# Function to summarize text
def generate_summary(prompt, transcript):
    response = model.generate_content(prompt + transcript)
    return response.text

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += '' + i['text']
    return result

# Function to check if a YouTube video is valid and available
def is_valid_youtube_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False

# Function to check if a YouTube video is available
def is_youtube_video_available(video_id):
    video_info_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    try:
        response = requests.get(video_info_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        return False
    
#Functions to change Background Changes
    
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    opacity: 0.8;  /* Adjust opacity as needed */
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Custom function to change color of text
def color_text(text, color):
    return f'<span style="color:{color};font-size:24px">{text}</span>'


# Custom CSS to change font color for heading and subheading
custom_css = """
    <style>
        .heading-text {
            color: purple; /* Change color as per your preference */
           
        }
        .subheading-text {
            color: purple; /* Change color as per your preference */
            
        }
    </style>
"""

# Render custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit app
def main():

    set_png_as_page_bg('pod_image.png')
    # st.title("Podcast Summarizer")
    st.markdown("<h1 class='heading-text'>Podcast Summarizer</h1>", unsafe_allow_html=True)

    # Input field for YouTube URL
    youtube_url = st.text_input("Enter YouTube Podcast URL:") 

    
    if youtube_url:
        video_id = youtube_url.split("=")[-1]  # Extract video ID from URL
        # st.subheader("YouTube Video")
        st.markdown("<h2 class='subheading-text'>YouTube Video</h2>", unsafe_allow_html=True)

        # YouTubeVideo(video_id)
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)


            # Check if the YouTube URL is valid
        if not is_valid_youtube_url(youtube_url):
            st.error("Invalid YouTube URL. Please enter a valid URL.")
            return
        
        # Check if the YouTube video is available
        if not is_youtube_video_available(video_id):
            st.error("The YouTube video is unavailable. Please try another video.")
            return
        try:
            transcript_text=get_transcript(video_id)
        except:
            st.error("Plz try with another youtube URL")

            
    if st.button("Summarize"):
            # st.subheader("Summary")
            st.markdown("<h2 class='subheading-text'>Summary</h2>", unsafe_allow_html=True)

            prompt="You are a Podcast Summary Generator. Your job involves condensing YouTube transcripts into concise summaries, Start with the Introduction who is organizing the podcast who is the guest and what is main topic of podcast and then capture the key highlights in bullet points.Summary should not be more than 200 words.Below is transcript text:\n"
 
            summary = generate_summary(prompt,transcript_text)
            st.markdown(f"<div style='background-color:white;color:black;padding:10px;border-radius:10px;'>{summary}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
