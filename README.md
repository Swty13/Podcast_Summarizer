# Podcast Summarizer

Podcast Summarizer is a tool built to generate concise summaries of podcast episodes based on their transcripts. It takes the transcript of a podcast episode as input and provides a summarized version of the content, making it easier for users to grasp the main points discussed in the episode without having to listen to the entire podcast.


# How it works?

[![Watch the video](pdcast_video.mov)]

## Features

- Summarize podcast episodes: Generate summarized versions of podcast episodes by extracting key points from their transcripts.
- YouTube integration: Accepts YouTube podcast URLs as input, making it convenient to summarize podcast episodes hosted on YouTube.
- Automatic summarization: Utilizes machine learning models to automatically generate summaries, saving time and effort for users.
- Streamlit interface: Provides a user-friendly interface built with Streamlit, allowing users to interact with the tool seamlessly.

## Getting Started

To get started with Podcast Summarizer, follow these steps:

1. Clone the repository:

    `git clone https://github.com/your-username/podcast-summarizer.git`
2. Install the required dependencies:

    `pip install -r requirements.txt`

3. Run the Streamlit app:
        `streamlit run main.py`

4. Enter the YouTube podcast URL in the input field.
5. Click the "Summarize" button to generate a summary of the podcast episode.

## Dependencies

- Streamlit
- Google GenerativeAI
- youtube_transcript_api
- requests
- base64

## Usage

- Enter the YouTube podcast URL in the provided input field.
- Click the "Summarize" button to generate a summary of the podcast episode.
- The summarized text will be displayed below the input field.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- This project utilizes the Google GenerativeAI API for text summarization.
- Special thanks to the Streamlit and Google GenerativeAI communities for their support and contributions.


