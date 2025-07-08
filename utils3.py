from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def generate_script(subject):
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """你是一位中海油海上采油平台的工程师。根据以下问题和相关信息，对该问题进行解答。
             问题：{subject}。
             要求回答基于海上石油工程行业。
             回答格式首先为简要概述，之后分成多个小标题，并对每个小标题进行详细描述，最后对所有内容进行总结，之后可以列举相关问题。
             对相关资料来源，可在回答结束时附上所有参考网站首页链接或引用论文。""")
        ]
    )

    model = ChatOpenAI(model="deepseek-chat",
                       openai_api_key="sk-9c68954ad73c4186bf05c1aac5758c7a",
                       openai_api_base="https://api.deepseek.com/v1")

    script_chain = script_template | model

    script = script_chain.invoke({"subject": subject}).content

    print(script)

    return subject, script