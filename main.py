import logging

from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates

import services
from models import RequestModel, ResponseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": id, "data": []})


@app.post('/api/v1/summary', response_model=ResponseModel)
async def summary(data: RequestModel):
    try:
        result = services.summary(data.text, data.sentence_count)
        return ResponseModel(data=result)
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=400, detail='Не удалось получить саммари!')
