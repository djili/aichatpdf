# AI Chat with PDF

AI Chat with PDF is a powerful application that allows you to have natural conversations with your PDF documents. Using state-of-the-art language models and embeddings, the application can understand and answer questions about the content of your PDF files.

## Features

- 📄 Upload and process PDF documents
- 💬 Chat with your documents using natural language
- 🔍 Retrieve relevant information from large documents
- 🧠 Built with LangChain and OpenAI's powerful language models
- 🚀 Streamlit-based web interface

## Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) (recommended) or pip
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/djili/aichatpdf.git
   cd aichatpdf
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
   
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Start the application:
   ```bash
   poetry run streamlit run app.py
   ```
   
   Or with pip:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501`

3. Upload a PDF file using the file uploader

4. Start chatting with your document by typing questions in the chat interface

## How It Works

1. The application processes your PDF document and extracts the text content
2. The text is split into manageable chunks
3. These chunks are converted into vector embeddings using HuggingFace embeddings
4. When you ask a question, the system finds the most relevant text chunks
5. The relevant context is sent to the language model to generate an answer

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web application framework
- [LangChain](https://python.langchain.com/) - Framework for developing applications with LLMs
- [OpenAI](https://openai.com/) - Language models for generating responses
- [HuggingFace](https://huggingface.co/) - Embeddings for document retrieval
- [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search
- [PyPDF2](https://pypi.org/project/PyPDF2/) - PDF processing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with ❤️ using amazing open-source libraries
- Inspired by the growing ecosystem of AI-powered document processing tools

---

**Note:** Make sure to handle sensitive documents appropriately and be aware of the data you're processing through the application.
