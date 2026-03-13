# Knapsack

## Complexity

- Best: O(nk)
- Worst: O(nk)
- Avg: O(nk)
- Space: O(nk)

## Problem Description

The 0-1 knapsack problem asks for the maximum total value that can fit within a fixed capacity when each item may be chosen at most once. Every item has both a weight and a value, so the challenge is not just to pack as many items as possible, but to choose the combination that gives the best total value without exceeding the capacity limit.

This implementation uses dynamic programming to compute the best value for every prefix of items and every capacity from 0 through `k`. The problem is called 0-1 knapsack because for each item there are only two choices: take it once or do not take it at all.

## Code

```javascript
/**
 * Solve the 0-1 knapsack problem with dynamic programming.
 *
 * @param {{weight: number, value: number}[]} items Available items.
 * @param {number} capacity Maximum total weight.
 * @returns {number[][]} Completed dynamic programming table.
 */
function knapsack(items, capacity) {
    const dp = Array.from({ length: items.length + 1 }, () => Array(capacity + 1).fill(0));

    for (let itemIndex = 1; itemIndex <= items.length; itemIndex++) {
        for (let currentCapacity = 0; currentCapacity <= capacity; currentCapacity++) {
            const currentItem = items[itemIndex - 1];

            if (currentItem.weight <= currentCapacity) {
                // Compare skipping the item with taking it once.
                dp[itemIndex][currentCapacity] = Math.max(
                    dp[itemIndex - 1][currentCapacity],
                    dp[itemIndex - 1][currentCapacity - currentItem.weight] + currentItem.value
                );
            } else {
                dp[itemIndex][currentCapacity] = dp[itemIndex - 1][currentCapacity];
            }
        }
    }

    return dp;
}

/**
 * Format the item list for console output.
 *
 * @param {{weight: number, value: number}[]} items Available items.
 * @returns {string} Formatted item string.
 */
function formatItems(items) {
    return items
        .map((item) => `{ weight: ${item.weight}, value: ${item.value} }`)
        .join(", ");
}

/**
 * Format a 2D dynamic programming table for console output.
 *
 * @param {number[][]} table Dynamic programming table.
 * @returns {string} Formatted table string.
 */
function formatTable(table) {
    return table.map((row) => `[${row.join(", ")}]`).join(", ");
}

/**
 * Run the knapsack demonstration.
 *
 * @returns {void}
 */
function main() {
    const items = [
        { weight: 2, value: 3 },
        { weight: 3, value: 4 },
        { weight: 4, value: 5 },
    ];
    const maxCapacity = 5;

    console.log(`Original items = ${formatItems(items)}`);
    console.log(`Max capacity = ${maxCapacity}`);
    console.log(`DP table = ${formatTable(knapsack(items, maxCapacity))}`);
}

main();
```

## Algorithm Steps

1. Create a dynamic programming table with `n + 1` rows and `k + 1` columns.
2. Use row `i` to represent the first `i` items and column `j` to represent capacity `j`.
3. Initialize the first row and first column to 0 to represent empty-item and zero-capacity cases.
4. For each item and capacity, decide whether taking the item improves the best known value.
5. If the item fits, choose the larger of skipping it and taking it once.
6. If the item does not fit, copy the value from the row above.
7. Return the completed table after every row and capacity has been processed.

## Explanation

Each table entry `dp[i][j]` stores the best total value obtainable using the first `i` items with capacity `j`. That means every cell represents a smaller version of the original problem. Instead of exploring every possible subset directly, the algorithm fills the table one row at a time and reuses answers that have already been computed.

If the current item fits inside the current capacity, the recurrence compares two choices: skip the item and keep the value `dp[i - 1][j]`, or take the item once and add its value to the best answer from the remaining capacity, `dp[i - 1][j - weight] + value`. If the item does not fit, the algorithm has no decision to make and simply copies the value from the row above.

In the JavaScript implementation, the dynamic programming table is created with `Array.from()` and `fill(0)`, which gives a full 2D table of zeros before the algorithm begins. Then `Math.max()` is used in the recurrence to choose between skipping the item and taking it once. The formatting helpers later use `map()` and `join()` so the items and the finished table can be displayed clearly in the example output.

Because the table contains `(n + 1)(k + 1)` cells and each cell is filled in constant time, the runtime is `O(nk)`. The implementation stores the entire table, so the space usage is also `O(nk)`. That runtime is pseudo-polynomial because it depends on the numeric capacity `k`, not just on the number of items.
