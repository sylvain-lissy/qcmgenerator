# import necessary packages

import sys
from flask import Flask, render_template
sys.path.insert(1, 'prod/')
import controller as ctrl


# create the flask app

app = flask.Flask(__name__)

app.config["DEBUG"] = True

# the route to show a complete qcm
# parameters: str theme and int nbQuestions
# returns a qcm object as string
@app.route('/qcm', methods=['GET'])
def qcmString():
   return str(qcm())


# the controller returns a qcm object
# having the theme and the number of questions asked
# parameters: str theme and int nbQuestions
def qcm():
   theme='theme'
   nbQuestions=6
   return ctrl.getQCM(theme, nbQuestions)

# the route to show questions from a qcm
# returns a string containing the questions objects as string
# separated by "////"
@app.route('/question', methods=['GET'])
def getQuestionsQCM():
   myqcm=qcm()
   texte=""
   for question in ctrl.getQuestions(myqcm):
      texte=texte+str(question)+"////"
   return texte 

# the route to add a qcm
# parameters: str nom, str theme, int nombreQuestion, str questions
# asks the controller to create a new entry in the database
# this entry is a qcm with the parameters specified
@app.route('/addqcm', methods=['GET','POST'])
def addQCM():
   nom='nom'
   theme='theme'
   nombreQuestion=23
   questions='1,2,3,4,5,6'
   return ctrl.addQCM(nom, theme, nombreQuestion, questions)

# the route to add a question
# parameters: str question, array[str] reponse, int index, str theme
# asks the controller to create a new entry in the database
# this entry is a question with the parameters specified
@app.route('/addquestion', methods=['GET','POST'])
def addQuestion():
   question='question'
   reponse=['rep1', 'rep2', 'rep3', 'rep4']
   index=1
   theme='theme'
   return ctrl.addQuestion(question, reponse, index, theme)

# the route to correct a qcm
# parameters: str qcmName, str reponsesDonnees
# u must specify the qcm name in order to get the answers and compare to the given answers
# returns a string containing the answers and the score 
@app.route('/correction', methods=['GET','POST'])
def correctQCM():
   qcmName="nomDuQCM" # requires unique names to be specified
   reponsesDonnees='1,2,3,4,1,2,3,4' # we cannot randomize the order of the questions given because we dont have the questions id here
   # this means i cant reorder them to make correspond the answer given and the question
   # in the case it is randomized
   return ctrl.correctQCM(qcmID, reponsesDonnees)

# the route to show all the available qcm
# returns a string containing all the qcm
# TODO: specify a parameter to have a minimal number of questions
@app.route('/allQCMs', methods=['POST'])
def getAllQCMs():
   return ctrl.getAllQCMs()

# the route to show a qcm selectionned by his name
# parameters: str qcmName
# returns a string containing the qcm
@app.route('/qcmByName', methods=['POST'])
def getAllQCMs():
   qcmName="nomDuQCM"
   return ctrl.getQCMbyName(qcmName)


# run the app

app.run()
