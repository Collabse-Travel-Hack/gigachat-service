from fastapi import APIRouter
from gigachat_request import ask_gigachat
from models.prompt import *

router = APIRouter(prefix="/gigachat")

@router.post("/ask", status_code = 200)
async def ask(prompt: UserPrompt) -> ResponsePrompt:
    return ResponsePrompt(content = ask_gigachat(prompt.system_msg, prompt.prompt_msg))

@router.post("/sample-task", status_code = 200)
async def sample_task() -> ResponsePrompt:
    system_msg = """
    
    """

    prompt_msg = """


    """
    return ResponsePrompt(
        content = ask_gigachat(
            system_msg,
            prompt_msg
        )
    )