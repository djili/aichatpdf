import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain, create_history_aware_retriever
from langchain.memory import ChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import OpenAIEmbeddings, ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from ui import css, bot_template, user_template


def main():
    load_dotenv()
    st.write(css, unsafe_allow_html=True)

    # Initialize session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.set_page_config(page_title="Rag with PDF", page_icon=":books:")
    st.title("Discutez avec votre PDF")
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if user_question := st.chat_input("Posez une question sur vos documents :"):
        handle_userinput(user_question)
    
    with st.sidebar:
        st.subheader("Vos documents")
        pdf_file = st.file_uploader("Upload vos documents ici et cliquer sur explorer", 
                                 accept_multiple_files=True, 
                                 type=["pdf"])
        if st.button("Explorer"):
            with st.spinner("Chargement des documents..."):
                # Get pdf text
                text = getTextFromPDF(pdf_file)
                # Get the text chunks
                chunks = getChunkFromText(text)
                # Create vector store
                vector_store = getVectorStore(chunks)
                # Create conversation chain
                st.session_state.conversation = getConversation(vector_store)
                st.success("Documents chargés avec succès ! Posez vos questions.")

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
    embedding = HuggingFaceEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embedding)
    return vectorstore

def getConversation(vector_store):
    llm = ChatOpenAI()
    
    # Create a retriever
    retriever = vector_store.as_retriever()
    
    # Create a prompt that includes the chat history
    contextualize_q_system_prompt = """Given a chat history and the latest user question \
    which might reference context in the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."""
    
    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    
    # Create the history-aware retriever
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )
    
    # Create the QA prompt
    qa_system_prompt = """You are an assistant for question-answering tasks. \
    Use the following pieces of retrieved context to answer the question. \
    If you don't know the answer, just say that you don't know. \
    Use three sentences maximum and keep the answer concise.\n\n
    {context}"""
    
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    
    # Create the question answering chain
    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    
    # Create the final retrieval chain
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    
    return rag_chain


def handle_userinput(user_question):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_question})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_question)
    
    # Get response from the conversation chain
    if st.session_state.conversation is not None:
        response = st.session_state.conversation.invoke({
            "input": user_question,
            "chat_history": st.session_state.messages
        })
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response["answer"])
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response["answer"]})
    else:
        with st.chat_message("assistant"):
            st.warning("Veuillez d'abord charger des documents PDF.")

L
if __name__ == "__main__":
    main()