import streamlit as st

st.set_page_config(
    page_title="WZ12-2油田AI助手",
    page_icon="🌊",
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

        /* 卡片样式 */
        .feature-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border: 1px solid #E2E8F0;
        }

        /* 功能标题 */
        .feature-title {
            color: #1E40AF;
            font-size: 1.3rem;
            margin-bottom: 0.8rem;
            font-weight: 600;
        }

        /* 页脚样式 */
        .footer {
            text-align: center;
            margin-top: 3rem;
            padding: 1.5rem;
            color: #64748B;
            font-size: 0.9rem;
            border-top: 1px solid #E2E8F0;
        }

        /* 链接样式 */
        a {
            color: #2563EB !important;
            text-decoration: none !important;
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
    </style>
""", unsafe_allow_html=True)

# 主标题和副标题
st.markdown("<h1 class='main-title'>🌊 WZ12-2油田AI助手</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>智能技术赋能海上油田开发 | 专业咨询与决策支持</p>", unsafe_allow_html=True)
st.divider()

# 侧边栏内容
with st.sidebar:
    st.markdown("### 🚀 快速开始")
    if st.button("开始新对话"):
        st.switch_page("pages/page1.py")
    if st.button("上传新文档"):
        st.switch_page("pages/page2.py")
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


# 功能卡片展示
col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("##### 🗣️ AI聊天助手")
        st.markdown("与智能助手对话，获取油田技术专业建议")
        if st.button("开始聊天"):
            st.switch_page("pages/page1.py")

with col2:
    with st.container(border=True):
        st.markdown("##### 📑 文档智能问答")
        st.markdown("上传技术文档，快速获取关键信息")
        if st.button("上传文档"):
            st.switch_page("pages/page2.py")

with col3:
    with st.container(border=True):
        st.markdown("##### 🔍 专业搜索工具")
        st.markdown("对油田技术问题提问，实现规范化知识检索")
        if st.button("开始搜索"):
            st.switch_page("pages/page3.py")
st.divider()

# 功能介绍
with st.expander("📌 详细功能介绍"):
    st.markdown("""
    <div class="feature-card">
        <h3 class="feature-title">🗣️ AI聊天助手</h3>
        <p>基于DeepSeek大模型构建的专业对话系统，可回答油田开发、生产管理、设备维护等各类技术问题。</p>
        <ul>
            <li>支持多轮对话上下文理解</li>
            <li>提供专业术语解释</li>
            <li>生成技术报告草稿</li>
        </ul>
    </div>

    <div class="feature-card">
        <h3 class="feature-title">📑 文档智能问答</h3>
        <p>基于RAG技术，对上传的PDF技术文档进行智能解析和问答。</p>
        <ul>
            <li>单独支持PDF文档格式</li>
            <li>快速提取关键数据和技术参数</li>
            <li>生成文档摘要</li>
        </ul>
    </div>

    <div class="feature-card">
        <h3 class="feature-title">🔍 专业搜索工具</h3>
        <p>专为石油工业设计的智能搜索引擎，内置行业相关提示模板实现规范化搜索。</p>
        <ul>
            <li>规范化技术术语检索</li>
            <li>关联技术标准查询</li>
            <li>参考来源标注</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# 页脚
st.markdown("""
<div class="footer">
    <p>© 2025 中海石油涠洲12-2油田仪表部门 | 智湛未来，AI涠油</p>
    <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 0.5rem;">
        <a href="https://www.cnooc.com.cn/" target="_blank">中国海油官网</a>
        <span>|</span>
        <a href="https://github.com/fch2000/WZ12-2_AI" target="_blank">项目源码</a>
        <span>|</span>
        <a href="https://github.com/fch2000/WZ12-2_AI/blob/main/README.md" target="_blank">使用手册</a>
    </div>
</div>
""", unsafe_allow_html=True)