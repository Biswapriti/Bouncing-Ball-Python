![Screenshot 2025-01-22 155255](https://github.com/user-attachments/assets/124d63d8-1ac7-4db1-ad66-c198a79ecf24)

# 🏀 Bouncing Ball Game - Python (Pygame)

A simple and fun bouncing ball game made using Python and the Pygame library. The ball bounces within the screen, changing direction when it hits the edges. This project demonstrates basic physics, collision detection, and animation using Pygame.

---

## 📸 Preview

![Bouncing Ball GIF](preview.gif) <!-- Optional: You can add a gif or image -->

---

## 🧰 Tech Stack

- **Python 3**
- **Pygame**

---

## 🚀 Features

- Ball movement and bouncing mechanics
- Window boundaries collision detection
- Customizable ball speed, color, and window size
- Easy to modify for learning purposes

---

## 🔧 Requirements

Make sure you have Python installed. Then install Pygame:

```bash
pip install pygame
📦 Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Biswapriti/bouncing-ball-game.git
cd bouncing-ball-game
Run the game:

bash
Copy code
python bouncing_ball.py
🧠 How It Works
A ball is drawn on the screen using pygame.draw.circle().

The position of the ball updates every frame based on its velocity.

When it hits the screen borders, the velocity is inverted to simulate a bounce.

📁 File Structure
text
Copy code
bouncing-ball-game/
│
├── bouncing_ball.py   # Main game logic
├── README.md           # Game documentation
└── preview.gif         # (Optional) Game preview animation
🎯 Example Code Snippet
python
Copy code
if ball_x + radius > width or ball_x - radius < 0:
    velocity_x *= -1
if ball_y + radius > height or ball_y - radius < 0:
    velocity_y *= -1
💡 Ideas to Extend
Add multiple balls

Add gravity and friction

Track score or number of bounces

Add sound effects

🤝 Contributing
Contributions, ideas, and feedback are welcome! Feel free to fork this project and submit pull requests.

📄 License
This project is licensed under the MIT License.

🙋‍♀️ Author
Made with ❤️ by Biswapriti

