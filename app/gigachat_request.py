from langchain_community.chat_models import GigaChat
from langchain_core.messages import HumanMessage, SystemMessage

import os

os.environ["GIGACHAT_CREDENTIALS"] = "NzJlNTU0NTItZWM2Yy00N2E0LTg5ZGQtYmRlNjYxMDIxNDQxOjFlYzhmYTEwLTU3MzYtNDkxZS05MjA0LWQwZmY0NTZjYjk3Mw=="

chat = GigaChat(verify_ssl_certs=False, scope="GIGACHAT_API_PERS")

def ask_gigachat(system_msg: str, prompt_msg: str) -> str:
    messages = [
        SystemMessage(
            content=system_msg
        ),
        HumanMessage(
            content=prompt_msg
        ),
    ]
    return chat.invoke(messages).content

