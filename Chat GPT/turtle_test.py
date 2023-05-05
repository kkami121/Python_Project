import turtle

# Set up the turtle window
window = turtle.Screen()
window.title("5x5 Tic Tac Toe")
window.bgcolor("white")
window.setup(width=600, height=600)

# Create a turtle pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.goto(-250, 250)
pen.pendown()

# Draw the game board
for i in range(4):
    pen.forward(500)
    pen.right(90)
pen.right(90)
for i in range(4):
    pen.forward(500)
    pen.right(90)

# Create a list to store the player moves
moves = [[None for j in range(5)] for i in range(5)]

# Set up the players
players = ["X", "O"]
current_player = players[0]

# Define a function to handle player moves
def click(x, y):
    global current_player
    i = int((y + 250) // 100)
    j = int((x + 250) // 100)
    if moves[i][j] == None:
        moves[i][j] = current_player
        draw_player(current_player, i, j)
        if check_win(current_player):
            turtle.penup()
            turtle.goto(-150, 0)
            turtle.pendown()
            turtle.write(current_player + " wins!", font=("Arial", 24, "bold"))
            window.exitonclick()
        current_player = players[(players.index(current_player) + 1) % 2]

# Define a function to draw a player's move
def draw_player(player, i, j):
    turtle.penup()
    turtle.goto(j*100-250+50, i*100-250+50)
    turtle.pendown()
    if player == "X":
        turtle.write("X", align="center", font=("Arial", 48, "normal"))
    elif player == "O":
        turtle.write("O", align="center", font=("Arial", 48, "normal"))

# Define a function to check for a win
def check_win(player):
    # Check rows
    for i in range(5):
        if moves[i] == [player]*5:
            return True
    # Check columns
    for j in range(5):
        if [moves[i][j] for i in range(5)] == [player]*5:
            return True
    # Check diagonals
    if [moves[i][i] for i in range(5)] == [player]*5:
        return True
    if [moves[i][4-i] for i in range(5)] == [player]*5:
        return True
    return False

# Set up the turtle listener
turtle.listen()
turtle.onscreenclick(click)

# Start the game
turtle.mainloop()
