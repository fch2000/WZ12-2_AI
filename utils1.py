from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


def get_chat_response(prompt, memory):
    model = ChatOpenAI(model="deepseek-chat",
                       openai_api_key="sk-9c68954ad73c4186bf05c1aac5758c7a",
                       openai_api_base="https://api.deepseek.com/v1")

    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]
