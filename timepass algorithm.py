# -*- coding: cp1254 -*-
import time

import random

info = """welcome to contest!..

pls answer question as quick as possible you can

pls enter small letter...\n"""

print(info)

questions = {"2 * 2 ?":"4",
"what is the capital city of turkey?":"ankara",

"what is the king of jungle?":"lion",

"what is the meaning of book in turkish language?":"kitap",

"who is the foundation of turkish government":"atatürk",

"what is the most popular drink in turkey?":"raki",

"pls tell us a hero as comic":"temel"}

correct = 0

wrong = 0

blank = 0

current_time = time.time() #system time

allowed_time = 25 #total time to reply the question 


for i in random.sample(list(questions), 5):

     question = questions[i]

     if time.time() < current_time+allowed_time:

         answer = input("1. soru --> {} : ".format(i))

     if answer == question:

         correct += 1

     elif answer == "":

         blank += 1

     else:

         wrong += 1

print()

print("right answer  :", correct)

print("wrong answer :", wrong)

print("blank answer :", blank)
