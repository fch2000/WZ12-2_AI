import streamlit as st

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

st.markdown("<h1 style='text-align: center;'>🌊 WZ12-2油田AI助手</h1>", unsafe_allow_html=True)  # 居中标题
st.markdown("<p class='subtitle'>为您提供专业的技术咨询与支持</p>", unsafe_allow_html=True)
st.divider()

with st.sidebar:
    st.markdown("### 帮助与支持")
    st.markdown("🔑 [获取DeepSeek API key](https://platform.deepseek.com/)")
    st.markdown("🗝️ [获取OpenAI API key](https://api.aigc369.com/register?aff=8Xgg)")
    st.markdown("📧 联系我们: fengchh6@cnooc.com.cn")
    st.divider()
    st.markdown("ℹ️ **版本**: v1.0.0")

# 功能介绍
with st.expander("ℹ️ 系统功能介绍", expanded=False):
    st.markdown("""
    ### 🌟 主要功能
    - **🖥️ AI聊天助手**: 克隆DeepSeek实现AI对话
    - **📚 智能PDF问答工具**: 基于RAG实现PDF文件问答
    - **💬 AI搜索工具**: 通过石油工业相关提示模板实现规范化搜索

    ### 💡 使用技巧
    - 使用侧边栏切换不同功能，获取API KEY和联系作者
    - AI聊天助手：与AI进行对话，通过侧边栏“开始新的对话”按钮创建新对话
    - 智能PDF问答工具：上传PDF文件后，对文件内容提问，通过下拉框回顾历史问题，通过侧边栏“开始新的提问”按钮刷新回答
    - AI搜索工具：对与石油工业或技术相关问题搜索，文末可查看参考链接
    """)

st.markdown("""
<div style="
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    margin-top: 2rem;
    border: 1px solid #e0e0e0;
">
    <h4 style="color: #8B4513; margin-bottom: 1rem;">🌊 WZ12-2油田AI助手</h4>
    <p style="color: #666; margin-bottom: 1rem;">
        基于 <strong>DeepSeek API</strong> 构建 | 采用 <strong>RAG技术</strong> | 使用 <strong>Streamlit</strong> 开发
    </p>
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <span style="color: #555;">🔗 <a href="https://platform.deepseek.com/" target="_blank" style="color: #8B4513; text-decoration: none;">DeepSeek平台</a></span>
        <span style="color: #555;">📖 <a href="https://streamlit.io/" target="_blank" style="color: #8B4513; text-decoration: none;">Streamlit官网</a></span>
        <span style="color: #555;">💻 <a href="https://github.com/fch2000/WZ12-2_AI" target="_blank" style="color: #8B4513; text-decoration: none;">GitHub源码</a></span>
    </div>
    <br>
    <p style="color: #888; font-size: 1.0rem; margin-top: 1rem;">
        智湛未来，AI涠油
    </p>
</div>
""", unsafe_allow_html=True)