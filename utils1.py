from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI


def get_chat_response(prompt, memory):
    model = ChatOpenAI(model="gpt-3.5-turbo",
                       openai_api_key="sk-CduDoQyNF5Ml0XKVDA6A2ZVHgsmLRje5GIY44xVYPb6nYGd0",
                       openai_api_base="https://api.aigc369.com/v1")

    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]
