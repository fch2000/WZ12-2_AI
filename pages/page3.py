import streamlit as st
from utils3 import generate_script

st.set_page_config(
    page_title="AI搜索助手",
    page_icon="❓",
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

st.markdown("<h1 style='text-align: center;'>❓ AI搜索助手</h1>", unsafe_allow_html=True)  # 居中标题
st.markdown("<p class='subtitle'>为您提供专业的技术咨询与支持</p>", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown("### 帮助与支持")
    st.markdown("🔑 [获取DeepSeek API key](https://platform.deepseek.com/)")
    st.markdown("🗝️ [获取OpenAI API key](https://api.aigc369.com/register?aff=8Xgg)")
    st.markdown("📧 联系我们: fengchh6@cnooc.com.cn")
    st.divider()
    st.markdown("ℹ️ **版本**: v1.0.0")

subject = st.chat_input("请输入您的问题...")

if subject:
    with st.spinner("AI正在思考中，请稍等..."):
        title, script = generate_script(subject)
    st.success("解答已生成！")
    st.subheader("📝 解答：")
    st.write(script)