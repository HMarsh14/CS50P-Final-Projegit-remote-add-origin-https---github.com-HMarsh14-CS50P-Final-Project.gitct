# Space Invaders Game - README

#### Project Video URL: https://youtu.be/MXJ756_xDBI

## Overview
This project is a classic "Space Invaders" style game built using Python and the Pygame library, and is my first project I have made using python and pygame. Players control a spaceship, shoot down enemy aliens, and aim to achieve the highest score possible. The game also includes features like a leaderboard, sound effects, and a main menu.

## Features
- Player Control: Move the player spaceship left and right using the 'A' and 'D' keys, and fire bullets with the 'SPACE' key.
- Enemies: A group of alien enemies moves across the screen, dropping down after hitting boundaries. The player must shoot them before they reach the bottom.
- Bullet Mechanics: Players can fire one bullet at a time, and they must wait for the bullet to go off-screen or hit an enemy before firing again.
- Collision Detection: The game uses basic distance calculation to detect bullet collisions with enemies.
- Score and Leaderboard: The game keeps track of the player's score and allows for submitting and viewing the top 10 scores.
- Sound Effects: Background music and sound effects for shooting and enemy destruction are included.
- Game Over: The game ends when an enemy reaches the bottom of the screen, after which the player's score can be submitted to the leaderboard.

## Installation

### Prerequisites
- Python 3.x
- Pygame library: Install using the following command:


### Assets
Ensure you have the following assets in the same directory as the Python script:
- Images:
  - space-invaders-background.png
  - space-invaders.png
  - player.png
  - enemy.png
  - bullet.png
  
- Sounds:
  - laser.wav (for bullet firing)
  - explosion.wav (for enemy destruction)
  - background.wav (for background music)

- Leaderboard File:  
  - leaderboard.csv (for storing leaderboard scores in CSV format)

## How to Play
1. Main Menu: 
   - Use the number keys (1, 2, 3) to navigate:
     - 1: Start the game
     - 2: View the leaderboard
     - 3: Exit the game

2. Gameplay: 
   - Move the player spaceship using the 'A' (left) and 'D' (right) keys.
   - Fire bullets by pressing the 'SPACE' key.
   - Shoot down enemies before they reach the bottom of the screen.
   - If an enemy reaches the bottom, the game will end, and your score can be submitted.

3. Leaderboard:
   - After the game ends, you can enter your name and submit your score to the leaderboard. Only the top 10 scores are saved.
   - View the leaderboard from the main menu.

## Game Components

### Functions
- main_menu(): Displays the main menu and handles navigation to the game, leaderboard, or exit.
- game(screen): The core game loop. Manages player movement, enemy generation, collision detection, and score updates.
- display_window(): Sets up the game window, background music, and game icon.
- player(screen, x, y): Renders the player sprite on the screen.
- enemy(screen, x, y): Renders an enemy sprite on the screen.
- fire_bullet(screen, x, y): Renders the bullet when fired.
- detect_collision(enemy_x, enemy_y, bullet_x, bullet_y): Detects a collision between an enemy and a bullet using distance-based calculations.
- show_score(screen, x, y, score): Displays the player's score on the screen during gameplay.
- game_over(screen, score): Handles the game over screen, allowing players to return to the main menu or submit their score.
- leaderboard(screen): Displays the top 10 scores from 'leaderboard.csv'.
- submit_score(score, user_input): Saves the player's score to the leaderboard and ensures that only the top 10 scores are saved.

## Future Improvements
- Levels: Add increasing difficulty with more enemies or faster speeds as the player progresses.
- Power-ups: Introduce power-ups for the player, such as faster shooting or shields.
- Multiplayer: Implement local multiplayer support for more engaging gameplay.

All Pull Requests and help would be amazing, I'm constantly trying to learn and appreciate all feedback given.

## Known Issues
- The game currently supports only keyboard controls. Additional input methods (like game controllers) could be added.
- The game does not save the leaderboard between sessions unless the 'leaderboard.csv' file is already present. Ensure this file is created in the same directory before running the game.

## Credits
- Pygame Library: https://www.pygame.org/
  
All graphical and sound assets are either free to use or were created for this project.
