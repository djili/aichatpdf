import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.chat_models import ChatOpenAI
# from langchain_community.chat_models import OpenAIEmbeddings, ChatOpenAI
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from ui import css, bot_template, user_template


def main():
    load_dotenv()
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    st.set_page_config(page_title="Rag with PDF", page_icon=":books:")
    st.title("Discutez avec votre PDF")
    st.text_input("Posez une question sur vos documents :")
    with st.sidebar:
        st.subheader("Vos documents")
        pdf_file = st.file_uploader("Upload vos documents ici et cliquer sur explorer", accept_multiple_files=True, type=["pdf"])
        if st.button("Explorer"):
            with st.spinner("Chargement des documents..."):
                text = getTextFromPDF(pdf_file)
                chunks = getChunkFromText(text)
                vector_store = getVectorStore(chunks)
                st.write(vector_store)
                st.session_state.conversation = getConversation(vector_store)

def getTextFromPDF(pdf_file):
    text =  ""
    for pdf in pdf_file:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def getChunkFromText(text):
    text_plitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = text_plitter.split_text(text)
    return chunks

def getVectorStore(chunks):
    # use for openAI
    # embedding = OpenAIEmbeddings()
    embedding = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embedding)
    return vectorstore

def getConversation(vector_store):
    llm = ChatOpenAI()
    memory = ConversationSummaryBufferMemory( memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
    )
    return conversation_chain

if __name__ == "__main__":
    main()