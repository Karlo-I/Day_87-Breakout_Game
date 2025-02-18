from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick_manager import Brick
from random import randint
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0) # Turn off automatic screen updates for better performance

paddle = Paddle((0, -250))
ball = Ball((randint(-350, 350), -210))
brick = Brick()
scoreboard = Scoreboard((-350, 250))

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

brick.create_bricks()

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with left and right walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    paddle_hit = False

    # Define the paddle's width and height
    paddle_width = 8 * 20  # paddle's width is 8 * 20 = 160 units
    paddle_height = 20  # height of the paddle

    # Check if the ball is within the horizontal and vertical bounds of the paddle
    if (ball.xcor() > paddle.xcor() - paddle_width / 2 and ball.xcor() < paddle.xcor() + paddle_width / 2 and
            ball.ycor() > paddle.ycor() - paddle_height / 2 and ball.ycor() < paddle.ycor() + paddle_height / 2):

        paddle_hit = True

        ball_x = ball.xcor()
        ball_y = ball.ycor()
        paddle_x = paddle.xcor()
        paddle_y = paddle.ycor()

        # If the ball hits the top of the paddle, bounce vertically
        if ball_y > paddle_y:
            ball.bounce_y()
            # Prevent the ball from sinking into the paddle by correcting its position
            if ball_y < paddle_y + paddle_height / 2:  # Adjust the ball's position if it's inside the paddle
                ball.sety(paddle_y + paddle_height / 2)

        # Ball hitting the sides of the paddle (bounce horizontally)
        elif abs(ball_x - paddle_x) < paddle_width / 2:  # Handle side collisions
            # ball.bounce_x()
            # Prevent the ball from sinking into the paddle horizontally
            if ball_x < paddle_x + paddle_width / 2 and ball_x > paddle_x - paddle_width / 2:
                ball.setx(paddle_x + paddle_width / 2 if ball_x > paddle_x else paddle_x - paddle_width / 2)

    # Detect paddle misses
    if ball.ycor() < -280:
        print("Ball missed the paddle!")
        game_is_on = False # End the game
        scoreboard.game_over()

    # Detect collision with brick
    bricks_hit = False  # Flag to check if a brick was hit
    for brick_obj in brick.all_bricks:
        if ball.distance(brick_obj) < 50:
            print(f"Ball hit a {brick_obj.color()[0]} brick!")
            brick.remove_brick(brick_obj) # Remove brick on collision
            bricks_hit = True # Set the flag to True if a brick was hit

            ball_x = ball.xcor()
            ball_y = ball.ycor()
            brick_x = brick.xcor()
            brick_y = brick.ycor()

            scoreboard.score_up()

            # Determine where the ball hit the brick
            if abs(ball_x - brick_x) > abs(ball_y - brick_y):
                # Left / Right Collision, if the horizontal distance is greater than the vertical distance, it means the
                # ball is more "aligned" with the left or right side of the brick (e.g. ball is likely hitting the side
                # of the brick (left or right)
                ball.bounce_x()
            else: # Top / Bottom Collision
                ball.bounce_y()

    # Debugging: Check if all bricks are removed
    if not brick.all_bricks:
        print("All bricks have been removed!")

    # Optional: If you want to end the game when there are no bricks left
    if not brick.all_bricks:
        print("You win! All bricks are gone!")
        game_is_on = False

screen.exitonclick()