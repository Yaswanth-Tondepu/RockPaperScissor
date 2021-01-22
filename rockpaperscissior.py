from random import randint
import streamlit as st

options = ["Rock", "Paper", "Scissors"]

def gamePlay(playerChoice):
    player = playerChoice
    computer = options[randint(0,2)]
    if player == computer:
        st.write("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            st.write("You lose!", computer, "covers", player)
        else:
            st.write("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            st.write("You lose!", computer, "cut", player)
        else:
            st.write("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            st.write("You lose...", computer, "smashes", player)
        else:
            st.write("You win!", player, "cut", computer)
    if player != False:
        st.write("You chose: ",player)
        st.write("Computer chose: ",computer)
    
player = False
st.write("Choose one option!")
if st.button('Rock'):
    player = 'Rock'  
if st.button('Paper'):
    player = 'Paper'  
if st.button('Scissors'):
    player = 'Scissors'
gamePlay(player)