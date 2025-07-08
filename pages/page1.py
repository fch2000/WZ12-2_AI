import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils1 import get_chat_response

st.set_page_config(
    page_title="WZ12-2油田AI助手",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        /* 副标题样式 */
        .subtitle {
            color: #64748b;
            text-align: center;
            font-size: 1rem;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>☁️ AI聊天助手</h1>", unsafe_allow_html=True)  # 居中标题
st.markdown("<p class='subtitle'>为您提供专业的技术咨询与支持</p>", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    clearpage = st.button("➕ 开始新对话")
    if clearpage:
        st.session_state["memory1"] = ConversationBufferMemory(return_messages=True)
        st.session_state["messages"] = [{"role": "ai",
                                         "content": "您好，我是WZ12-2油田AI助手，有什么可以帮您的吗？"}]
    st.divider()
    st.markdown("### 帮助与支持")
    st.markdown("🔑 [获取DeepSeek API key](https://platform.deepseek.com/)")
    st.markdown("📧 联系我们: fengchh6@cnooc.com.cn")
    st.divider()
    st.markdown("ℹ️ **版本**: v1.0.0")

if "memory1" not in st.session_state:
    st.session_state["memory1"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "您好，我是WZ12-2油田AI助手，有什么可以帮您的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])  #展示历史对话

prompt = st.chat_input("请输入您的问题...")  #对话框

if prompt:
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)  #将输入内容展示到历史对话

    with st.spinner("AI正在思考中，请稍等..."):  #等待AI回应
        response = get_chat_response(prompt, st.session_state["memory1"])

    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)