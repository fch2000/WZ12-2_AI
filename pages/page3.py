import streamlit as st
from utils3 import generate_script

st.title("❓ STEP问题解答")
st.divider()

with st.sidebar:
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

subject = st.chat_input("💡 请输入你的问题")

if subject:
    with st.spinner("AI正在思考中，请稍等..."):
        title, script = generate_script(subject)
    st.success("解答已生成！")
    st.subheader("📝 解答：")
    st.write(script)
