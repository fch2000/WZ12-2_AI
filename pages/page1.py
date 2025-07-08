import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils1 import get_chat_response

st.title("☁️ WZ12-2 AI聊天助手")
st.divider()

with st.sidebar:
    clearpage = st.button("新对话")
    if clearpage:
        st.session_state["memory1"] = ConversationBufferMemory(return_messages=True)
        st.session_state["messages"] = [{"role": "ai",
                                         "content": "你好，我是WZ12-2油田AI助手，有什么可以帮你的吗？"}]
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

if "memory1" not in st.session_state:
    st.session_state["memory1"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是WZ12-2油田AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])  #展示历史对话

prompt = st.chat_input("给AI发送消息")  #对话框

if prompt:
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)  #将输入内容展示到历史对话

    with st.spinner("AI正在思考中，请稍等..."):  #等待AI回应
        response = get_chat_response(prompt, st.session_state["memory1"])

    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)