import sys
import dotenv
import qianfan # baidu big model


dotenv.load_dotenv(".env.dev")


def smoke_test():
    chat_comp = qianfan.ChatCompletion()

    # specify the model name
    model_name = "ERNIE-3.5-8K"
    # model_name = "ERNIE-4.0-8K-Latest"
    
    resp = chat_comp.do(model=model_name, messages=[{
        "role": "user",
        "content": "你好"
    }])

    success = resp.status_code == 200
    if not success:
        return False
    
    print(resp["body"])
    return True


if __name__ == '__main__':
    if len(sys.argv) > 1 and "--test" in sys.argv:
        ok = smoke_test()
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

        messages = [
            { "role": "system", "content": "你是一个对儿童读物尤其是绘本非常熟悉的助理，请根据下列要求回答问题。"},
            { "role": "user", "content": user_input},
            { "role": "ai", "content": ""},
        ]
        prompt_template = f"""placeholder"""

    print("Good-bye!")

