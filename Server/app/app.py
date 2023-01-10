from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import statistics
from .nbp_enums import TableName, Period
from .nbp_client import NBPClient

app = FastAPI()

origins = ["http://localhost:8000", "http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"],
                   allow_headers=["*"])


@app.get("/")
async def home():
    return {"hello": "world"}


@app.get("/currencies/{table_name}")
def get_table_currencies(table_name: TableName):
    nbp_client = NBPClient()
    tables_names = [table_name.value.lower() for member in TableName]
    if table_name.value.lower() in tables_names:
        if table_name.value.lower() != TableName.A.value.lower():
            raise HTTPException(status_code=403, detail=f"Tables B and C are not available for that request!")
        response = nbp_client.get_all_currencies_for_table(table_name.value)
        if response is not None:
            return response
    raise HTTPException(status_code=404, detail=f"Currencies of table {table_name} not found (check correctness of "
                                                "the parameter).")


@app.get("/currencies/{table_name}/{code}/{period}")
def get_single_currency_rates(table_name: TableName, code: str, period: Period):
    response = get_response_for_currency(table_name, code, period)
    if get_response_for_currency(table_name, code, period) is not None:
        return response
    raise HTTPException(status_code=404, detail=f"Error, rates not found for period '{period}' and table "
                                                f"'{table_name.value}' with currency code '{code}'")

@app.get("/math_ops/{table_name}/{code}/{period}")  # mediana
def get_single_currency_rates_math_ops(table_name: TableName, code: str, period: Period):
    response = get_response_for_currency(table_name, code, period)
    if get_response_for_currency(table_name, code, period) is not None:
        rates = [element.get("rate") for element in response]
        rounded_rates = [round(element, 2) for element in rates]
        mean = statistics.mean(rates)
        st_deviation = statistics.stdev(rates)
        mode = statistics.mode(rounded_rates)
        rates.sort()
        median = statistics.median(rates)
        return {"median": median,
                "standard_deviation": st_deviation,
                "mode": mode,
                "cv": (st_deviation/mean)*100}
    raise HTTPException(status_code=404, detail=f"Error, rates not found for period '{period}' and table "
                                                f"'{table_name.value}' with currency code '{code}'")


def get_response_for_currency(table_name: TableName, code: str, period: Period):
    tables_names = [table_name.value.lower() for member in TableName]
    if table_name.value.lower() in tables_names:
        if table_name.value.lower() != TableName.A.value.lower():
            raise HTTPException(status_code=403, detail=f"Tables B and C are not available for that request!")
        periods_enum_values = [member.lower() for member in Period]
        if period.value.lower() not in periods_enum_values:
            period = None
        nbp_client = NBPClient()
        response = nbp_client.get_single_currency_data(table_name.value, code, period)
        return response


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
