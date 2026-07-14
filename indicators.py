import pandas as pd


def get_trend(df):

    ema = df["close"].ewm(span=50).mean()

    if df["close"].iloc[-1] > ema.iloc[-1]:
        return "Bullish"

    else:
        return "Bearish"



def volume_strength(df):

    current = df["volume"].iloc[-1]

    average = df["volume"].mean()

    return current / average



def fvg_size(df):

    size = abs(
        df["low"].iloc[-1] -
        df["high"].iloc[-3]
    )

    price = df["close"].iloc[-1]

    return (size / price) * 100
