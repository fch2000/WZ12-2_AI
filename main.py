import streamlit as st

page0 = st.Page("pages/page0.py", title="🌊 WZ12-2油田AI助手")
page1 = st.Page("pages/page1.py", title="☁️ AI聊天助手")
page2 = st.Page("pages/page2.py", title="📑 PDF问答工具")
page3 = st.Page("pages/page3.py", title="❓ AI搜索助手")

pg = st.navigation([page0, page1, page2, page3])
pg.run()