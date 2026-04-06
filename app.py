import streamlit as st
from dotenv import load_dotenv
import os
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings,ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def get_pdf_text(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text
def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks  =  splitter.split_text(text)
    return chunks
def get_vector_store(chunks):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview",
        )
    vector_store= Chroma.from_texts(chunks, embedding=embeddings,persist_directory="./chroma_db")
    vector_store.persist()
    return vector_store
def get_qa_chain(vector_store):
    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.3)
    
    prompt_template = """
    Answer the question based on the PDF context below.
    If the answer is not found in the context,"I could find in this PDF."
    Context: {context}
    Question: {question}

    Answer:
    """
    prompt =PromptTemplate(
        input_variables=["context","question"],
        template=prompt_template
    )
    chain= RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(
            search_kwargs={"k":4}
        ),
        chain_type_kwargs={"prompt":prompt}
    )
    return chain
def main():
    st.set_page_config(page_title="Chat with PDF using Gemini API", page_icon=":books:")
    st.title("Chat with PDF using Gemini API")
    st.write("Upload a PDF file and ask questions about it!")

    uploaded_file=st.file_uploader("Choose a PDF file",type="pdf")
    if uploaded_file is not None:
        with st.spinner("Processing PDF..."):
            raw_text = get_pdf_text(uploaded_file)
            text_chunks= get_text_chunks(raw_text)
            vector_store = get_vector_store(text_chunks)
            st.session_state.qa_chain = get_qa_chain(vector_store)
        st.success("PDF processed successfully! Ask me anything about the PDF.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if question :=st.chat_input("Ask a question about the PDF..."):
        st.session_state.messages.append({"role":"user","content":question})
      
        with st.chat_message("user"):
            st.write(question)

        if "qa_chain" in st.session_state:
            with st.chat_message("assistant"):
                with st.spinner("Generating answer..."):
                    response = st.session_state.qa_chain.run(question)
                    st.write(response)

            st.session_state.messages.append({"role":"assistant","content":response})

        else:
            st.warning("Please upload a PDF First!")
if __name__ == "__main__":
    main()