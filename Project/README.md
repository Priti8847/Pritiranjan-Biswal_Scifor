
# ChatPDF App

The ChatPDF App is a Streamlit-based chatbot designed to interact with PDF documents using the LangChain and OpenAI LLM (Large Language Model) technology. With this app, you can upload PDF files, extract text from them, and ask questions or make queries related to the content of the PDF.

## About

This app leverages various technologies and libraries to provide a seamless experience for working with PDF documents:

- [Streamlit](https://streamlit.io/): A Python library for creating web apps with minimal code, which is used for the user interface of the ChatPDF App.
- [LangChain](https://python.langchain.com/): A powerful library for text and language processing, enabling text splitting, embeddings, and question-answering capabilities.
- [OpenAI LLM](https://platform.openai.com/docs/models): The OpenAI Large Language Model is used to generate responses to user queries based on the provided PDF content.

## Usage

### Uploading a PDF

1. Open the ChatPDF App.
2. Use the file uploader to upload your PDF document. The app will extract text from the PDF automatically.

### Asking Questions

1. Once the PDF is uploaded, you can ask questions or make queries about the content.
2. Enter your question in the provided text input box.

### Getting Responses

The app will provide responses to your questions based on the content of the PDF. It uses LangChain for text processing and OpenAI LLM for generating responses.

## Dependencies

Make sure to have the following libraries and components installed:

- Streamlit
- dotenv
- PyPDF2
- streamlit_extras
- langchain
- OpenAI


You can install these dependencies using `pip`:

```bash
pip install streamlit dotenv PyPDF2 streamlit_extras langchain openai pydantic
