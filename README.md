# information-retrieval-system/QA System
📄 PDF Information Retrieval System/QA System
This project is designed to build an interactive system that allows users to retrieve information from PDF files using natural language queries. It leverages Google Generative AI for embeddings and FAISS for efficient vector-based searches, allowing users to ask questions based on the content of the uploaded PDFs.
🌟 Features
•	PDF Upload: Users can upload multiple PDF files which are processed into searchable text chunks.
•	Text Chunking: Large PDF content is split into manageable pieces using LangChain's RecursiveCharacterTextSplitter.
•	Vector Store: The system generates embeddings for the text chunks using Google Generative AI and stores them in a local FAISS vector index.
•	Question Answering: Once the index is created, users can ask questions in natural language. The system retrieves relevant document chunks using similarity search and provides detailed answers, powered by Google Generative AI.
🔧 Technologies Used
•	Streamlit: Provides an intuitive and interactive web interface.
•	PyPDF2: Used to extract text from PDF files.
•	LangChain: Helps with text chunking and embeddings integration.
•	FAISS (Facebook AI Similarity Search): Efficiently searches for similar text chunks.
•	Google Generative AI: Provides embeddings and chat functionality for both vector searches and answering questions.
🧠 Prompt Design
The system uses a custom prompt template to ensure detailed and accurate responses. The prompt is designed to retrieve answers only from the relevant context, ensuring that if the answer cannot be found, the system responds with "answer is not available in the context." This helps avoid any misleading or incorrect information.
🛠️ How it Works
1.	Upload PDF Files: Users upload PDF documents via the Streamlit interface.
2.	Text Processing: The system extracts text from the PDFs and chunks it into smaller, manageable pieces.
3.	Vector Indexing: Text chunks are converted into vector embeddings using Google Generative AI and stored in a FAISS index.
4.	Ask a Question: Users can then ask questions about the content of the PDFs. The system retrieves the most relevant text chunks and generates detailed answers based on the provided context.
📋 Prerequisites
•	Python 3.10
•	Install dependencies with pip install -r requirements.txt.
•	Set up your .env file with your GOOGLE_API_KEY.
🚀 How to Run the Project
1.	Clone the repository
2.	Install the required dependencies: pip install -r requirements.txt
3.	Run the Streamlit app: streamlit run app.py
4.	Upload PDFs via the interface, process them, and ask questions!

