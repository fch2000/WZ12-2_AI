import streamlit as st
from utils3 import generate_script

st.set_page_config(
    page_title="AI搜索助手",
    page_icon="🔍",
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
st.markdown("<h1 class='main-title'>🔍 AI搜索助手</h1>", unsafe_allow_html=True)  # 居中标题
st.markdown("<p class='subtitle'>专业知识 · 丰富信源 · 整合搜索</p>", unsafe_allow_html=True)
st.divider()

# 侧边栏内容
with st.sidebar:
    st.markdown("### 🕒 历史记录")
    clear_page = st.button("🔄️ 开始新的提问")
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

# 用户输入
subject = st.chat_input("请输入您的问题...")

# 获取AI回复
if subject:
    with st.spinner("⏳ AI正在思考中，请稍等..."):
        title, script = generate_script(subject)
    st.success("✅ 解答已生成！")
    st.subheader("📝 解答：")
    st.write(script)