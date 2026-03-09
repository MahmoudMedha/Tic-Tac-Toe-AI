# Tic Tac Toe (X/O) with Minimax AI

This is a simple Tic Tac Toe desktop game built with **Python** and **Tkinter**, featuring an AI opponent that uses the **Minimax algorithm** to play optimally.

## 🎮 Project Structure

- `game.py` - Main GUI application. Uses Tkinter to render the board and handle user interaction.
- `ai.py` - Minimax AI implementation that chooses the optimal move for the AI player.

## 🧠 How the AI Works

- The AI uses **Minimax** to evaluate all possible game states and choose the move that maximizes its chance of winning.
- The AI can **never lose** when played optimally (it will win or force a draw).

## ▶️ How to Run

1. Make sure you have Python installed (3.8+ recommended).
2. Run the game:

```bash
python game.py
```

3. Play by clicking on an empty cell. The AI will respond automatically.

## 🕹️ Controls & Behavior

- Click a cell to place your symbol.
- The AI will play immediately after your move.
- Click **New Game** to restart and swap sides (player becomes AI and vice versa).

## 📌 Notes

- You can customize the player and AI symbols by editing `player_symbol` and `ai_symbol` in `ai.py` and `game.py`.
- The AI uses a depth-unlimited Minimax search, so it plays perfectly.

## ✅ Requirements

- Python (3.x)
- Tkinter (usually included with standard Python installs)

Enjoy playing!
