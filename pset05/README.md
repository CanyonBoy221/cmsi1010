# Feathered Frenzy - Flappy Bird Game

A fun Pygame-based Flappy Bird clone with motivational quotes!

## Requirements

- Python 3.7+
- pygame
- requests

## Installation

```bash
pip install pygame requests
```

## How to Play

- **UP ARROW**: Make the bird flap and go up
- **DOWN ARROW**: Let gravity pull the bird down (no input needed)
- **SPACE**: Restart the game after game over

## Features

- Score tracking (count pipes passed)
- Collision detection with pipes and boundaries
- Random motivational quotes on game over (from Quotes API)
- Score history saved to `scores.txt` with timestamps
- Colorful graphics (circle bird, rectangle pipes)

## Game Over

When you crash, you'll see:
- Your final score
- A random quote to inspire you to play again
- Scores are automatically saved to `scores.txt`

## Notes

- This is a team project - make sure all team members have commits
- The game saves scores with timestamps for tracking
- If the quotes API is unavailable, a default message is shown
