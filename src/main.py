from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import uvicorn
import logging
import asyncio
import dotenv

dotenv.load_dotenv()

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()


class Response(BaseModel):
    message: str
    user: str


class Request(BaseModel):
    message: str
    user: str


@app.get("/", response_model=Response)
async def get(
    data: str = None,
):
    return Response(message="Message received", user=data)


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
):
    await websocket.accept()
    try:
        data = await websocket.receive_text()

        response = Response(message="Message received",
                            data={"message": data})

        await websocket.send_json(response)
    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        logging.info("Closing websocket connection")
        await websocket.close()
