# Reeborg's World
# Hurdle 1 code


#Method 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for i in range(6):
    jump()


#Method 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


no_of_strip = 6
while no_of_strip > 0:
    jump()
    no_of_strip -= 1


# Hurdle 2 code
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_right()
    move()
    turn_right()
    move()


def by_pass():
    move()
    turn_left()
    jump()
    turn_left()
    move()
    turn_left()
    jump()
    turn_left()
    move()
    turn_left()
    jump()
    turn_left()
    move()
    turn_left()
    jump()


while at_goal() == False:
    by_pass()

# Hurdle 3 code


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while True:
    if not wall_in_front() and not at_goal():
        move()
    elif not at_goal():
        jump()

    else:
        break


#method 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()

    else:
        move()
