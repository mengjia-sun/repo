#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import itertools
import pandas as pd
import random


a = 1
b = 6
c = 3
d = 2
e = 4
f = 5
g = 6
h = 2
i = 5
j = 2
k = 1
l = 3
m = 4
n = 5
o = 3
p = 5
q = 1
r = 1
s = 3



TN = 10

tplist = [('a', 'b', 'c'), ('a', 'd', 'h'), ('a', 'e', 'j'), ('b', 'e', 'i'), ('b', 'f', 'k'), ('c', 'f', 'j'), ('d', 'i', 'n'), ('d', 'e', 'f'), ('e', 'i', 'm'), ('e', 'f', 'g'), ('e', 'j', 'o'), ('f', 'j', 'n'), ('f', 'k', 'p'), ('g', 'k', 'o'), ('h', 'i', 'j'), ('h', 'm', 'q'), ('i', 'n', 'r'), ('i', 'j', 'k'), ('j', 'k', 'l'), ('j', 'n', 'q'), ('j', 'o', 's'), ('k', 'o', 'r'), ('l', 'p', 's'), ('m', 'n', 'o'), ('n', 'o', 'p'), ('q', 'r', 's'), ('c', 'g', 'l')]




st.title("Memory Magic: Hexagon Time!")

st.write('Welcome to Memory Magic: Hexagon Time! Below you will see a hexagon with 19 numeric values. You will mesmorize as many of them as you can, as you will try to sum them to a certain value. Once you are ready, proceed to the next page. A countdown timer will begin, and you will have 1 minute to enter you answer.') 

from PIL import Image
st.image(Image.open('123.jpg'))



st.button('I am ready, let the game start!')



st.image(Image.open('ABC.jpg'))

count = 0
wintotal = 2

letters = st.text_input("Enter a sequence of 3 letters (e.g., abc): ").lower()

if st.button("Check Combo"):
    if len(letters) == 3:
        # Generate and print all permutations of the entered 3 letters
        permutations = itertools.permutations(letters)
        # intialize flag
        flag = False
        for combo in permutations:
            for i in range(len(tplist)):
                if tplist[i] == combo:

                    flag = True
                    if eval(combo[0]) + eval(combo[1]) + eval(combo[2]) == TN:
                        ANSWER = True
                        count += 1
                    else:
                        ANSWER = False 
                        count -=1
                    if ANSWER == True:
                        st.write('You are correct! Your score is', count)
                    else:
                        st.write('WRONG! Your score is', count)
        if flag == False:
            st.write('Not a possible combo')
    else:
        st.write("Please enter exactly 3 letters.")

if count < 0:
    print("Automatic Loss!")
elif count == wintotal:
    print("You win! Your score is now", count)

# Get the letters from the user
letters = input("Enter a sequence of 3 letters (e.g., abc): ")

if len(letters) == 3:
    # Generate and print all permutations of the entered 3 letters
    permutations = itertools.permutations(letters)
    # intialize flag
    flag = False
    for combo in permutations:
        for i in range(len(tplist)):
            if tplist[i] == combo:
                flag = True
                if eval(combo[0]) + eval(combo[1]) + eval(combo[2]) == TN:
                    ANSWER = True
                else:
                    ANSWER = False
                if ANSWER == True:
                    print('You are correct!')
                else:
                    print('WRONG!')
    if flag == False:
        print('Not a possible combo')
else:
    print("Please enter exactly 3 letters.")
