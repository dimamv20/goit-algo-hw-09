def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            num_coin = amount // coin
            result[coin] = num_coin
            amount -= num_coin * coin
    return result


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev_coin = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev_coin[i] = coin

    result = {}
    while amount > 0:
        result[prev_coin[amount]] = result.get(prev_coin[amount], 0) + 1
        amount -= prev_coin[amount]
    return result

def main():
    amount = 113
    coins_greedy = find_coins_greedy(amount)
    print("Greedy algorithm:", coins_greedy)
    
    coins_dynamic = find_min_coins(amount)
    print("Dynamic programming algorithm:", coins_dynamic)

if __name__ == "__main__":
    main()
