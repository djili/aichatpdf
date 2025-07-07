# AI Chat with PDF

AI Chat with PDF is a powerful application that allows you to have natural conversations with your PDF documents. Using state-of-the-art language models and HuggingFace embeddings, the application can understand and answer questions about the content of your PDF files in a conversational manner.

## Features

- 📄 Upload and process multiple PDF documents simultaneously
- 💬 Interactive chat interface with conversation history
- 🔍 Semantic search using HuggingFace embeddings
- 🧠 Powered by LangChain and HuggingFace models
- 🚀 Modern Streamlit-based web interface
- 🌍 Multilingual support (French/English)

## Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) (recommended) or pip
- HuggingFace API key (optional, for some models)

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
   - Configure your preferred models and API keys:
   ```bash
   # For OpenAI models (optional)
   OPENAI_API_KEY=your_openai_key
   
   # For HuggingFace models (recommended)
   HUGGINGFACEHUB_API_TOKEN=your_hf_token
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
2. The text is split into manageable chunks using recursive text splitting
3. These chunks are converted into vector embeddings using HuggingFace's instructor-xl model
4. When you ask a question, the system performs a semantic search to find the most relevant text chunks
5. The conversation history and relevant context are used to generate a coherent response
6. The chat interface maintains conversation history for context-aware responses

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web application framework
- [LangChain](https://python.langchain.com/) - Framework for developing applications with LLMs
- [LangChain](https://python.langchain.com/) - Framework for LLM applications
- [HuggingFace](https://huggingface.co/) - For embeddings and language models
- [FAISS](https://github.com/facebookresearch/faiss) - Efficient similarity search
- [PyPDF2](https://pypi.org/project/PyPDF2/) - PDF text extraction
- [Streamlit](https://streamlit.io/) - Web application framework
- [Sentence Transformers](https://www.sbert.net/) - For generating embeddings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with ❤️ using amazing open-source libraries
- Inspired by the growing ecosystem of AI-powered document processing tools

---

**Note:** Make sure to handle sensitive documents appropriately and be aware of the data you're processing through the application.
