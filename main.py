from fastapi import FastAPI, status, Response, Header, Request, WebSocket
from fastapi.responses import HTMLResponse
from typing import Optional, List
from db import models
from db.database import engine
from chat_html import html
from router import blog, chat

import pydantic

models.Base.metadata.create_all(engine)

app = FastAPI()

# app.include_router(chat.router)
app.include_router(blog.router)


@app.get("/")
async def get():
    return HTMLResponse(html)

clients = []


@app.websocket("/chat")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    clients.append(ws)
    print(clients)
    while True:
        data = await ws.receive_text()
        for client in clients:
            await client.send_text(data)
