import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils2 import qa_agent

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

st.markdown("<h1 style='text-align: center;'>📑 PDF问答工具</h1>", unsafe_allow_html=True)  # 居中标题
st.markdown("<p class='subtitle'>为您提供专业的技术咨询与支持</p>", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown("### 帮助与支持")
    st.markdown("🔑 [获取DeepSeek API key](https://platform.deepseek.com/)")
    st.markdown("📧 联系我们: fengchh6@cnooc.com.cn")
    st.divider()
    st.markdown("ℹ️ **版本**: v1.0.0")

if "memory2" not in st.session_state:
    st.session_state["memory2"] = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history",
        output_key="answer"
    )

uploaded_file = st.file_uploader("上传你的PDF文件：", type="pdf")
question = st.chat_input("请输入您的问题...", disabled=not uploaded_file)

if uploaded_file and question:
    with st.spinner("AI正在思考中，请稍等..."):
        response = qa_agent(st.session_state["memory2"],
                            uploaded_file, question)
    st.subheader("📝 解答：")
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
