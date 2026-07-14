from scanner import get_top_coins

print("🔥 Crypto FVG Scanner Starting...\n")

coins = get_top_coins()

print("Top Binance coins:")

for coin in coins:
    print("✅", coin)
