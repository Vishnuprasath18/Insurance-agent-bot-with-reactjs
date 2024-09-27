from flask import Flask, request, jsonify
from langchain_community.document_loaders import PyPDFLoader  
from langchain_community.vectorstores import Chroma  
from langchain_community.embeddings import OllamaEmbeddings 
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Load PDF and initialize LangChain components
file_path = "E:\\lang and llama\\data\\sample data.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()

# Create vectorstore using Mistral embeddings
embedding_function = OllamaEmbeddings(model="mistral")
vectorstore = Chroma.from_documents(docs, embedding=embedding_function)

# Retriever and LLM setup
retriever = RunnableLambda(vectorstore.similarity_search).bind(k=7)
llm = ChatOllama(model="mistral")  # Use the Mistral model

message_template = """
Answer this question using the provided context only.
Answer precisely within 3 lines or so,
don't answer with unnecessary answers,
answer only within this PDF,
answer based on the given context shortly,
if the user greets you, greet them back,
always ask a question based on the answer you provided.

{question}

Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([("human", message_template)])
rag_chain = {"context": retriever, "question": RunnablePassthrough()} | prompt | llm

@app.route("/ask", methods=["POST"])
def ask_question():
    request_data = request.get_json()
    question = request_data["question"]
    
    # Invoke the RAG chain with the user's question
    response = rag_chain.invoke(question)
    
    # Return the response as JSON
    return jsonify({"response": response.content})

@app.route("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
