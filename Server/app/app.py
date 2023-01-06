from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
from nbp_enums import TableName, Period
from nbp_client import NBPClient

app = FastAPI()

origins = ["http://localhost:8000", "http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/")
async def home():
    return {"hello": "world"}


@app.get("/currencies/{table_name}")
async def get_table_currencies(table_name: TableName):
    nbp_client = NBPClient()
    table_enum_values = [member.value.lower() for member in TableName]
    if table_name.value.lower() in table_enum_values:
        response = nbp_client.get_all_currencies_for_table(table_name.value)
        if response is not None:
            return response
    raise HTTPException(status_code=404, detail=f"Currencies of table {table_name} not found (check correctness of "
                                                "the parameter).")


@app.websocket("/ws/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except WebSocketDisconnect:
        message = {"message": "Offline, client disconnected"}
        await websocket.send_bytes(json.dumps(message))
