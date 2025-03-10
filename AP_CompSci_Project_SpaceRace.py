# the purpose of this program is to be a recreation of the popular arcade game in 1973, Space Race
# import turtle, time, math, and random, all of which will be used in this program
import turtle as trtl
import time
import math
import random

# setting up turtle screen, various turtles, and over variables important to the program
wn = trtl.Screen()
# setting turtle screen to black
wn.bgcolor("black")
# turtle that will be drawing the title screen and the line dividing the two players
screendraw = trtl.Turtle()
screendraw.speed(0)
screendraw.hideturtle()
# turtle that will represent player 1
player1 = trtl.Turtle()
player1.hideturtle()
# setting the turtle color to white so it will actually be visible
player1.color("white")
player1.speed(0)
# turtle that will represent player 2
player2 = trtl.Turtle()
player2.color("white")
player2.hideturtle()
player2.speed(0)
# score variables
player1score = 0
player2score = 0
# sets standard font setup for score display and timer
font_setup = ("Arial", 15, "normal")
# turtle that will update score for player 1
scorewriter1 = trtl.Turtle()
scorewriter1.speed(0)
scorewriter1.hideturtle()
scorewriter1.pencolor('white')
scorewriter1.penup()
scorewriter1.goto(-500, 300)
scorewriter1.pendown()
# turtle that will update score for player 2
scorewriter2 = trtl.Turtle()
scorewriter2.speed(0)
scorewriter2.hideturtle()
scorewriter2.pencolor('white')
scorewriter2.penup()
scorewriter2.goto(500, 300)
scorewriter2.pendown()
# duration of the game, which is 1 minute
timer = 40
# sets the variable of the timer being up to false
timer_up = False
# initiates empty lists that will be filled with turtles representing asteroids and their corresponding direction that they are moving towards
asteroid_list = []
asteroid_direction = []
# turtle that will display the time remaining
counter = trtl.Turtle()
counter.speed(0)
counter.hideturtle()
counter.pencolor('white')
counter.penup()
counter.goto(0, 300)
counter.pendown()
counter_interval = 1000
# iteration variable
x = 0

# countdown function
def countdown():
  # make the timer and timer_up variables global so they can be used everywhere
  global timer, timer_up
  # clear the current time before writing anything
  counter.clear()
  # if the timer is up
  if timer == 0:
    # set timer_up to true
    timer_up = True
    # clear the whole screen
    wn.clear()
    # set the background color to black
    wn.bgcolor("black")
    # write Time's Up!
    counter.write("Time's Up!", align='center', font=font_setup)
    # write player 1's score
    scorewriter1.penup()
    scorewriter1.goto(0, 100)
    scorewriter1.pendown()
    scorewriter1.write("Player 1's score: " + str(player1score), align='center', font=font_setup)
    # write player 2's score
    scorewriter2.penup()
    scorewriter2.goto(0, -100)
    scorewriter2.pendown()
    scorewriter2.write("Player 2's score: " + str(player2score), align='center', font=font_setup)
  # if the timer is not up
  else:
    # subtract 1 from the timer
    timer -= 1
    # update the timer
    counter.write("Timer: " + str(timer), align='center', font=font_setup)
    counter.getscreen().ontimer(countdown, counter_interval)

# collision check function with two parameters, asteroid and player, function checks distance between these two
def isCollision(asteroid, player):
  # uses distance formula to caluclate the distance between a player and an asteroid
  distance = math.sqrt(math.pow(asteroid.xcor()-player.xcor(),2)+math.pow(asteroid.ycor()-player.ycor(),2))
  # if the distance is less than 40 which is the point around which an asteroid hits the player, the conditional is true. Otherwise, it is false.
  if distance < 40:
    return True
  else:
    return False

# generating asteroids function with one parameter, direction, which is the direction that the asteroid is meant to go, function moves the asteroid based on this
def generate_asteroids(direction, i):
  global x
  x = 0
  while x < i:
    # makes the variable asteroid global
    global asteroid
    # generates the asteroid turtle, which is a square shape and white to be visible, and is size 0.2
    asteroid = trtl.Turtle()
    asteroid.penup()
    asteroid.speed(0)
    asteroid.hideturtle()
    asteroid.shape('square')
    asteroid.color('white')
    asteroid.turtlesize(0.2)
    # appends the corresponding direction assigned to the turtle to the list asteroid_direction, so they have the same index in different lists
    asteroid_direction.append(direction)
    # checks if the direction is left or right, then moves the asteroid to a random position on the y axis and its corresponding x axis
    # if going left then moves to the right side, if going right then moves to the left side
    if direction == "left":
      asteroidposleft = random.randrange(-150, 200, 10)
      asteroid.goto(400, asteroidposleft)
      asteroid.showturtle()
      asteroid_list.append(asteroid)
    elif direction == "right":
      asteroidposright = random.randrange(-150, 200, 10)
      asteroid.goto(-400, asteroidposright)
      asteroid.showturtle()
      asteroid_list.append(asteroid)
    x += 1

# update score function with one parameter, player, which is the player that got the score
def update_score(player):
  # makes score variables global
  global player1score, player2score
  # if player1 got the point, add 1 to their score and update the score on the side
  # else if player2 got the point, then add 1 to their score and update the score on the other side
  if player == 1:
    player1score += 1
    scorewriter1.clear()
    scorewriter1.write("Player 1 Score: " + str(player1score), align='center', font=font_setup)
  elif player == 2:
    player2score += 1
    scorewriter2.clear()
    scorewriter2.write("Player 2 Score: " + str(player2score), align='center', font=font_setup)

# title screen function
def titlescreen():
  # using screendraw turtle, write SPACE RACE
  screendraw.hideturtle()
  screendraw.pencolor('white')
  screendraw.penup()
  screendraw.goto(0, 200)
  screendraw.pendown()
  screendraw.write('SPACE RACE', False, align='center', font=['Arial', 30, 'normal'])
  screendraw.penup()
  screendraw.goto(0,0)

# player setup function
def playersetup():
  # write the timer and display 60 seconds
  counter.write("Timer: " + str(timer), align='center', font=font_setup)
  screendraw.hideturtle()
  screendraw.penup()
  screendraw.goto(0, -200)
  screendraw.pendown()
  screendraw.setheading(90)
  screendraw.forward(400)
  # move the player turtles to the starting position
  player1.hideturtle()
  player1.penup()
  player1.goto(-200, -200)
  player1.setheading(90)
  player1.showturtle()
  player2.hideturtle()
  player2.penup()
  player2.goto(200, -200)
  player2.setheading(90)
  player2.showturtle()

# player movement functions
# player 1
# moving left
def player1moveleft():
  # checks to see if the player is within the screen
  x = player1.xcor()
  if x > -400:
    player1.goto(player1.xcor() - 10, player1.ycor())
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player1):
      player1.hideturtle()
      player1.goto(-200, -200)
      player1.setheading(90)
      player1.showturtle()
  else:
    # if the player wants to go off the screen then it will print that you cannot go off the screen
    print("you cannot go off the screen.")

# moving right
def player1moveright():
  # checks to see if the player is within their side
  x = player1.xcor()
  if x < -10:
    player1.goto(player1.xcor() + 10, player1.ycor())
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player1):
      player1.hideturtle()
      player1.goto(-200, -200)
      player1.setheading(90)
      player1.showturtle()
  else:
    # if the player wants to go to the opponent's side then it will print that you cannot go to your opponent's side
    print("you cannot go to your opponent's side.")

# moving forward
def player1moveforward():
  # makes the score variable global
  global player1score
  # checks to see if the player has reached the score point
  y = player1.ycor()
  if y < 200:
    player1.goto(player1.xcor(), player1.ycor() + 10)
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player1):
      player1.hideturtle()
      player1.goto(-200, -200)
      player1.setheading(90)
      player1.showturtle()
  else:
    # if the player reaches the score point, then add a point and reset it
    player1.hideturtle()
    player1.goto(-200, -200)
    player1.setheading(90)
    player1.showturtle()
    update_score(1)

# moving down
def player1movedown():
  # checks to see if the player is within the screen
  y = player1.ycor()
  if y > -200:
    player1.goto(player1.xcor(), player1.ycor() - 10)
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player1):
      player1.hideturtle()
      player1.goto(-200, -200)
      player1.setheading(90)
      player1.showturtle()
  else:
    # if the player wants to go off the screen then it will print that you cannot go off the screen
    print("you cannot go off the screen.")

# player 2
# moving left
def player2moveleft():
  # checks to see if the player is within their side
  x = player2.xcor()
  if x > 10:
    player2.goto(player2.xcor() - 10, player2.ycor())
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player2):
      player2.hideturtle()
      player2.goto(200, -200)
      player2.setheading(90)
      player2.showturtle()
  else:
    # if the player wants to go to the opponent's side then it will print that you cannot go to your opponent's side
    print("you cannot go to your opponent's side.")

# moving right
def player2moveright():
  # checks to see if the player is within the screen
  x = player2.xcor()
  if x < 400:
    player2.goto(player2.xcor() + 10, player2.ycor())
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player2):
      player2.hideturtle()
      player2.goto(200, -200)
      player2.setheading(90)
      player2.showturtle()
  else:
    # if the player wants to go off the screen then it will print that you cannot go off the screen
    print("you cannot go off the screen.")

# moving forward
def player2moveforward():
  # makes the score variable global
  global player2score
  # checks to see if the player has reached the score point
  y = player2.ycor()
  if y < 200:
    player2.goto(player2.xcor(), player2.ycor() + 10)
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player2):
      player2.hideturtle()
      player2.goto(200, -200)
      player2.setheading(90)
      player2.showturtle()
  else:
    # if the player reaches the score point, then add a point and reset it
    player2.hideturtle()
    player2.goto(200, -200)
    player2.setheading(90)
    player2.showturtle()
    update_score(2)

# moving down
def player2movedown():
  # checks to see if the player is within the screen
  y = player2.ycor()
  if y > -200:
    player2.goto(player2.xcor(), player2.ycor() - 10)
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player2):
      player2.hideturtle()
      player2.goto(200, -200)
      player2.setheading(90)
      player2.showturtle()
  else:
    # if the player wants to go off the screen then it will print that you cannot go off the screen
    print("you cannot go off the screen.")

# shows the title screen for 5 seconds before clearing it
titlescreen()
time.sleep(5)
screendraw.clear()
# runs the asteroids through the screen to prevent the players from moving straight for the score point easily in the beginning, moves the asteroids 6 times
i = 0
while i < 6:
  # generates 3 asteroids on either side per iteration
  generate_asteroids("left", 3)
  generate_asteroids("right", 3)
  # iterates through the asteroids in asteroid list and moves them
  for asteroids in asteroid_list:
    index = asteroid_list.index(asteroids)
    # checks the corresponding index that was appended to asteroid_direction and moves the asteroid accordingly at a random number of pixels
    if asteroid_direction[index] == "left":
      asteroids.goto(asteroids.xcor() - random.randrange(75, 100, 5), asteroids.ycor())
    elif asteroid_direction[index] == "right":
      asteroids.goto(asteroids.xcor() + random.randrange(75, 100, 5), asteroids.ycor())
  i += 1

# sets up the player
playersetup()

# keypress commands, player 1 is controlled by WASD and player 2 is controlled by the arrow keys
wn.onkeypress(player1moveforward, 'w')
wn.onkeypress(player1moveleft, 'a')
wn.onkeypress(player1movedown, 's')
wn.onkeypress(player1moveright, 'd')
wn.onkeypress(player2moveforward, 'Up')
wn.onkeypress(player2moveleft, 'Left')
wn.onkeypress(player2movedown, 'Down')
wn.onkeypress(player2moveright, 'Right')
wn.listen()
# starts the timer based on counter_interval, which is 1000 milliseconds or 1 second, and runs function countdown
wn.ontimer(countdown, counter_interval)

# while the timer is still running, keep moving the asteroids
while timer_up == False:
  # generates 2 asteroids on either side per iteration
  generate_asteroids("left", 2)
  generate_asteroids("right", 2)
  # iterates through the asteroids in asteroid list and moves them
  for asteroids in asteroid_list:
    index = asteroid_list.index(asteroids)
    # checks the corresponding index that was appended to asteroid_direction and moves the asteroid accordingly at a random number of pixels
    if asteroid_direction[index] == "left":
      asteroids.goto(asteroids.xcor() - random.randrange(75, 100, 5), asteroids.ycor())
    elif asteroid_direction[index] == "right":
      asteroids.goto(asteroids.xcor() + random.randrange(75, 100, 5), asteroids.ycor())
    # checks for a collision between player and asteroid, if a collision occurs then reset the player
    if isCollision(asteroids, player1):
      player1.hideturtle()
      player1.goto(-200, -200)
      player1.setheading(90)
      player1.showturtle()
    elif isCollision(asteroids, player2):
      player2.hideturtle()
      player2.goto(200, -200)
      player2.setheading(90)
      player2.showturtle()
    # checks to see if the asteroids have gone off-screen, if so then hide them and delete them from the list
    if asteroids.xcor() > 400 or asteroids.xcor() < -400:
      asteroids.hideturtle()
      asteroid_list.pop(index)
      asteroid_direction.pop(index)

wn.mainloop()

