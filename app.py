import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def main():
    load_dotenv()
    st.set_page_config(page_title="Rag with PDF", page_icon=":books:")
    st.title("Discutez avec votre PDF")
    st.text_input("Posez une question sur vos documents :")
    with st.sidebar:
        st.subheader("Vos documents")
        pdf_file = st.file_uploader("Upload vos dociments ici et cliquer sur explorer", accept_multiple_files=True, type=["pdf"])
        if st.button("Explorer"):
            with st.spinner("Chargement des documents..."):
                text = getTextFromPDF(pdf_file)
                chunks = getChunkFromText(text)
                st.write(chunks)

def getTextFromPDF(pdf_file):
    text =  ""
    for pdf in pdf_file:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def getChunkFromText(text):
    text_plitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_plitter.split_text(text)
    return chunks

if __name__ == "__main__":
    main()