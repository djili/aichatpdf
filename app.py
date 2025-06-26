import streamlit as st

def main():
    st.set_page_config(page_title="Rag with PDF", page_icon=":books:")
    st.title("Discutez avec votre PDF")
    st.text_input("input")
    with st.sidebar:
        st.subheader("subheader")
        st.file_uploader("file uploader")
        st.button("button")

if __name__ == "__main__":
    main()