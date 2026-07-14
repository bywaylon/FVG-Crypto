from indicators import get_trend, volume_strength, fvg_size


def check_fvg(symbol):

    df = get_candles(symbol)

    score = 0
    reasons = []

    trend = get_trend(df)

    size = fvg_size(df)

    volume = volume_strength(df)


    if trend == "Bullish":
        score += 25
        reasons.append("Bullish trend")

    else:
        score += 25
        reasons.append("Bearish trend")


    if size > 0.1:
        score += 25
        reasons.append("Large FVG")


    if volume > 1.3:
        score += 25
        reasons.append("Volume increase")


    if df["low"].iloc[-1] > df["high"].iloc[-3]:

        score += 25

        return {
            "coin": symbol.replace("USDT",""),
            "direction": "LONG",
            "score": score,
            "reasons": reasons
        }


    if df["high"].iloc[-1] < df["low"].iloc[-3]:

        score += 25

        return {
            "coin": symbol.replace("USDT",""),
            "direction": "SHORT",
            "score": score,
            "reasons": reasons
        }


    return None