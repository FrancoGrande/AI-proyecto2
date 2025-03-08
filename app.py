import os
import requests
import io
import pdfminer.high_level
import docx
from bs4 import BeautifulSoup
import google.generativeai as genai
import streamlit as st
from deep_translator import GoogleTranslator
import toml
import os

# Read the API key from secrets.toml
secrets = toml.load("secrets.toml")
GOOGLE_API_KEY = secrets["gemini"]["api_key"]

# Set up the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-001')


def summarize_text(text):
    """Summarizes the given text using the Gemini model."""
    prompt = f"Summarize the following text, extracting the main ideas.  Keep the summary concise and to the point:\n\n{text}\n\nSummary:"
    response = model.generate_content(prompt)
    return response.text


def translate_text(text, target_language='es'):
    """Translates the given text to the target language."""
    try:
        translator = GoogleTranslator(source='auto', target=target_language)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Translation error: {e}"


def extract_text_from_url(url):
    """Extracts text content from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract all text from the body
        text = ' '.join(soup.body.stripped_strings)
        return text
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"


def extract_text_from_pdf(file_path):
    """Extracts text content from a PDF file."""
    try:
        with open(file_path, 'rb') as f:
            text = pdfminer.high_level.extract_text(f)
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {e}"


def extract_text_from_docx(file_path):
    """Extracts text content from a Word document."""
    try:
        doc = docx.Document(file_path)
        text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"


def process_input(input_data, input_type):
    """Processes the input data based on the specified type."""
    if input_type == 'url':
        return extract_text_from_url(input_data)
    elif input_type == 'pdf':
        return extract_text_from_pdf(input_data)
    elif input_type == 'docx':
        return extract_text_from_docx(input_data)
    elif input_type == 'text':
        return input_data
    else:
        return "Invalid input type."


# Streamlit UI
st.title("Article Summarizer")

input_type = st.selectbox("Input Type:", ["url", "pdf", "docx", "text"])

if input_type == "pdf" or input_type == "docx":
    input_data = st.file_uploader(f"Upload {input_type.upper()} file", type=[input_type])
    if input_data is not None:
        # Save the uploaded file to a temporary location
        temp_file_path = f"temp.{input_type}"
        with open(temp_file_path, "wb") as f:
            f.write(input_data.read())
        text = process_input(temp_file_path, input_type)
        os.remove(temp_file_path)  # Remove the temporary file
    else:
        text = None
elif input_type == "text":
    input_data = st.text_area("Enter Text:", "")
    text = process_input(input_data, input_type)
else:
    input_data = st.text_input("Enter URL:", "")
    text = process_input(input_data, input_type)


if text:
    if isinstance(text, str):
        summary = summarize_text(text)
        translated_summary = translate_text(summary)
        st.subheader("Summary (Spanish - Argentina):")
        st.write(translated_summary)
    else:
        st.error(text)