from pydantic import BaseModel


class RequestModel(BaseModel):
    text: str
    sentence_count: int = 2


class ResponseModel(BaseModel):
    data: list[str] = []
