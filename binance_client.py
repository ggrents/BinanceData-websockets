import json
import websockets
import asyncio
import time


class BinanceClient:
    def __init__(self, symbol):
        self.url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"
        self.xdata = []
        self.ydata = []

    async def connect(self):
        self.websocket = await websockets.connect(self.url)

    async def get_data(self):
        raw_data = await self.websocket.recv()
        data = json.loads(raw_data)
        if 'data' in data:
            trade_data = data['data']
            event_time = time.localtime(trade_data['E'] // 1000)
            event_time = f"{event_time.tm_hour}:{event_time.tm_min}:{event_time.tm_sec}"
            print(event_time, trade_data['c'])
            self.xdata.append(event_time)
            self.ydata.append(float(trade_data['c']))
        return self.xdata, self.ydata

    def close(self):
        self.websocket.close()
