import openai
import os

GPT_MODEL = "gpt-3.5-turbo"
openai.api_key = os.getenv("OPENAI_KEY")


def get_response(user_txt: str) -> str:
    messages = []
    content = user_txt
    messages.append(
        {"role": "user", "content": content}
    )

    completion = openai.ChatCompletion.create(model=GPT_MODEL, messages=messages)
    chat_response = completion.choices[0].message.content
    messages.append(
        {"role": "assistant", "content": chat_response}
    )

    return chat_response
