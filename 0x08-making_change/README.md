# 0x08-making_change

This directory contains solutions and notes for the "making change" / coin change problem. The goal is to compute the minimum number of coins needed to make a given amount using a set of coin denominations.

This README explains the problem, the approaches used, when each approach is appropriate, complexity trade-offs, usage, examples, and recommended next steps for contributors and engineers reviewing the code.

---

## Problem statement

Given:
- A list of positive integer coin denominations (e.g., [25, 10, 5, 1]) — typically sorted in descending order.
- A target amount (non-negative integer).

Return:
- The minimum number of coins required to make the target amount using those denominations, or -1 / an error if the amount cannot be represented by the given coins (depending on the repository's conventions).

Assumptions:
- Each coin denomination can be used an unlimited number of times.
- Coin denominations do not necessarily include 1, so some amounts might be impossible.

Example:
- Input: denominations = [25, 10, 5, 1], amount = 37
- Output: 4 (25 + 10 + 1 + 1)

---

## Typical files in this directory

(If any filename below differs from the repository, adapt the examples to the actual filenames)
- making_change.py — primary implementation(s) for the coin change problem (greedy and / or dynamic).
- tests/ — unit tests that validate correctness across edge-cases and typical inputs.
- README.md — this file.

---

## Approaches

1. Greedy algorithm
   - Strategy: repeatedly take the largest denomination that does not exceed the remaining amount until the amount is zero.
   - When it works: The greedy algorithm yields an optimal solution for canonical coin systems (e.g., modern US coin denominations [25, 10, 5, 1]). It is fast and simple.
   - When it fails: For some coin systems (non-canonical), the greedy algorithm does not guarantee an optimal solution. Example counterexample for [1, 3, 4] and amount 6:
     - Greedy chooses 4 + 1 + 1 = 3 coins, but optimal is 3 + 3 = 2 coins.
   - Complexity: O(n) per coin choice if denominations are scanned left-to-right; overall O(k) where k is number of coins used. For an amount A, worst-case number of iterations is O(A) if smallest coin is 1 and you pick 1 repeatedly.

2. Dynamic Programming (DP) — the robust solution
   - Strategy: use bottom-up DP to compute the minimum coins for every value from 0 to amount:
     dp[0] = 0
     dp[x] = min(dp[x - coin] + 1 for coin in coins if coin <= x)
   - Guarantees an optimal solution for any coin set.
   - Complexity: time O(len(coins) * amount), space O(amount).
   - Use when: coin system is arbitrary or when correctness must be guaranteed for all inputs.

3. Mixed strategy
   - If the coin set is known to be canonical and performance is critical, prefer greedy.
   - If coin set may be arbitrary or correctness is critical, use DP.
   - For large amounts with many denominations and strict memory/time constraints, consider optimized DP variants (e.g., BFS on states, coin-change with heuristics), but always measure.

---

## Recommended API / Usage patterns

Example function signatures (adapt to actual implementation in this repo):

- def min_coins_greedy(amount: int, coins: List[int]) -> int:
  - Returns the number of coins used by greedy strategy, or -1 if impossible (when coins can't make the amount).

- def min_coins_dp(amount: int, coins: List[int]) -> int:
  - Returns the minimum number of coins using DP, or -1 if impossible.

Command-line usage examples (if a script exists):
- python3 making_change.py 37
  - Output: 4

Unit tests should include:
- Basic canonical system test (e.g., [25, 10, 5, 1])
- Known counterexample for greedy (e.g., coins [1, 3, 4], amount 6)
- Impossible amount (e.g., coins [5, 10], amount 3)
- Edge cases: amount 0, empty coins list, repeated denominations, unsorted input

---

## Implementation notes and best practices

- Input sanitization:
  - Validate amount is a non-negative integer.
  - Validate denominations are positive integers, unique (or normalize duplicates), and non-zero.
  - Sort denominations in descending order for greedy; ascending or any order is fine for DP.

- Return values and error handling:
  - Decide on a consistent policy: e.g., return -1 for impossible amounts, or raise ValueError. Document and test that convention.

- Performance:
  - Greedy: constant space O(1) beyond inputs; very fast for canonical sets.
  - DP: linear space O(amount). If amount is large (e.g., millions), consider optimizations or streaming approaches.

- Tests:
  - Include tests that explicitly assert when greedy fails and show DP succeeds. This helps future engineers understand the limitations of greedy solutions.

---

## Example walkthrough

Target = 37, coins = [25, 10, 5, 1]
- Greedy:
  - 37 >= 25 -> take 25 (remaining 12)
  - 12 >= 10 -> take 10 (remaining 2)
  - 2 >= 1 -> take 1 (remaining 1)
  - 1 >= 1 -> take 1 (remaining 0)
  - Total coins = 4 (optimal for this coin set)

Counterexample where greedy fails:
- Target = 6, coins = [4, 3, 1] (or [1, 3, 4])
  - Greedy: take 4 -> remaining 2 -> take 1 + 1 -> total 3 coins
  - DP optimal: 3 + 3 -> total 2 coins

---

## Complexity summary

- Greedy: time O(number_of_coins_used * denominations_scan) — effectively near O(amount / largest_coin) in practical runs; space O(1).
- DP (bottom-up): time O(amount * len(coins)), space O(amount).

---

## Notes for contributors and reviewers

- If you add or modify an implementation:
  - Add unit tests that cover the new behavior.
  - If adding a greedy-based optimization, add a clear comment describing which coin systems it is valid for and include tests showing known failures.
  - If you make DP faster or more memory-efficient, include benchmarking notes and rationale.

---

## Next steps (recommended)

- Add a canonical test suite demonstrating both greedy success cases and greedy failure counterexamples.
- Include a small benchmark script comparing greedy vs DP for typical coin sets and large amounts.
- If the repository currently contains only greedy, consider adding a DP implementation and tests so reviewers can compare correctness and performance.

---

Acknowledgements
- Problem and structure adapted for clarity to help engineers reading the code quickly determine correctness trade-offs and how to run tests and reproduce results.
