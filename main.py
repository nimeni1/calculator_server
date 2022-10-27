from fastapi import FastAPI, WebSocket

from services import Parser

# from fastapi.responses import HTMLResponse

app = FastAPI()
parser = Parser()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}


@app.websocket_route("/ws")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()


@app.websocket_route("/evaluate")
async def websocket(websocket: WebSocket):
    await websocket.accept()
    expression = await websocket.receive_text()
    parser.set_expression(expression)
    parser.check_expression()
    result = parser.evaluate_expression()
    await websocket.send_json({"result": f"{result}"})
    await websocket.close()
