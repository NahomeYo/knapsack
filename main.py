def knapsack(weights, values, capacity):
    item_count = len(weights)
    table = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    for item in range(1, item_count + 1):
        weight = weights[item - 1]
        value = values[item - 1]
        for current_capacity in range(capacity + 1):
            if weight > current_capacity:
                table[item][current_capacity] = table[item - 1][current_capacity]
            else:
                table[item][current_capacity] = max(
                    table[item - 1][current_capacity],
                    table[item - 1][current_capacity - weight] + value,
                )

    return table[item_count][capacity]


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    print("Best value:", knapsack(weights, values, capacity))
