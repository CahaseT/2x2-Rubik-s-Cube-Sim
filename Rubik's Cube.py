

up = ["⬜", "⬜", 
      "⬜", "⬜"]
front = ["🟩", "🟩", 
         "🟩", "🟩"]
right = ["🟥", "🟥",
          "🟥", "🟥"]
left = ["🟧", "🟧",
         "🟧", "🟧"]
down = ["🟨", "🟨", 
        "🟨", "🟨"]
back = ["🟦", "🟦",
         "🟦", "🟦"]
your_turns = []
def print_cube ():
    print ("      " + up[0], up[1])
    print ("      " + up[2], up[3])
    print (left[0], left[1], front[0], front[1], right[0], right[1], back[0], back[1])
    print (left[2], left[3], front[2], front[3], right[2], right[3], back[2], back[3]) 
    print ("      " + down[0], down[1])
    print ("      " + down[2], down[3]) 
  
def save_copy ():
    old_up = up[:]
    old_front = front[:]
    old_right = right[:]
    old_left = left[:]
    old_down = down[:]
    old_back = back[:]
    return  old_up, old_front, old_right, old_left, old_down, old_back  
def R (old_up, old_front, old_right, old_left, old_down, old_back ):
    right[:] = [old_right[2], old_right[0], old_right[3], old_right[1]]
    up[:]    = [old_up[0], old_front[1], old_up[2], old_front[3]]
    front[:] = [old_front[0], old_down[1], old_front[2], old_down[3]]
    down[:]  = [old_down[0], old_back[2], old_down[2], old_back[0]]
    back[:]  = [old_up[3], old_back[1], old_up[1], old_back[3]]
def U (old_up, old_front, old_right, old_left, old_down, old_back ):
    up[:] = [old_up[2], old_up[0], old_up[3], old_up[1]]
    front[:] = [old_right[0], old_right[1], old_front[2], old_front[3]]
    right[:] = [old_back[0], old_back[1], old_right[2], old_right[3]]
    back[:] = [old_left[0], old_left[1], old_back[2], old_back[3]]
    left[:] = [old_front[0], old_front[1], old_left[2], old_left[3]]
def F (old_up, old_front, old_right, old_left, old_down, old_back ):
    front[:] = [old_front[2], old_front[0], old_front[3], old_front[1]]
    up[:] = [old_up[0], old_up[1], old_left[3], old_left[1]]
    left[:] = [old_left[0], old_down[0], old_left[2], old_down[1]]
    down[:] = [old_right[2], old_right[0], old_down[2], old_down[3]]
    right[:] = [old_up[2], old_right[1], old_up[3], old_right[3]]
def L (old_up, old_front, old_right, old_left, old_down, old_back ):
    left[:] = [old_left[2], old_left[0], old_left[3], old_left[1]]
    front[:] = [old_up[0], old_front[1], old_up[2], old_front[3]]
    up [:] = [old_back[3], old_up[1], old_back[1], old_up[3]]
    down [:] = [old_front[0], old_down[1], old_front[2], old_down[3]]
    back [:] = [old_back[0], old_down[2], old_back[2], old_down[0]]
def D (old_up, old_front, old_right, old_left, old_down, old_back ):
    down [:] = [old_down[2], old_down[0], old_down[3], old_down[1]]
    front [:] = [old_front[0], old_front[1], old_left[2], old_left[3]]
    left [:] = [old_left[0], old_left[1], old_back[2], old_back[3]]
    back [:] = [old_back[0], old_back[1], old_right[2], old_right[3]]
    right [:] = [old_right[0], old_right[1], old_front[2], old_front[3]]
def B (old_up, old_front, old_right, old_left, old_down, old_back ):
    back [:] = [old_back[2], old_back[0], old_back[3], old_back[1]]
    up [:] = [old_right[1], old_right[3], old_up[2], old_up[3]]
    right [:] = [old_right[0], old_down[3], old_right[2], old_down[2]]
    down [:] = [old_down[0], old_down[1], old_left [0], old_left[2]]
    left [:] = [old_up[1], old_left[1], old_up[0], old_left[3]]

while True:
    turn = input("What face do you want to turn? (cube notation)  ").strip().upper ()
    old_up, old_front, old_right, old_left, old_down, old_back = save_copy()

    if turn == "R":
        R(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("R")
    elif turn == "U":
        U(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("U")
    elif turn == "F":
        F(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("F")
    elif turn == "L":
        L(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("L")
    elif turn == "D":
        D(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("D")
    elif turn == "B":
        B(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("B")
    elif turn =="R2":
        R(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("R2")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        R(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "U2":
        U(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("U2")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        U(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "F2":
        F(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("F2")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        F(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "L2":
        L(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("L2")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        L(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "D2":
        D(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("D2")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        D(old_up, old_front, old_right, old_left, old_down, old_back)    
    elif turn == "B2":
        B(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("B2")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        B(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "R'":
        R(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("R'")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        R(old_up, old_front, old_right, old_left, old_down, old_back)
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        R(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "U'":
        U(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("U'")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        U(old_up, old_front, old_right, old_left, old_down, old_back)
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        U(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "F'":
        F(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("F'")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        F(old_up, old_front, old_right, old_left, old_down, old_back)
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        F(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "L'":
        L(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("L'")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        L(old_up, old_front, old_right, old_left, old_down, old_back)
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        L(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "B'":
        B(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("B'")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        B(old_up, old_front, old_right, old_left, old_down, old_back)
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        B(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "D'":
        D(old_up, old_front, old_right, old_left, old_down, old_back)
        your_turns.append ("D'")
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        D(old_up, old_front, old_right, old_left, old_down, old_back)
        old_up, old_front, old_right, old_left, old_down, old_back = save_copy()
        D(old_up, old_front, old_right, old_left, old_down, old_back)
    elif turn == "X":
        up = ["⬜", "⬜", 
             "⬜", "⬜"]
        front = ["🟩", "🟩", 
                "🟩", "🟩"]
        right = ["🟥", "🟥", 
                "🟥", "🟥"]
        left = ["🟧", "🟧",
                "🟧", "🟧"]
        down = ["🟨", "🟨", 
                "🟨", "🟨"]
        back = ["🟦", "🟦",
                "🟦", "🟦"]
    elif turn == "SCRAMBLE":
        print("coming soon")
    print_cube()
    print (your_turns)