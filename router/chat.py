import asyncio

from fastapi import APIRouter
from fastapi.websockets import WebSocket
from fastapi.responses import HTMLResponse
from chat_html import html

router = APIRouter(
    prefix='/chat',
    tags=['chat']
)


@router.get("/")
async def get():
    return HTMLResponse(html)

clients = []


@router.websocket("/chat")
async def chat(websockets: WebSocket):
    await websockets.accept()
    clients.append(websockets)
    print(clients)
    while True:
        data = await websockets.receive_text()
        for client in clients:
            await client.send_text(data)
