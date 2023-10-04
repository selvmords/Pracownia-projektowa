import tkinter as tk

# from PIL import Image, ImageTk

WIDTH = 400
HEIGHT = 300
BALL_RADIUS = 10
PADDLE_WIDTH = 70
PADDLE_HEIGHT = 10
BALL_SPEED = 5

window = tk.Tk()
window.title("PING PONG")
game = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
game.pack()

paddle = game.create_rectangle(
    WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT,
    WIDTH // 2 + PADDLE_WIDTH // 2, HEIGHT, fill="white"
)
ball = game.create_oval(
    WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS,
    WIDTH // 2 + BALL_RADIUS, HEIGHT // 2 + BALL_RADIUS, fill="white"
)
ball_speed = 5

ball_speed_x = ball_speed
ball_speed_y = ball_speed
ball_dx = BALL_SPEED
ball_dy = BALL_SPEED
paddle_speed = 10


def move_ball():
    global ball_dx, ball_dy

    ball_coords = game.coords(ball)

    if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
        ball_dx *= -1

    if game.coords(ball)[1] <= game.coords(paddle)[3]:
        if game.coords(ball)[0] >= game.coords(paddle)[0] and game.coords(ball)[2] <= game.coords(paddle)[2]:
            ball_dy *= -1

    if ball_coords[3] >= HEIGHT:
        window.after_cancel(ball_animation)

    game.move(ball, ball_dx, ball_dy)
    window.after(30, move_ball)


def move_paddle(event):
    paddle_coord = game.coords(paddle)

    if event.keysym == "Left" and paddle_coord[1] > 0:
        game.move(paddle, -20, 0)
    elif event.keysym == "Right" and paddle_coord[3] < WIDTH:
        game.move(paddle, 20, 0)


window.bind("<KeyPress-Left>", move_paddle)
window.bind("<KeyPress-Right>", move_paddle)

ball_animation = window.after(1000, move_ball)

window.mainloop()
