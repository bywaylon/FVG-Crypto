from binance.client import Client
import pandas as pd

client = Client()


def get_candles(symbol, interval="1h"):

    candles = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=100
    )

    df = pd.DataFrame(
        candles,
        columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "x1",
            "x2",
            "x3",
            "x4",
            "x5",
            "x6"
        ]
    )

    df["high"] = df["high"].astype(float)
    df["low"] = df["low"].astype(float)
    df["close"] = df["close"].astype(float)

    return df


def check_fvg(symbol):

    df = get_candles(symbol)

    last = df.iloc[-1]
    two_back = df.iloc[-3]


    # Bullish FVG
    if last["low"] > two_back["high"]:
        return {
            "coin": symbol.replace("USDT",""),
            "type": "Bullish FVG"
        }


    # Bearish FVG
    if last["high"] < two_back["low"]:
        return {
            "coin": symbol.replace("USDT",""),
            "type": "Bearish FVG"
        }


    return None
