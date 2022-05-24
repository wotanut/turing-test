from flask import Flask, jsonify, request, render_template, redirect
import json
import random

# still to do

# testing
# client does not show second response for some reason

app = Flask(__name__)

def readJson():
  """ reads the current question ID """
  f = open("question_id.json")
  data = json.load(f)
  ID = data["question_id"]
  return ID

def incrementQuestionID():
  """ Increases the question ID by 1 """
  new_value = readJson() + 1
  information = {'question_id': new_value}
  jsonString = json.dumps(information, indent=4)
  f = open("question_id.json","w")
  f.write(jsonString)
  f.close()
  return True


class question():
  def __init__(self, question, ai_response, human_response,question_id):
    self.question = question
    self.ai_response = ai_response
    self.human_response = human_response
    self.question_id = question_id

questions = []
column = "0" # this column is whatever the human is gonna be
column = random.randint(1,2)
if column == 1:
  column = "A"
else:
  column = "B"
    
@app.route("/")
def index():
  """ Home Page """
  return render_template("main.html")

@app.route("/finish")
def finish():
    """Finish Page"""
    return render_template("finish_test.html",len = len(questions), questions=questions, column=column)
  
@app.route("/newquestion", methods=["POST"])
def new():
  """ Make a new question """
  response = request.json
  questions.append(question(response['answer'],None,None,readJson()))
  incrementQuestionID()
  return jsonify(accepted="True"),200

@app.route('/getquestion')
def getquestion():
    """get the latest question"""
    try:
      latest = questions[-1].question
      return jsonify(question=latest,question_id=readJson()),200
    except:
      return jsonify(question="no question found",question_id=readJson()),200

@app.route('/postquestion', methods=["POST"])
def post_question():
  """
  change the answer for the provided question ID from None to the response
  """
  response = request.json # get the response in json format
  question_ = questions[response["question_id"]].question
  question_id = questions[response["question_id"]].question_id
  
  # checks the team 
  
  if response["team"] == "1":
    # set the AI's response
    ai_response = response["answer"]
    if questions[response["question_id"]].human_response != None:
      human_response = questions[response["question_id"]].human_response 
    else:
      human_response = None
  else:
    # set the human's response
    human_response = response["answer"]
    if questions[response["question_id"]].ai_response != None:
      ai_response = questions[response["question_id"]].ai_response
    else:
      ai_response = None

  # adds the response back to the list

  questions.remove(questions[response["question_id"]])
  questions.append(question(question_,ai_response,human_response,question_id))

  # returns 200 ok
  
  return jsonify(),200

@app.route("/whoresponded",methods=["GET"])
def whoresponded():
  """Checks who responded for the server"""
  try:
    return jsonify(human=questions[-1].human_response, AI=questions[-1].ai_response,column=column),200
  except:
    return jsonify(None),404

@app.route("/new_game",methods=["GET"])
def new_game():
  """ Creates a new game and deletes everything about the old one"""
  questions.clear()

  information = {'question_id': 0}
  jsonString = json.dumps(information, indent=4)
  f = open("question_id.json","w")
  f.write(jsonString)
  f.close()

  return redirect("/", 302)
  # redirect home

app.run(host='0.0.0.0', port=81)
