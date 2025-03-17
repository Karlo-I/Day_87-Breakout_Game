Below is a self-reflection I have submitted to the course provider after completing the project, which I believe will help provide background for this repository.

Reflection:

The way I approached the project was exactly as the instructions suggested — that is, to avoid relying on a tutorial for building the project (which I tend to do in previous projects) and instead, to plan out the project and figure out how it should work.

I have tinkered with PyGame but opted for Tkinter, as I already have examples I can use to complete this project, such as the Ping Pong program.

I started by setting up the UI and the canvas, and then, one by one, added the objects needed for the game, such as the ball, paddle, and bricks.

Next, I worked on the methods for detecting collisions between the ball, wall, and paddle.

Everything was going well until I faced a couple of challenges:

- How to make the brick disappear when it is hit by the ball
- How to create a set of bricks with different colors, lined up in different layers
- I managed to resolve these issues by consulting ChatGPT for possible causes of the errors and suggestions for improvement.

Another edge case occurred when the ball seemed to oscillate inside the paddle when it first hit the sides of the paddle.

Again, ChatGPT provided some solutions. This was quite interesting because, as it turned out, my initial code wasn’t fully accounting for the full width of the paddle.
