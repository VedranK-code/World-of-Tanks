import turtle
import time
import random

delay = 0.1

#Score
score_p1 = 0
score_p2 = 0
wn = turtle.Screen()
wn.title("WoT")
wn.bgpic("mapa.gif")
wn.setup(width=1000, height=1000)
wn.tracer(0) #gasi updejtiranje ekrana
wn.register_shape('explosion.gif')

#tenk

tenk = turtle.Turtle()
tenk.speed(0)
wn.register_shape('tenkdole.gif')
tenk.shape("tenkdole.gif")
tenk.color("black")
tenk.penup()
tenk.goto(-400,400)
tenk.direction = "stop"

#neprijatelj

enemy = turtle.Turtle()
enemy.speed(0)
wn.register_shape('enemygore.gif')
enemy.shape("enemygore.gif")
enemy.color("black")
enemy.penup()
enemy.goto(400,-400)
enemy.direction = "stop"

#olovka
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,450)
pen.write("Player_1: 0       Player_2: 0", align="center", font=("Courier", 24, "normal"))

wn.register_shape('tenkgore.gif')
wn.register_shape('tenklevo.gif')
wn.register_shape('tenkdesno.gif')

tenkspeed=30

#raketa

wn.register_shape('raketagore.gif')
rocket = turtle.Turtle()
rocket.shape("raketagore.gif")
rocket.penup()
rocket.speed(0)
rocket.setheading(90)
rocket.hideturtle()

rocketspeed = 50

rocketstate = "ready"


#raketa 2

wn.register_shape('p2raketagore.gif')
rocket2 = turtle.Turtle()
rocket2.shape("p2raketagore.gif")
rocket2.penup()
rocket2.speed(0)
rocket2.setheading(90)
rocket2.hideturtle()

rocket2speed = 50

rocket2state = "ready"

#micanje tenka

def move_up():
    y = tenk.ycor()
    y += tenkspeed
    tenk.sety(y)
    tenk.shape("tenkgore.gif")
    tenk.direction = "up"
      

def move_down():
    y = tenk.ycor()
    y -= tenkspeed
    tenk.sety(y)
    tenk.shape("tenkdole.gif")
    tenk.direction = "down"
        
    
def move_left():
    x = tenk.xcor()
    x -= tenkspeed
    tenk.setx(x)
    tenk.shape("tenklevo.gif")
    tenk.direction = "left"
        
    
def move_right():
    x = tenk.xcor()
    x += tenkspeed
    tenk.setx(x)
    tenk.shape("tenkdesno.gif")
    tenk.direction = "right"
        
    
#micanje neprijatelja
    
wn.register_shape('enemydole.gif')
wn.register_shape('enemylevo.gif')
wn.register_shape('enemydesno.gif')

def p2_move_up():
    y = enemy.ycor()
    y += tenkspeed
    enemy.sety(y)
    enemy.shape("enemygore.gif")
    enemy.direction = "up"
    
def p2_move_down():
    y = enemy.ycor()
    y -= tenkspeed
    enemy.sety(y)
    enemy.shape("enemydole.gif")
    enemy.direction = "down"
    
def p2_move_left():
    x = enemy.xcor()
    x -= tenkspeed
    enemy.setx(x)
    enemy.shape("enemylevo.gif")
    enemy.direction = "left"
    
def p2_move_right():
    x = enemy.xcor()
    x += tenkspeed
    enemy.setx(x)
    enemy.shape("enemydesno.gif")
    enemy.direction = "right"
    
wn.register_shape('raketadesno.gif')
wn.register_shape('raketalevo.gif')
wn.register_shape('raketadole.gif')

wn.register_shape('p2raketadesno.gif')
wn.register_shape('p2raketalevo.gif')
wn.register_shape('p2raketadole.gif')

#funkcija pucanje 1

def fire_rocket():
    
	#deklariranje stanja rakete
    
	global rocketstate
	if rocketstate == "ready":
		rocketstate = "fire"
		

def ferit():	#pomicanje metka iznad glave tenka
    if (tenk.direction == "up"):
        x = tenk.xcor()
        y = tenk.ycor() + 20
        rocket.setposition(x, y)
        rocket.showturtle()
        rocket.setheading(90)
        rocket.shape("raketagore.gif")
        
    if tenk.direction == "down":
        x = tenk.xcor()
        y = tenk.ycor() - 20
        rocket.setposition(x, y)
        rocket.showturtle()
        rocket.setheading(270)
        rocket.shape("raketadole.gif")
        
    if tenk.direction == "left":
        x = tenk.xcor() - 20
        y = tenk.ycor() 
        rocket.setposition(x, y)
        rocket.showturtle()
        rocket.setheading(180)
        rocket.shape("raketalevo.gif")

    if tenk.direction == "right":
        x = tenk.xcor() + 20
        y = tenk.ycor() 
        rocket.setposition(x, y)
        rocket.showturtle()
        rocket.setheading(0)
        rocket.shape("raketadesno.gif")
        
def move_rocket():
    
	#pomicanje metka
	if (rocketstate == "fire") and (tenk.direction == "up"):
		y = rocket.ycor()
		y += rocketspeed
		rocket.sety(y)

	elif (rocketstate == "fire") and (tenk.direction == "down"):
		y = rocket.ycor()
		y -= rocketspeed
		rocket.sety(y)
		
	elif (rocketstate == "fire") and (tenk.direction == "left"):
		x = rocket.xcor()
		x -= rocketspeed
		rocket.setx(x)
		
	elif (rocketstate == "fire") and (tenk.direction == "right"):
		x = rocket.xcor()
		x += rocketspeed
		rocket.setx(x)
		
def reset_rocket():
    
	#granice metka 1
    
	if rocket.ycor() > 495:
		rocket.hideturtle()
		rocketstate = "ready"
		
	if rocket.ycor() < -495:
		rocket.hideturtle()
		rocketstate = "ready"
		
	if rocket.xcor() > 495:
		rocket.hideturtle()
		rocketstate = "ready"

	if rocket.xcor() < -495:
		rocket.hideturtle()
		rocketstate = "ready"

#funkcija pucanje 2

def fire_rocket2():
    
	#deklariranje stanja rakete 2
    
	global rocket2state
	if rocket2state == "ready":
		rocket2state = "fire"
		

def ferit2():	#pomicanje metka iznad glave tenka 2
    if enemy.direction == "up":
        x = enemy.xcor()
        y = enemy.ycor() + 20
        rocket2.setposition(x, y)
        rocket2.showturtle()
        rocket2.setheading(90)
        rocket2.shape("p2raketagore.gif")
        
    if enemy.direction == "down":
        x = enemy.xcor()
        y = enemy.ycor() - 20
        rocket2.setposition(x, y)
        rocket2.showturtle()
        rocket2.setheading(270)
        rocket2.shape("p2raketadole.gif")
        
    if enemy.direction == "left":
        x = enemy.xcor() - 20
        y = enemy.ycor() 
        rocket2.setposition(x, y)
        rocket2.showturtle()
        rocket2.setheading(180)
        rocket2.shape("p2raketalevo.gif")

    if enemy.direction == "right":
        x = enemy.xcor() + 20
        y = enemy.ycor() 
        rocket2.setposition(x, y)
        rocket2.showturtle()
        rocket2.setheading(0)
        rocket2.shape("p2raketadesno.gif")
        
def move_rocket2():
    
	#pomicanje metka 2
	if (rocket2state == "fire") and (enemy.direction == "up"):
		y = rocket2.ycor()
		y += rocket2speed
		rocket2.sety(y)

	if (rocket2state == "fire") and (enemy.direction == "down"):
		y = rocket2.ycor()
		y -= rocket2speed
		rocket2.sety(y)
		
	if (rocket2state == "fire") and (enemy.direction == "left"):
		x = rocket2.xcor()
		x -= rocket2speed
		rocket2.setx(x)
		
	if (rocket2state == "fire") and (enemy.direction == "right"):
		x = rocket2.xcor()
		x += rocket2speed
		rocket2.setx(x)
		
def reset_rocket2():
    
	#granice metka 2
    
	if rocket2.ycor() > 495:
		rocket2.hideturtle()
		rocket2state = "ready"
		
	if rocket2.ycor() < -495:
		rocket2.hideturtle()
		rocket2state = "ready"
		
	if rocket2.xcor() > 495:
		rocket2.hideturtle()
		rocket2state = "ready"

	if rocket2.xcor() < -495:
		rocket2.hideturtle()
		rocket2state = "ready"

		
#spajanje tipkovinice s akcijama u igri

wn.listen()

wn.onkeypress(move_up, "w")
wn.onkeypress(move_down, "s")
wn.onkeypress(move_left, "a")
wn.onkeypress(move_right, "d")
wn.onkeypress(ferit, "f")

wn.onkeypress(p2_move_up, "Up")
wn.onkeypress(p2_move_down, "Down")
wn.onkeypress(p2_move_left, "Left")
wn.onkeypress(p2_move_right, "Right")
wn.onkeypress(ferit2, "p")

#glavni krug igre

while True:

	
    wn.update()

    #provjera udaranja u zid
    if tenk.xcor()>500 or tenk.xcor()<-500 or tenk.ycor()>500 or tenk.ycor()<-500:
        time.sleep(1)
        tenk.goto(-400,400)
        tenk.direction = "stop"
        tenk.shape("tenkdole.gif")

    if enemy.xcor()>500 or enemy.xcor()<-500 or enemy.ycor()>500 or enemy.ycor()<-500:
        time.sleep(1)
        enemy.goto(-400,400)
        enemy.direction = "stop"
        enemy.shape("enemygore.gif")
        
    #updejtanje score-a 1
    pen.clear()
    pen.write("Player_1: {}         Player_2: {}".format(score_p1, score_p2), align="center", font=("Courier", 24, "normal"))

    #provjera spajanja s raktom
        
    if tenk.distance(rocket2) < 30:
        rocket2.goto(550,550)
        delay = 1
        time.sleep(delay)
        tenk.goto(-400,400)
        enemy.goto(400,-400)
        score_p2 += 10      
        delay = 0.1
        time.sleep(delay)
        tenk.shape("tenkdole.gif")
        enemy.shape("enemygore.gif")
        
    #provjera spajanja s raketom

    if enemy.distance(rocket) < 30:
        rocket.goto(550,550)
        delay = 1
        time.sleep(delay)
        enemy.goto(400,-400)
        tenk.goto(-400,400)
        score_p1 += 10
        delay = 0.1
        time.sleep(delay)
        enemy.shape("enemygore.gif")
        tenk.shape("tenkdole.gif")
        
    fire_rocket()
    
    move_rocket()
    
    reset_rocket()
    
    fire_rocket2()
    
    move_rocket2()
    
    reset_rocket2()
    
    time.sleep(delay)



wn.mainloop()

