from fastapi import FastAPI, WebSocket

from services import Parser


app = FastAPI()
parser = Parser()


@app.get("/")
async def read_main():
    """Standard fastapi RESTapi endpoint, used for testing the connection from a client to the server."""
    return {"msg": "Hello World"}


@app.websocket_route("/ws")
async def websocket_connect(websocket: WebSocket):
    """Websocket route used for testing connection from a client to the server."""
    await websocket.accept()
    await websocket.send_json({"msg": "Hello WebSocket"})
    await websocket.close()


@app.websocket_route("/evaluate")
async def websocket_evaluate(websocket: WebSocket):
    """"Websocker route used for evaluating the client input mathematical expression
     and computing a result for it."""
    await websocket.accept()
    expression = await websocket.receive_text()
    parser.set_expression(expression)
    parser.check_expression()
    result = parser.evaluate_expression()
    await websocket.send_json({"result": f"{result}"})
    await websocket.close()
