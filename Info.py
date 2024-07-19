width, height = 1600, 800
white = (126, 247, 247)
red = (255, 0, 0)
blue = (0,0,255)
black = (0,0,0)
center_x,center_y = 1550,700
red_dot_center_x, red_dot_center_y = 50, 50
red_dot_center_x2, red_dot_center_y2 = 100, 600
angle_interval = [0.1, 1.9 * 3.14159]
change_angle = [-0.1, 0.1]
epsilon = 0.0000001
simulation = 2
speed = 200


def get_width_height(simulation):
    if simulation !=8:
        return (width, height)
    
    else:
        return (height,height)

def get_step_count(simulation):
    step_count = 400
    if simulation == 1:
        return 2*step_count
    elif simulation == 2:
        return 2*step_count
    elif simulation == 5 or simulation == 3:
        return 3*step_count
    elif simulation == 4:
        return 2*step_count
    elif simulation == 6 or simulation == 7 :
        return step_count//2
    elif simulation == 8:
        return step_count//4
    else:
        return step_count


def get_step_add(simulation):
    steps_add = 10
    if simulation == 1 or simulation == 2 or simulation == 3 or simulation == 4:
        return 0
    elif simulation == 6 or simulation == 7:
        return steps_add
    elif simulation == 8:
        return steps_add*5
    else:
        return 0
    
def get_population(simulation):
    population_number = 400
    if simulation ==8:
        return population_number*5
    return population_number


def get_max_sample(simulation):
    if simulation ==8:
        return get_population(simulation)//100
    else:
        return get_population(simulation)//10

def get_wall_size(simulation):
    return (12, height-200)

def get_wall_position(simulation):
    if simulation == 1 or simulation == 2:
        return (1000, 400)
    elif simulation == 3 or simulation == 4 or simulation == 5 or simulation == 6 or simulation == 7:
        return (1400,500)

    else:
        return (0,0)

def get_red_dot_position(simulation):
    if simulation == 1 or simulation == 2 or simulation == 3 or simulation == 7:
        return (50,50)
    elif simulation == 4 or simulation == 5 or simulation == 6:
        return (100,700)
    elif simulation == 8:
        return (50,50)
    else:
        return (red_dot_center_x, red_dot_center_y)
    

def get_center_dots(simulation):
    if simulation != 8:
        return (center_x,center_y)
    else :
        return (750,750)