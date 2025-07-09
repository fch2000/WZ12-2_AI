from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

def qa_agent(memory, uploaded_file, question):
    model = ChatOpenAI(model="deepseek-chat",
                       openai_api_key="sk-9c68954ad73c4186bf05c1aac5758c7a",
                       openai_api_base="https://api.deepseek.com/v1")

    # 获取桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # 构建完整的文件路径
    temp_file_path = os.path.join(desktop_path, uploaded_file.name)

    # 保存文件
    file_content = uploaded_file.read()
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(file_content)

    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n", "。", "！", "？", "，", "、", ""]
    )  #对文本进行分割


    texts = text_splitter.split_documents(docs)
    embeddings_model = OpenAIEmbeddings(openai_api_key="sk-CduDoQyNF5Ml0XKVDA6A2ZVHgsmLRje5GIY44xVYPb6nYGd0",
                                        openai_api_base="https://api.aigc369.com/v1")
    db = FAISS.from_documents(texts, embeddings_model)
    retriever = db.as_retriever()
    qa = ConversationalRetrievalChain.from_llm(
        llm=model,
        retriever=retriever,
        memory=memory
    )
    response = qa.invoke({"chat_history": memory, "question": question})

    return response
