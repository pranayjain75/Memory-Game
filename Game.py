#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import random
import time

NUM_ROWS = 2
NUM_COLS = 2

if(NUM_ROWS*NUM_COLS % 2!=0):
    raise ValueError("There must be even number of spots")
HIDDEN_CARD = "#"
EMPTY_SPOT = " "
DELAY = 2 #Time in seconds cards are revealed for 


# In[2]:


def clear():
    os.system("cls" if os.name=="nt" else "clear")


# In[3]:


def print_title():
    print(r"""
___  ___                                  _____                      
|  \/  |                                 |  __ \                     
| .  . | ___ _ __ ___   ___  _ __ _   _  | |  \/ __ _ _ __ ___   ___ 
| |\/| |/ _ \ '_ ` _ \ / _ \| '__| | | | | | __ / _` | '_ ` _ \ / _ \
| |  | |  __/ | | | | | (_) | |  | |_| | | |_\ \ (_| | | | | | |  __/
\_|  |_/\___|_| |_| |_|\___/|_|   \__, |  \____/\__,_|_| |_| |_|\___|
                                   __/ |                             
                                  |___/                              
""")


# In[4]:


def print_instructions():
    print("Uncover two cards which you think contain the same symbol")
    print("Try to find all the pairs in the minimum number of turns")
    print()   


# In[5]:


def play_again():
    print()
    print("Would you like to play again?(Yes or No)?")
    return input().lower().startswith("y")


# In[6]:


def create_board():
    cards = []
    for offset in range((NUM_ROWS*NUM_COLS)//2):
        cards.append(chr(65+offset))
    cards.extend(cards)
    random.shuffle(cards)
    board = []
    for row_num in range(NUM_ROWS):
        new_row = []
        for col_num in range(NUM_COLS):
            new_row.append(cards[row_num*NUM_COLS+col_num])
        board.append(new_row)
    return board
            


# In[7]:


def display_cards(board,visible=None):
    if(visible is None):
        visible = []
    row_indices = range(NUM_ROWS)
    col_indices = range(NUM_COLS)
    print("\t",end="")
    for col_index in col_indices:
        print(col_index,end="\t")
    print()
    print("\t",end="")
    for col_index in col_indices:
        print("----",end="\t")
    print()
    for row_num in range(NUM_ROWS):
        print(row_indices[row_num],":\t",end="")
        for col_num in range(NUM_COLS):
            if((row_num,col_num) in visible):
                print(board[row_num][col_num],end="\t")   
            elif(board[row_num][col_num]==EMPTY_SPOT):
                print(EMPTY_SPOT,end="\t");
            else:
                print(HIDDEN_CARD,end="\t")
        print()
    print()


# In[8]:


def validate_user_input(player_choice,board):
    try:
        row,col = player_choice.split()
    except ValueError:
        print("You should enter two numbers separated by a space")
        return False
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("You should enter numbers only")
        return False
    if(row<0 or row>NUM_ROWS-1):
        print("The row number must be between 0 and ",NUM_ROWS-1,".",sep="")
        return False
    if(col<0 or col>NUM_COLS-1):
        print("The column number must be between 0 and ",NUM_COLS-1,".",sep="")
        return False
    if(board[row][col]== EMPTY_SPOT):
        print("That spot is Empty")
        return False
        
    return True
        


# In[9]:


def get_player_choices(board):
    player_choices = []
    valid_input = False
    while(not valid_input):
        print("Enter the Row and Column number for your FIRST choice of cards")
        player_choice = input("separated by space:")
        valid_input = validate_user_input(player_choice,board)
    row,col = player_choice.split()
    new_position = (int(row),int(col))
    player_choices.append(new_position)
    
    valid_input = False
    while(not valid_input):
        print("Enter the Row and Column number for your SECOND choice of cards")
        player_choice = input("separated by space:")
        if validate_user_input(player_choice,board):
            row,col = player_choice.split()
            new_position = (int(row),int(col))
            if(new_position not in player_choices):
                player_choices.append(new_position)
                valid_input = True
            else:
                print("Cards must be different")
    return player_choices
            
            
    
        
        
        


# In[10]:


def player_turn(board,player_score,player_turns):
    clear()
    print_title()
    print("Turns taken:",player_turns)
    print("Current_score:",player_score)
    print()
    display_cards(board)
    player_choices = get_player_choices(board)
    card1_pos, card2_pos = player_choices
    clear()
    print_title()
    print_instructions()
    print()
    print()
    display_cards(board,player_choices)
    
    symbol1 = board[card1_pos[0]][card1_pos[1]]
    symbol2 = board[card2_pos[0]][card2_pos[1]]
    if(symbol1==symbol2):
        board[card1_pos[0]][card1_pos[1]] = EMPTY_SPOT
        board[card2_pos[0]][card2_pos[1]] = EMPTY_SPOT
        player_score+=1
        print("WELL DONE")
        time.sleep(DELAY)
        return True
    time.sleep(DELAY)
    return False
    
    
    
    


# In[11]:


def main():
    lets_play_again = True
    max_score = NUM_ROWS*NUM_COLS//2
    while lets_play_again:
        # Initialize values
        board = create_board()
        player_turns = 0
        player_score = 0

        # Main Game Logic
        game_over = False
        while(not game_over):
            success = player_turn(board,player_score,player_turns)
            if(success):
                player_score+=1
            player_turns+=1
            if(player_score>=max_score):
                game_over = True
        print()
        print("COngratulations!")
        print("You completed the game in",player_turns,"turns")
        print("Your score is ",player_score,".",sep="")
        if not play_again():
            lets_play_again = False
    print("Goodbye!")
    
            
    
    print(success)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




