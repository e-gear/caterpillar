from datetime import datetime
import turtle as t
import time
import random
from tkinter import messagebox, simpledialog, Tk

t.bgcolor('black')

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('red')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()
caterpillar_online = True

leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)
leaf_online = True

game_started = False
text_turtle = t.Turtle()
text_turtle.color('white')
text_turtle.write('press SPACE to start', align='center', font=('arial', 16, 'bold'))
text_turtle.hideturtle()
start_1 = True

darkmode = True

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.color('white')
score_turtle.speed(0)
start_2 = True


def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpillar.pos()
    outside = \
        x < left_wall or \
        x > right_wall or \
        y < bottom_wall or \
        y > top_wall
    return outside


def game_over():
    if darkmode == False:
        caterpillar.color('yellow')
        leaf.color('yellow')
        text_turtle.penup()
        text_turtle.hideturtle()
        text_turtle.write('GAME OVER! press space to restart', align='center', font=('pixel', 30, 'normal'))
    else:
        caterpillar.color('black')
        leaf.color('black')
        t.hideturtle()
        t.color('white')
        t.write('GAME OVER! press space to restart', align='center', font=('pixel', 30, 'normal'))

def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='center', font=('arial', 40, 'normal'))


def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200, 200))
    leaf.sety(random.randint(-200, 200))
    leaf.st()

def pause():
    stop_game()
    text_turtle.write('you are paused. please press u to unpause', align='center', font=('arial', 16, 'bold'))
    paused = True

def darkmode():
    darkmode = True
    t.bgcolor('black')
    text_turtle.color('white')
    text_turtle.write('press SPACE to start', align='center', font=('arial', 16, 'bold'))
    text_turtle.hideturtle()
    score_turtle.color('white')

def lightmode():
    darkmode = False
    t.bgcolor('yellow')
    text_turtle.color('black')
    text_turtle.write('press SPACE to start', align='center', font=('arial', 16, 'bold'))
    text_turtle.hideturtle()
    score_turtle.color('black')

def stop_game():
        if game_started == True:
            print("")
            #caterpillar_speed = 0

def monster():
    monster1 = t.Turtle()
    monster2 = t.Turtle()
    monster3 = t.Turtle()
    monster4 = t.Turtle()
    monster5 = t.Turtle()
    monster6 = t.Turtle()
    monster7 = t.Turtle()
    monster1.speed(0)
    monster2.speed(0)
    monster3.speed(0)
    monster4.speed(0)
    monster5.speed(0)
    monster6.speed(0)
    monster7.speed(0)
    monster1.color('grey')
    monster2.color('grey')
    monster3.color('grey')
    monster4.color('grey')
    monster5.color('grey')
    monster6.color('grey')
    monster7.color('grey')
    monster1.penup()
    monster2.penup()
    monster3.penup()
    monster4.penup()
    monster5.penup()
    monster6.penup()
    monster7.penup()
    monster1.setx(random.randint(0, 300))
    monster2.setx(random.randint(0, 300))
    monster3.setx(random.randint(0, 300))
    monster4.setx(random.randint(0, 300))
    monster5.setx(random.randint(0, 300))
    monster6.setx(random.randint(0, 300))
    monster7.setx(random.randint(0, 300))
    monster1.sety(random.randint(0, 300))
    monster2.sety(random.randint(0, 300))
    monster3.sety(random.randint(0, 300))
    monster4.sety(random.randint(0, 300))
    monster5.sety(random.randint(0, 300))
    monster6.sety(random.randint(0, 300))
    monster7.sety(random.randint(0, 300))
    monster1.forward()
    monster2.forward()
    monster3.forward()
    monster4.forward()
    monster5.forward()
    monster6.forward()
    monster7.forward()

def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    # re-initialise all turtles like what happens at begining, put in a new initialise func to reuse
    #t.pendown()
    #caterpillar.setpos(0,0)from datetime import datetime, timedelta
    #t.showturtle()

    score = 0
    text_turtle.clear()
    start_3 = True

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    seconds = 1

    if start_1 == True: 
        if start_2 == True: 
            if start_3 == True:
                print('''
                    loading.
                    loading..
                    loading...
                    loading.
                    loading..
                    loading...

                    start up complete
                    connection to Lepidopteran server established
                    starting boot
                    ''')


                if caterpillar_online == True:
                    print('''
                    caterpilar online
                          ''')

                if leaf_online == True:
                    print('''
                    leaf online
                          ''')
                if caterpillar_online == False:
                    print('''
                    caterpilar offline
                          ''')
                    
                if leaf_online == False:
                    print('''
                    leaf offline
                          ''')
                print('''
                    caterpillar test: started
                    caterpillar test: sucsessful
                    leaf test: started
                    leaf test: sucsessful

                    boot sucsessful



                ''')

    #print("before set position")
    #caterpillar.setposition(0,0)
     
    start = datetime.now()
    leaves_collected = 0
    monster()
         
    while True:
        caterpillar.forward(caterpillar_speed)
        caterpillar_healthy()
        #if pause == True:
        #    caterpillar.speed(0)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            leaves_collected = leaves_collected + 1
            caterpillar_length = caterpillar_length + 1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_started = False
            game_over()
            print('caterpillar unhealthy :(')
            seconds = datetime.now() - start
            #seconds = 10
            print('you survived for ', seconds, 'seconds!')
            print('you gathed', leaves_collected, 'leaves!')
            break

def restart_game():
    if game_started == True:
            caterpillar.speed()

def caterpillar_healthy():
    print('caterpillar healthy :)')

def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)


def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)


def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)


def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

t.onkey(start_game, 'space')
t.onkeypress(pause, 'p')
t.onkey(restart_game, 'u')
t.onkey(darkmode, 'r')
t.onkey(lightmode, 'l')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkeypress(pause, 'z')
t.onkey(restart_game, 'a')
t.onkey(darkmode, 'r')
t.onkey(lightmode, 'w')
t.onkey(move_up, 'e')
t.onkey(move_right, 'f')
t.onkey(move_down, 'd')
t.onkey(move_left, 's')
t.listen()
t.mainloop()
