import data


def main():


    info = data.get_data("BTCUSDT", "15m", 21)

    print(calculate_ema(20, info))
    ema20 = calculate_ema(20, info)
    print(calculate_ema(10, info))
    ema10 = calculate_ema(10, info)
    print(calculate_ema(5, info))
    ema5 = calculate_ema(5, info)


# multiplicator =  [2 ÷ (number of observations + 1)]
# EMA = (Closing price x multiplier) + (EMA (previous day) x (1-multiplier))

def calculate_ema(days, mydict, smoothing=2):
    prices = []
    counter = days
    while counter > 0:
        prices.append(float(mydict[counter]["close"]))
        counter -= 1
    ema = [sum(prices[:days]) / days]
    for price in prices[days:]:
        ema.append((price * (smoothing / (1 + days))) + ema[-1] * (1 - (smoothing / (1 + days))))
    return ema

if __name__ == "__main__":
    main()