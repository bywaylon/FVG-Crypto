from binance.client import Client
import pandas as pd
from indicators import get_trend, volume_strength, fvg_size

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
    df["volume"] = df["volume"].astype(float)

    return df



def check_fvg(symbol):

    df = get_candles(symbol)

    score = 0
    reasons = []

    trend = get_trend(df)
    size = fvg_size(df)
    volume = volume_strength(df)


    # Trend
    if trend == "Bullish":
        score += 25
        reasons.append("Bullish trend")

    else:
        score += 25
        reasons.append("Bearish trend")


    # FVG size
    if size > 0.1:
        score += 25
        reasons.append("Large FVG")


    # Volume
    if volume > 1.3:
        score += 25
        reasons.append("Volume increase")


    # Bullish FVG
    if df["low"].iloc[-1] > df["high"].iloc[-3]:

        score += 25

        return {
            "coin": symbol.replace("USDT", ""),
            "direction": "LONG",
            "score": score,
            "reasons": reasons
        }


    # Bearish FVG
    if df["high"].iloc[-1] < df["low"].iloc[-3]:

        score += 25

        return {
            "coin": symbol.replace("USDT", ""),
            "direction": "SHORT",
            "score": score,
            "reasons": reasons
        }


    return None