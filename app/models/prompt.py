from pydantic import BaseModel

class UserPrompt(BaseModel):
    system_msg: str | None = None
    prompt_msg: str

class ResponsePrompt(BaseModel):
    content: str