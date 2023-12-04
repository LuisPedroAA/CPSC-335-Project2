def max_stocks(N, stocks_and_values, amount):
    dp = [[0] * (amount + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, amount + 1):
            if stocks_and_values[i - 1][1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stocks_and_values[i - 1][1]] + stocks_and_values[i - 1][0])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][amount]

def main():
    with open("input.txt", "r") as file:
        N = int(file.readline().strip())
        stocks_and_values = [list(map(int, file.readline().strip().split())) for _ in range(N)]
        amount = int(file.readline().strip())

    result = max_stocks(N, stocks_and_values, amount)

    with open("output.txt", "w") as file:
        file.write(str(result) + "\n")

if __name__ == "__main__":
    main()
