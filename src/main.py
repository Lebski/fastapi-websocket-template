from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Response(BaseModel):
    message: str
    data: dict


@app.get("/", response_model=Response)
async def get(
    data: str = None,
):
    return Response(message="Message received", data={"message": data})


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        response = Response(message="Message received", data={"message": data})

        await websocket.send_json(response.json())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
