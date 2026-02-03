# Reborg's world

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
#-----------------------------------------      

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()

    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    if wall_in_front() and right_is_clear():
        turn_right()
    if wall_in_front() and not right_is_clear():
        turn_left()
    if front_is_clear():
        move()

    