from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from PyPDF2 import PdfReader

import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain.chains import conversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os


os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))






def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

#Create text chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size =1000, chunk_overlap = 20)
    chunks = text_splitter.split_documents(text)

    return chunks

def get_vector_store(text_chunks):
    embedding=GooglePalmEmbeddings()
    vector_store=FAISS.from_texts(text_chunks)
    return vector_store

def get_conversational_chain(vector_store):
    llm = GeminiProVision()
    merory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    conversation_chain=conversationalRetrievalChain.from_llm(llm=llm,retrievar=vector_store.as_retriever(),memory=merory)
    return conversation_chain

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")