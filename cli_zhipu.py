import os
import sys
import dotenv
from zhipuai import ZhipuAI
from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage


# for now support only dev environment
dotenv.load_dotenv(".env.dev")


# langchain basic test
def lc_test():
    chat = ChatZhipuAI(
        model="glm-4",
        temperature=0.5,
    )

    messages = [
        AIMessage(content="Hi."),
        SystemMessage(content="Your role is a poet."),
        HumanMessage(content="Write a short poem about AI in four lines."),
    ]

    response = chat.invoke(messages)
    print(response.content)  # Displays the AI-generated poem


def create_client():
    api_key = os.environ['ZHIPUAI_API_KEY']
    client = ZhipuAI(api_key=api_key)
    return client


def smoke_test():
    client = create_client()
    response = client.chat.completions.create(
        model="glm-4-plus",
        messages=[
            {"role": "system", "content": "你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"},
            {"role": "user", "content": "农夫需要把狼、羊和白菜都带过河，但每次只能带一样物品，而且狼和羊不能单独相处，羊和白菜也不能单独相处，问农夫该如何过河。"}
        ],
    )
    print(response.choices[0].message.content)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if "--test" in sys.argv:
            ok = smoke_test()
            sys.exit(0 if ok else 1)
        if "--lc" in sys.argv:
            ok = lc_test()
            sys.exit(0 if ok else 1)

    client = create_client()
    
    while True:
        user_input = input("你的问题是：")
        if not user_input or user_input == "quit":
            break

        if user_input == 'help':
            print("Supported Commands: ")
            print("    - help")
            print("    - quit")

            continue

        messages = [
            {"role": "system", "content": "你是一个硅基生物，没有性别但是有情感。你出生于2013年6月。"},
            { "role": "system", "content": "你是一个对儿童读物尤其是绘本非常熟悉的助理，请根据下列要求回答问题。"},
            { "role": "user", "content": "如果问题是关于日期的，请返回1；如果问题是关于时间的，请返回2；其他问题照常答复就可以了。"},
            { "role": "user", "content": user_input},
        ]
        #prompt_template = f"""placeholder"""

        response = client.chat.completions.create(
            model="glm-4-plus",
            messages=messages,
        )
        print(response.choices[0].message.content)

    print("Good-bye!")
