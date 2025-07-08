import streamlit as st

page1 = st.Page("pages/page1.py", title="☁️ WZ12-2 AI聊天助手")
page2 = st.Page("pages/page2.py", title="📑 PDF问答工具")
page3 = st.Page("pages/page3.py", title="❓ STEP问题解答")

pg = st.navigation([page1, page2, page3])
pg.run()