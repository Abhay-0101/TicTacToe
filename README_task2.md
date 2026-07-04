# Task 2 - Tic-Tac-Toe AI

**CodSoft AI Internship**

## About
An unbeatable Tic-Tac-Toe AI built using the **Minimax algorithm** with
**Alpha-Beta pruning**. You play as `X`, the AI plays as `O`, on the command line.

## How it works
- **Minimax**: The AI explores every possible sequence of future moves,
  assuming the human always plays their best possible counter-move. It
  picks the move that leads to the best guaranteed outcome for itself
  (win > draw > loss).
- **Alpha-Beta Pruning**: A speed optimization on top of Minimax. It
  skips exploring branches of the game tree that cannot possibly affect
  the final decision, without changing the outcome. This is why the AI
  responds instantly even though it's technically evaluating the whole
  game tree.
- **Depth-aware scoring**: Wins are scored higher the faster they happen
  (`10 - depth`) and losses are scored less negative the longer they're
  delayed (`depth - 10`), so the AI prefers winning quickly and, if a
  loss were ever forced, delaying it as long as possible.

## Result
Because Tic-Tac-Toe is a "solved" game, a perfect player can never lose.
This AI has been tested against a simulated perfect opponent and **always
results in at least a draw** — it can never be beaten.

## How to run
```bash
python3 tic_tac_toe.py
```

You'll be shown a position guide (cells numbered 1–9). Enter a number each
turn to place your `X`. The AI responds automatically as `O`.

```
Cell positions:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## Tech used
- Python 3
- Minimax algorithm (game theory / adversarial search)
- Alpha-Beta pruning (search optimization)

---
Part of the CodSoft Artificial Intelligence Internship (Task 2 of 5).
