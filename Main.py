from scanner import get_top_coins
from fvg import check_fvg

print("🔥 Crypto FVG Scanner Starting...\n")

coins = get_top_coins()

setups = []

print("Scanning coins...\n")


for coin in coins:

    symbol = coin + "USDT"

    result = check_fvg(symbol)

    if result:
        setups.append(result)


print("\n🔥 BEST FVG SETUPS 🔥\n")


if len(setups) == 0:

    print("No setups found.")

else:

    for setup in setups:

        print(
            setup["coin"],
            "-",
            setup["direction"],
            "- Score:",
            setup["score"]
        )

        print("Reasons:")

        for reason in setup["reasons"]:
            print(" ✅", reason)

        print()
        