import streamlit as st

from langchain.memory import ConversationBufferMemory
from utils2 import qa_agent


st.title("📑 PDF问答工具")
st.divider()

with st.sidebar:
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

if "memory2" not in st.session_state:
    st.session_state["memory2"] = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )

uploaded_file = st.file_uploader("上传你的PDF文件：", type="pdf")
question = st.chat_input("你有什么想了解的", disabled=not uploaded_file)

if uploaded_file and question:
    with st.spinner("AI正在思考中，请稍等..."):
        response = qa_agent(st.session_state["memory2"],
                            uploaded_file, question)
    st.write("### 答案")
    st.write(response["answer"])
    st.session_state["chat_history"] = response["chat_history"]

if "chat_history" in st.session_state:
    with st.expander("历史消息"):
        for i in range(0, len(st.session_state["chat_history"]), 2):
            human_message = st.session_state["chat_history"][i]
            ai_message = st.session_state["chat_history"][i+1]
            st.write(human_message.content)
            st.write(ai_message.content)
            if i < len(st.session_state["chat_history"]) - 2:
                st.divider()
