import tkinter as tk

# Game constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
BALL_SPEED_X = 6
BALL_SPEED_Y = 6
PADDLE_SPEED = 20
SCORE_FONT = ('Arial', 30, 'bold')
WINNING_SCORE = 5

# Paddle class
class Paddle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.paddle = canvas.create_rectangle(x, y, x + 30, y + 130, fill='blue')

    def move_up(self):
        if self.canvas.coords(self.paddle)[1] > 0:
            self.canvas.move(self.paddle, 0, -PADDLE_SPEED)

    def move_down(self):
        if self.canvas.coords(self.paddle)[3] < WINDOW_HEIGHT:
            self.canvas.move(self.paddle, 0, PADDLE_SPEED)

# Ball class
class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ball = canvas.create_oval(510, 310, 530, 330, fill='red')

        self.dx = BALL_SPEED_X
        self.dy = BALL_SPEED_Y

    def move(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)

        # Bounce off top and bottom walls
        if pos[1] <= 0 or pos[3] >= WINDOW_HEIGHT:
            self.dy *= -1

        # Check collision with paddles
        if self.check_collision(player1.paddle) or self.check_collision(player2.paddle):
            self.dx *= -1

        # Reset ball if it goes out of bounds and update score
        if pos[0] <= 0:
            update_score(2)
            self.reset_position()
        elif pos[2] >= WINDOW_WIDTH:
            update_score(1)
            self.reset_position()

    def reset_position(self):
        self.canvas.coords(self.ball, 490, 290, 510, 310)
        self.dx *= -1

    def check_collision(self, paddle):
        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(paddle)
        return (ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and
                ball_pos[3] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3])

# Move paddles
def key_pressed(event):
    if not game_over:
        if event.keysym == 'w':
            player1.move_up()
        elif event.keysym == 'x':
            player1.move_down()
        elif event.keysym == 'Up':
            player2.move_up()
        elif event.keysym == 'Down':
            player2.move_down()

# Update game
def update():
    if not game_over:
        ball.move()
    root.after(20, update)

# Update score and check for winner
def update_score(player):
    global score1, score2, game_over
    if player == 1:
        score1 += 1
    else:
        score2 += 1

    canvas.itemconfig(score_display, text=f"{score1} - {score2}")

    # Check if a player has won
    if score1 >= WINNING_SCORE:
        declare_winner(1)
    elif score2 >= WINNING_SCORE:
        declare_winner(2)

# Declare winner and stop the game
def declare_winner(player):
    global game_over
    game_over = True
    canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text=f"Player {player} Wins!", fill='white', font=('Arial', 40, 'bold'))

# Restart the game
def restart_game():
    global score1, score2, game_over, player1, player2, ball, score_display
    score1, score2 = 0, 0
    game_over = False
    canvas.delete("all")

    # Reinitialize paddles and ball
    player1 = Paddle(canvas, 30, 250)
    player2 = Paddle(canvas, 950, 250)
    ball = Ball(canvas)

    # Recreate score display
    score_display = canvas.create_text(WINDOW_WIDTH//2, 50, text=f"{score1} - {score2}", fill='white', font=SCORE_FONT)
    update()

# Cancel game
def cancel_game():
    root.destroy()

# Main application
root = tk.Tk()
root.title("2 Player Bouncing Ball Game")
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')
canvas.pack()

player1 = Paddle(canvas, 30, 250)
player2 = Paddle(canvas, 950, 250)
ball = Ball(canvas)

game_over = False
score1, score2 = 0, 0
score_display = canvas.create_text(WINDOW_WIDTH//2, 50, text=f"{score1} - {score2}", fill='white', font=SCORE_FONT)

cancel_button = tk.Button(root, text="Cancel", bg="grey", command=cancel_game)
cancel_button.pack()

restart_button = tk.Button(root, text="Restart", bg="grey", command=restart_game)
restart_button.pack()

root.bind('<KeyPress>', key_pressed)
update()
root.mainloop()
