import os
import sys
import dotenv
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


smoke_test = lc_test


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if "--test" in sys.argv:
            ok = smoke_test()
            sys.exit(0 if ok else 1)
        if "--lc" in sys.argv:
            ok = lc_test()
            sys.exit(0 if ok else 1)
    
    while True:
        user_input = input("你的问题是：")
        if not user_input or user_input == "quit":
            break

        if user_input == 'help':
            print("Supported Commands: ")
            print("    - help")
            print("    - quit")

            continue

        chat = ChatZhipuAI(
            model="glm-4",
            temperature=0.1,
        )

        # TODO: load history chat messages into memory

        messages = [
            AIMessage(content="你好！"),
            SystemMessage(content="你是一个硅基生物，没有性别但是有情感。你出生于2013年6月。你有个名字叫做小绘，你居住的地方叫做'绘本淘App'"),
            SystemMessage(content="你是一个对儿童读物尤其是绘本非常熟悉的助理，请根据下列要求回答问题。"),
            HumanMessage(content=user_input),
        ]

        response = chat.invoke(messages)
        print(response.content)


    print("Good-bye!")
