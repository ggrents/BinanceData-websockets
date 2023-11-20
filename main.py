import asyncio
from binance_client import BinanceClient
from plotter import Plotter


async def main():
    symbol = input("Enter Binance symbol (e.g., BTCUSDT): ")

    binance_client = BinanceClient(symbol)
    plotter = Plotter(symbol)

    await binance_client.connect()

    try:
        while True:
            await binance_client.get_data()
            plotter.update_graph(binance_client.xdata, binance_client.ydata)
    except KeyboardInterrupt:
        pass
    finally:
        await binance_client.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())