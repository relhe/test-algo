import math

def coin_change_greedy(cash:list, amount: int)->list:
    s = []
    p = max(cash)
    while amount > 0:
        if amount >= p:
            p = max(cash)
            amount -= p
            amount = round(amount, 2)
            s.append(p)
        else:
            cash.remove(p)
            p = max(cash)
    return s

# to be reviewed
def coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else float('inf') for c in coins]) + 1
    return dp[-1] if dp[-1] != float('inf') else -1

def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    elif amount < 0:
        return float('inf')
    else:
        list_of_coins = [coin_change_recursive(coins, amount - c) for c in coins]
        print(list_of_coins)
        return min(list_of_coins) + 1

def coin_change_recursive_memo(coins, amount):
    memo = {}
    def coin_change_recursive_memo_helper(coins, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        else:
            if amount in memo:
                return memo[amount]
            else:
                memo[amount] = min([coin_change_recursive_memo_helper(coins, amount - c) for c in coins]) + 1
                return memo[amount]
    return coin_change_recursive_memo_helper(coins, amount)

def coin_change_recursive_memo_optimized(coins, amount):
    memo = {}
    def coin_change_recursive_memo_helper(coins, amount):
        if amount == 0:
            return 0
        elif amount < 0:
            return float('inf')
        else:
            if amount in memo:
                return memo[amount]
            else:
                memo[amount] = min([coin_change_recursive_memo_helper(coins, amount - c) for c in coins]) + 1
                return memo[amount]
    return coin_change_recursive_memo_helper(coins, amount)


if __name__ == '__main__':
    coins = [0.1, 0.05, 0.25, 1, 2, 5, 50, 20, 10, 100]
    amount = float(input(
        'Enter the amount to be changed : '
    ))
    try :
        change_list = coin_change_greedy(coins, amount)
        print(change_list)
        print('The amount can be changed with {} coins and banknotes'.format(len(change_list)))
    except ValueError:
        print('The amount cannot be changed exactly')