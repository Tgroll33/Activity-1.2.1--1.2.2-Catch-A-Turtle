#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb
#colors and configs
color = "red"
shape = "square"
pen = 3
score = 0

#-----countdown variables-----
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")
turt = trtl.Turtle()
turt.pensize(pen)
turt.shape(shape)
turt.color(color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pencolor(color)
score_writer.penup()
score_writer.goto(-100,-100)
score_writer.pendown()

#-----countdown writer-----
counter = trtl.Turtle()
counter.hideturtle()
counter.pencolor(color)
counter.penup()
counter.goto(-100,-150)
counter.pendown()

#-----game functions-----
def spot_clicked(x,y):

    global timer 
    if timer > 0:
        update_score()
        change_position()
    else:
        turt.hideturtle()

def change_position():
    turt.hideturtle()
    newxpos = rand.randint(0,200)
    newypos = rand.randint(0,125)
    turt.penup()
    turt.goto(newxpos,newypos)
    turt.pendown()
    turt.showturtle()

def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font = font_setup)     

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, turt, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, turt, score)

#---------events---------
turt.onclick(spot_clicked)

wn = trtl.Screen()
wn.bgcolor("yellow")
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
