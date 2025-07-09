import streamlit as st
from langchain.memory import ConversationBufferMemory
from utils1 import get_chat_response

# 页面设置
st.set_page_config(
    page_title="AI聊天助手",
    page_icon="🗣️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
    <style>
        /* 主标题样式 */
        .main-title {
            color: #1E3A8A;
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }

        /* 副标题样式 */
        .subtitle {
            color: #64748B;
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            font-weight: 400;
        }

        /* 侧边栏样式 */
        .sidebar .sidebar-content {
            background: linear-gradient(180deg, #F8FAFC 0%, #EFF6FF 100%);
            border-right: 1px solid #E2E8F0;
        }

        /* 聊天消息样式 */
        .stChatMessage {
            border-radius: 12px;
            padding: 12px 16px;
            margin: 8px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        /* 用户消息样式 */
        [data-testid="stChatMessage"] [data-testid="chatAvatarIcon-human"] {
            background-color: #2563EB !important;
        }

        /* AI消息样式 */
        [data-testid="stChatMessage"] [data-testid="chatAvatarIcon-ai"] {
            background-color: #10B981 !important;
        }

        /* 按钮样式 */
        .stButton>button {
            background-color: #2563EB;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1rem;
            border: none;
            width: 100%;
            transition: all 0.3s;
        }

        .stButton>button:hover {
            background-color: #1D4ED8;
            color: white;
            transform: translateY(-1px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        /* 链接样式 */
        a {
            color: #2563EB !important;
            text-decoration: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# 主标题和副标题
st.markdown("<h1 class='main-title'>🗣️ AI聊天助手</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>智能对话 · 高效助手 · 随问随答</p>", unsafe_allow_html=True)
st.divider()

# 侧边栏内容
with st.sidebar:
    st.markdown("### 🕒 历史记录")
    clear_page = st.button("🔄️ 开始新的对话")
    if clear_page:
        st.session_state["memory1"] = ConversationBufferMemory(return_messages=True)
        st.session_state["messages"] = [{"role": "ai",
                                         "content": "您好，我是WZ12-2油田AI助手，有什么可以帮您的吗？"}]
        st.rerun()
    st.divider()

    st.markdown("### 🔧 技术支持")
    st.markdown("""
    - 🔑 [获取DeepSeek API key](https://platform.deepseek.com/)
    - 🗝️ [获取OpenAI API key](https://api.aigc369.com/register?aff=8Xgg)
    - 📧 **技术支持邮箱**: fengchh6@cnooc.com.cn
    """)
    st.divider()

    st.markdown("### ℹ️ 系统信息")
    st.markdown("""
    - **版本**: v1.0.2
    - **更新日期**: 2025-07-10
    - **开发团队**: 涠洲12-2油田仪表部门
    """)

# 初始化对话历史
if "memory1" not in st.session_state:
    st.session_state["memory1"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "您好，我是WZ12-2油田AI助手，有什么可以帮您的吗？"}]

# 显示历史消息
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 用户输入
question = st.chat_input("请输入您的问题...")

if question:
    # 显示用户消息
    with st.chat_message("human"):
        st.write(question)
    st.session_state["messages"].append({"role": "human", "content": question})

    # 获取AI回复
    with st.spinner("⏳ AI正在思考中，请稍等..."):
        response = get_chat_response(question, st.session_state["memory1"])

    # 显示AI回复
    with st.chat_message("ai"):
        st.write(response)
    st.session_state["messages"].append({"role": "ai", "content": response})