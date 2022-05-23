import requests
import time
from time import sleep

team = ""
current_question = ""
answered = False
question_id = 0

team = input("Please enter the team you are playing on \n 1) AI \n 2) Human \n")

team.lower()
if team == "AI" or team == 1:
  team = 1
if team == "human" or team == 2:
  team = 2

def getQuestion():
  response = requests.get('https://turing.wotanutt.repl.co/getquestion')
  try:
    if question_id != response.json()["question_id"]:
      if current_question == response.json()["question"] or response.json()["question"] == "no question found":
        return
      else:
        return "A new question has arrived: " + response.json()["question"] + " "
    else:
      pass
  except:
    return f"An error occured, please yell for Sam for more information \nError returned from the server:  {response.status_code}"

def postQuestion(answer):
  res = requests.post('https://turing.wotanutt.repl.co/postquestion', json={"answer":answer, "team":team,"question_id":question_id})
  if res.status_code != 200:
    return res.status_code
  else:
    return 200

running = True

while running != False:
  if getQuestion() == None:
    pass
  elif current_question != getQuestion():
    current_question = getQuestion()
    postQuestion(input(current_question))
  else:
    pass
  sleep(10)
