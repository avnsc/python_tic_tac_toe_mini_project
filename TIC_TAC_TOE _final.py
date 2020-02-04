#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    a=board
    print("\n\n\n")
    print("           | "+"       | ")
    print("    "+a[0]+"      |"+"    "+a[1]+"   |     "+a[2])
    print("           | "+"       | ")
    print("---------------------------------")
    print("           | "+"       | ")
    print("    "+a[3]+"      |"+"    "+a[4]+"   |     "+a[5])
    print("           | "+"       | ")
    print("---------------------------------")
    print("           | "+"       | ")
    print("    "+a[6]+"      |"+"    "+a[7]+"   |     "+a[8])
    print("           | "+"       | ")


# In[2]:


def player_input():
    while(True):
        x=input("Please pick a marker 'X' or 'O' : ")
        if x == 'X' or x == 'O':
            return x
        else:
            pass


# In[3]:


def place_marker(board, marker, position):
    mark1 = str(marker)
    posi = int(position)
    board[posi] = mark1


# In[4]:


def win_check(board, mark):
    a = board
    mark1 = str(mark)
    c=0
    if a[c] == a[c+1] == a[c+2] and a[c] != "b" and a[c+1] != "b" and a[c+2] != "b":   #1st row
        if a[c] == mark1:
                return True
        else:
                return False
    elif a[c+3] == a[c+4] == a[c+5] and a[c+3] != "b" and a[c+4] != "b" and a[c+5] != "b":  #2nd row
        if a[c+3] == mark1:
                return True
        else:
                return False
    elif a[c+6] == a[c+7] == a[c+8] and a[c+6] != "b" and a[c+7] != "b" and a[c+8] != "b":  #3rd row
        if a[c+6] == mark1:
                return True
        else:
                return False
    elif a[c] == a[c+4] == a[c+8] and a[c] != "b" and a[c+4] != "b" and a[c+8] != "b":   #left to right diagonal
        if a[c] == mark1:
                return True
        else:
                return False
    elif a[c+2] == a[c+4] == a[c+6] and a[c+2] != "b" and a[c+4] != "b" and a[c+6] != "b":  #right to left diagonal
        if a[c+2] == mark1:
                return True
        else:
                return False
    if a[c] == a[c+3] == a[c+6] and a[c] != "b" and a[c+3] != "b" and a[c+6] != "b":   #1st column
        if a[c] == mark1:
                return True
        else:
                return False
    if a[c+1] == a[c+4] == a[c+7] and a[c+1] != "b" and a[c+4] != "b" and a[c+7] != "b":   #2nd column
        if a[c+1] == mark1:
                return True
        else:
                return False
    if a[c+2] == a[c+5] == a[c+8] and a[c+2] != "b" and a[c+5] != "b" and a[c+8] != "b":   #3rd column
        if a[c+2] == mark1:
                return True
        else:
                return False


# In[5]:


import random
def choose_first():
    a = random.randint(1,2)
    return(a)


# In[6]:


def space_check(board,position):
    a = board
    posi = int(position)
    if a[posi] == "b":
        return True
    else:
        return False


# In[7]:


def full_board_check(board):
    for i in board:
        if i != "b":
            pass
        else:
            return False
    return True


# In[8]:


#this section was developed dealing next next next lvl horrible errors -_-
#it includes while loop bcoz, when a function doesn't get the required input, then we call it again till we get 
#right ouput. When we finally get the right output, then the return statement becomes invalid as it returns the
#position to previous function which doesn't take any input. Thus, this creates problem in main function
def player_choice(board):
    c=0
    while c == 0:
        position = input('Please enter a position between 0 and 8: ')
        posi = int(position)
        if posi>=0 and posi<=8:
            a = space_check(board,position)
            if a is True:
                c+=1
            else:
                print("repeated input !!!")
            if c == 1:
                return posi
        else:
            print("invalid input !!!")
            pass


# In[9]:


def replay():
    a=input("Do you want to play again? choose Y or N: ")
    if a == "Y":
        return True
    elif a == "N":
        return False
    else:
        replay()


# In[ ]:


while True:
    print("Welcome to Tic Tac Toe !")
    rev=0   #rev counter : it revokes the game 
    from IPython.display import clear_output
    test_board = ['b','b','b','b','b','b','b','b','b']
    display_board(test_board)
    p1 = choose_first()         # p1 is player 1's designation
    print("player {} has to play first".format(p1))
    q1 = player_input()         #q1 is player 1's choice          
    print("player {} has choosen ".format(p1) + "{}".format(q1))
    if p1 == 1:
        p2 = 2
    elif p1 == 2:
        p2 = 1                # p2 is player 2's designation
    if q1 == "X":              
        q2 = "O"
    elif q1 == "O":             #q2 is player 2's choice
        q2 = "X"
    print("player {} has choosen ".format(p2) + "{}".format(q2))
    while rev!=1:           # game starts here
        a1 = full_board_check(test_board)
        if a1 is False:
            print("player {} turn".format(p1))
            pos = player_choice(test_board)  #player 1 selecting a position
            place_marker(test_board,q1,pos)
            display_board(test_board)
            if win_check(test_board,q1):
                print("player {} ".format(p1) + "has won the game!!!")
                rev+=1
                break
            else:
                a1 = full_board_check(test_board)
                if a1 is False:
                    print("player {} turn".format(p2))
                    pos = player_choice(test_board)  #player 2 selection a position
                    place_marker(test_board,q2,pos)
                    display_board(test_board)
                    res = win_check(test_board,q2)
                    if win_check(test_board,q1):
                        print("player {} ".format(p2) + "has won the game!!!")
                        rev+=1
                        break
                else:
                    pass
        else:
            rev+=1
            print("GAME TIED !!!")
    eval = replay()
    if eval is True:
        print("\n\n")
        pass
    else:
        print("GAME OVER !!!")
        break


# In[ ]:






#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_board(board):
    a=board
    print("\n\n\n")
    print("           | "+"       | ")
    print("    "+a[0]+"      |"+"    "+a[1]+"   |     "+a[2])
    print("           | "+"       | ")
    print("---------------------------------")
    print("           | "+"       | ")
    print("    "+a[3]+"      |"+"    "+a[4]+"   |     "+a[5])
    print("           | "+"       | ")
    print("---------------------------------")
    print("           | "+"       | ")
    print("    "+a[6]+"      |"+"    "+a[7]+"   |     "+a[8])
    print("           | "+"       | ")


# In[2]:


def player_input():
    while(True):
        x=input("Please pick a marker 'X' or 'O' : ")
        if x == 'X' or x == 'O':
            return x
        else:
            pass


# In[3]:


def place_marker(board, marker, position):
    mark1 = str(marker)
    posi = int(position)
    board[posi] = mark1


# In[4]:


def win_check(board, mark):
    a = board
    mark1 = str(mark)
    c=0
    if a[c] == a[c+1] == a[c+2] and a[c] != "b" and a[c+1] != "b" and a[c+2] != "b":   #1st row
        if a[c] == mark1:
                return True
        else:
                return False
    elif a[c+3] == a[c+4] == a[c+5] and a[c+3] != "b" and a[c+4] != "b" and a[c+5] != "b":  #2nd row
        if a[c+3] == mark1:
                return True
        else:
                return False
    elif a[c+6] == a[c+7] == a[c+8] and a[c+6] != "b" and a[c+7] != "b" and a[c+8] != "b":  #3rd row
        if a[c+6] == mark1:
                return True
        else:
                return False
    elif a[c] == a[c+4] == a[c+8] and a[c] != "b" and a[c+4] != "b" and a[c+8] != "b":   #left to right diagonal
        if a[c] == mark1:
                return True
        else:
                return False
    elif a[c+2] == a[c+4] == a[c+6] and a[c+2] != "b" and a[c+4] != "b" and a[c+6] != "b":  #right to left diagonal
        if a[c+2] == mark1:
                return True
        else:
                return False
    if a[c] == a[c+3] == a[c+6] and a[c] != "b" and a[c+3] != "b" and a[c+6] != "b":   #1st column
        if a[c] == mark1:
                return True
        else:
                return False
    if a[c+1] == a[c+4] == a[c+7] and a[c+1] != "b" and a[c+4] != "b" and a[c+7] != "b":   #2nd column
        if a[c+1] == mark1:
                return True
        else:
                return False
    if a[c+2] == a[c+5] == a[c+8] and a[c+2] != "b" and a[c+5] != "b" and a[c+8] != "b":   #3rd column
        if a[c+2] == mark1:
                return True
        else:
                return False


# In[5]:


import random
def choose_first():
    a = random.randint(1,2)
    return(a)


# In[6]:


def space_check(board,position):
    a = board
    posi = int(position)
    if a[posi] == "b":
        return True
    else:
        return False


# In[7]:


def full_board_check(board):
    for i in board:
        if i != "b":
            pass
        else:
            return False
    return True


# In[8]:


#this section was developed dealing next next next lvl horrible errors -_-
#it includes while loop bcoz, when a function doesn't get the required input, then we call it again till we get 
#right ouput. When we finally get the right output, then the return statement becomes invalid as it returns the
#position to previous function which doesn't take any input. Thus, this creates problem in main function
def player_choice(board):
    c=0
    while c == 0:
        position = input('Please enter a position between 0 and 8: ')
        posi = int(position)
        if posi>=0 and posi<=8:
            a = space_check(board,position)
            if a is True:
                c+=1
            else:
                print("repeated input !!!")
            if c == 1:
                return posi
        else:
            print("invalid input !!!")
            pass


# In[9]:


def replay():
    a=input("Do you want to play again? choose Y or N: ")
    if a == "Y":
        return True
    elif a == "N":
        return False
    else:
        replay()


# In[ ]:


while True:
    print("Welcome to Tic Tac Toe !")
    rev=0   #rev counter : it revokes the game 
    from IPython.display import clear_output
    test_board = ['b','b','b','b','b','b','b','b','b']
    display_board(test_board)
    p1 = choose_first()         # p1 is player 1's designation
    print("player {} has to play first".format(p1))
    q1 = player_input()         #q1 is player 1's choice          
    print("player {} has choosen ".format(p1) + "{}".format(q1))
    if p1 == 1:
        p2 = 2
    elif p1 == 2:
        p2 = 1                # p2 is player 2's designation
    if q1 == "X":              
        q2 = "O"
    elif q1 == "O":             #q2 is player 2's choice
        q2 = "X"
    print("player {} has choosen ".format(p2) + "{}".format(q2))
    while rev!=1:           # game starts here
        a1 = full_board_check(test_board)
        if a1 is False:
            print("player {} turn".format(p1))
            pos = player_choice(test_board)  #player 1 selecting a position
            place_marker(test_board,q1,pos)
            display_board(test_board)
            if win_check(test_board,q1):
                print("player {} ".format(p1) + "has won the game!!!")
                rev+=1
                break
            else:
                a1 = full_board_check(test_board)
                if a1 is False:
                    print("player {} turn".format(p2))
                    pos = player_choice(test_board)  #player 2 selection a position
                    place_marker(test_board,q2,pos)
                    display_board(test_board)
                    res = win_check(test_board,q2)
                    if win_check(test_board,q1):
                        print("player {} ".format(p2) + "has won the game!!!")
                        rev+=1
                        break
                else:
                    pass
        else:
            rev+=1
            print("GAME TIED !!!")
    eval = replay()
    if eval is True:
        print("\n\n")
        pass
    else:
        print("GAME OVER !!!")
        break


# In[ ]:







# In[ ]:





# In[ ]:




