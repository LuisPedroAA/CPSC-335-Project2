from itertools import combinations

def stock_maximization(M, items):
    best = None

    # Generate all possible combinations of stocks
    for num_stocks in range(1, len(items) + 1):
        for candidates in combinations(items, num_stocks):
            if verify_combination(M, candidates):
                if best is None or total_value(candidates) > total_value(best):
                    best = candidates

    return total_value(best) if best is not None else 0

def verify_combination(M, stocks):
    # Check if the total cost of the selected stocks is within the budget
    return sum(stock[1] for stock in stocks) <= M

def total_value(stocks):
    # Calculate the total value of the selected stocks
    return sum(stock[1] for stock in stocks)

def main():
    with open("input.txt", "r") as input_file:
        N = int(input_file.readline().strip())
        Stocks_and_values = [list(map(int, input_file.readline().strip().split())) for _ in range(N)]
        Amount = int(input_file.readline().strip())

    result = stock_maximization(Amount, Stocks_and_values)

    with open("output.txt", "w") as output_file:
        output_file.write(str(result))

if __name__ == "__main__":
    main()