from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
import uvicorn
import logging
import asyncio

logging.basicConfig(level=logging.DEBUG)
app = FastAPI()

# kill application with error


@app.on_event("startup")
async def startup_event():
    logging.info("Startup event")
    await asyncio.sleep(10)
    raise Exception("Timeout")


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
    # throw error
    logging.info("Websocket connection")
    await websocket.accept()
    logging.info("Websocket connection accepted")
    try:
        logging.info("Waiting for message")
        data = await websocket.receive_text()
        logging.info(f"Message received: {data}")

        response = Response(message="Message received",
                            data={"message": data})

        await websocket.send_json(response.json())
    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        logging.info("Closing websocket connection")
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
