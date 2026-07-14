from binance.client import Client
import pandas as pd

client = Client()


def get_top_coins():

    tickers = client.get_ticker()

    df = pd.DataFrame(tickers)

    # Only USDT pairs
    df = df[df["symbol"].str.endswith("USDT")]

    # Convert volume to numbers
    df["quoteVolume"] = pd.to_numeric(df["quoteVolume"])

    # Sort by volume
    df = df.sort_values(
        "quoteVolume",
        ascending=False
    )

    # Return top 100 coins
    return df.head(100)["symbol"].tolist()
