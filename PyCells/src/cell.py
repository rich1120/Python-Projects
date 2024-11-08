import random
from config import *


class Cell:
    def __init__(self, logic, skin=-1, grade=0, velocity=0):
        self.logic = logic
        if skin == -1:
            self.skin = get_random(logic)
        else:
            self.skin = skin
        self.grade = grade
        self.velocity = velocity
        self.parent = None


PLACEHOLDER_CELL = Cell(PLACEHOLDER, 0)
BLANK_CELL = Cell(BLANK, 0)

G = 1  # direction of gravity

steps = 0

active_locations = set()

matrix = [None] * m
for i in range(m):
    matrix[i] = [None] * n


def get_step():
    return steps


def event(odds):
    return random.random() < odds


def coin_toss():
    return random.random() < 1


def pick_one(a, b):
    if coin_toss() < 0.5:
        return a
    else:
        return b


def invert_gravity():
    global G
    G = -G


def get_random(cell_logic):
    return (random.random() * 1000) % len(colors[cell_logic])


def set_t(key):
    nums = key.split()
    return int(nums[0]), int(nums[1])


def set_key(t):
    i, j = t
    return str(i) + " " + str(j)


def get_mod(t, table):
    try:
        i, j = t
        assert (0 <= i < m and 0 <= j < n)
        return table[set_key(t)]
    except:
        return PLACEHOLDER_CELL


def set_mod(t, table, cell):
    try:
        i, j = t
        assert (0 <= i <= m and 0 <= j < n)
        key = set_key(t)
        table[key] = cell
    except:
        pass


def init():
    global m
    global n
    global matrix
    for i in range(m):
        for j in range(n):
            matrix = Cell(BLANK, 0)


def init_cell(logic):
    cell = Cell(logic)
    if logic in FLUIDS:
        cell.velocity = pick_one(1, -1)
    return cell


def get_cell(t):
    try:
        i, j = t
        assert (0 <= i < m and 0 <= j < n)
        return matrix[i][j]
    except:
        return PLACEHOLDER_CELL


def set_cell(t, cell):
    try:
        i, j = t
        assert (0 <= i < m and 0 <= j < n)
        matrix[i][j] = cell
    except:
        pass


def insert_cell(i, j, cell):
    active_locations.add((i, j))
    set_cell((i, j), cell)


def generate(logic, i, j):
    final_spread = get_spread()
    for I in range(-final_spread + 1, final_spread):
        for J in range(-final_spread + 1, final_spread):
            cell = init_cell(logic)

            if logic == ROCK and (I + J + 2 * final_spread % 2 == 1):
                continue

            if event(SPAWN_CHANCE) or logic == BLANK:
                insert_cell(i + I, j + J, cell)

def evolve(PAUSED):
    global steps
    steps = steps + 1
    water_spread = coin_toss()
    m = {}
    changes = set()

    def blank(t):
        logic_now = get_cell(t).logic
        logic_next = get_mod(t, m).logic
        return logic_now in unconserved and logic_next == PLACEHOLDER or logic_next in unconserved

    def move(t, s):
        set_mod(s, m, get_cell(t))
        delete(t)
        changes.add(s)

    def move_and_change(t, s, nc):
        set_mod(s, m, nc)
        changes.add(s)
        delete(t)

    def place(t, cell):
        set_mod(t, m, cell)
        changes.add(t)

    def swap(t, s):
        if get_mod(t, m).logic == PLACEHOLDER:
            set_mod(t, m, get_cell(s))
            set_mod(s, m, get_cell(t))
            changes.add(t)

    def operable(t):
        return get_mod(t, m).logic == PLACEHOLDER

    def delete(t):
        set_mod(t, m, BLANK_CELL)
        
    def grow(t, s, cell):
        c = get_cell(t)
        cell.parent = c.parent
        c.parent = (t, cell.logic)
        move(t, s)
        place(t, cell)

    def mutate(t, cell):
        cell.parent = get_cell(t).parent
        place(t, cell)

    def has_parent(cell):
        return cell.parent == None or get_cell(cell.parent[0]).logic == cell.parent[1]
    
    def process():
        active_list = list(active_locations)
        random.shuffle(active_list)
        for t in active_list:
            
            changes.add(t)
            if PAUSED:
                continue

            i, j = t
            cell = get_cell(t)
            down = (i+G,j)
            down_left = (i+G,j-1)
            down_right = (i+G,j+1)
            left = (i,j-1)
            right = (i,j+1)
            up = (i-G,j)
            up_right = (i-G,j+1)
            up_left = (i-G,j-1)
            
            neighbours = [up,up_left,up_right,left,right,down,down_left,down_right]
            neighbours_close = [up,down,left,right]

            if cell.logic == SAND and operable(t):
                if blank(down):
                    move(t,down)
                elif blank(down_left) and blank(down_right):
                    move(t,pick_one(down_left,down_right))
                elif blank(down_left):
                    move(t,down_left)
                elif blank(down_right):
                    move(t,down_right)
                elif get_cell(down).logic in FLUIDS:
                    swap(t,down)

            if cell.logic in FLUIDS and operable(t) and viscosity[cell.logic]>=0:

                # check if splashing happens
                splash_positons = []
                side_flow_postions = []
                if event(viscosity[cell.logic]):
                    side_flow_postions = [left,right]
                if event(SPLASH_CHANCE[cell.logic]):
                    splash_positons = [up,up_left,up_right]
                flowable_postions = [[down,down_left,down_right],splash_positons,side_flow_postions]
                
                pos = None # final position to move to
                fp = [] # free flowable positions
                
                # compute availability of free positons
                for pos_set in flowable_postions:
                    fp_end = []
                    for p in pos_set:
                        if blank(p):
                            fp_end.append(p)
                    fp.append(fp_end)

                # pick according to priority
                double_free = False
                for pos_set_free in fp:
                    if len(pos_set_free) != 0:
                        if left in pos_set_free and right in pos_set_free:
                            double_free = True
                        pos = random.choice(pos_set_free)
                        break

                # if position chosen is opposite velocity
                if pos == left and double_free and cell.velocity == -1:
                    pos = right
                elif pos == right and double_free and cell.velocity == 1:
                    pos = left

                # reassign velocity
                if pos == left:
                    cell.velocity = 1
                elif pos == right:
                    cell.velocity = -1

                if not pos == None:
                    move(t,pos)
            
            if cell.logic == ROCK and operable(t):
                primary_supports = [left,right,up]
                auxiliary_supports = [up_left,up_right,down_left,down_right]
                ct_prime = 0
                ct_aux = 0
                for s in primary_supports:
                    if get_cell(s).logic == ROCK:
                        ct_prime=ct_prime+1
                for s in auxiliary_supports:
                    if get_cell(s).logic == ROCK:
                        ct_aux = ct_aux+1
                if ct_prime <= ROCK_PRIME_LIMIT and ct_aux <= ROCK_AUX_LIMIT:
                    if blank(down):
                        move(t,down)
                    elif get_cell(down).logic in FLUIDS:
                        swap(t,down)

        for key in m:
            t = set_t(key)
            set_cell(t,m[key])
            active_locations.add(t)

        m.clear()

    process()

    to_deactivate = set()
    for t in active_locations:
        if get_cell(t).logic == BLANK:
            to_deactivate.add(t)

    active_locations.difference_update(to_deactivate)

    return changes