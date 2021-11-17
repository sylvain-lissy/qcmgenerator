# import necessary packages

import sys
import flask
sys.path.insert(1, 'qcmgenerator/prod/')
import controller as ctrl


# create the flask app

app = flask.Flask(__name__)

app.config["DEBUG"] = True

@app.route('/qcm', methods=['GET'])
def qcmString():
   return str(qcm())

def qcm():
   theme='theme'
   nbQuestions=6
   return ctrl.getQCM(theme, nbQuestions)

@app.route('/question', methods=['GET'])
def getQuestionsQCM():
   myqcm=qcm()
   texte=""
   for question in ctrl.getQuestions(myqcm):
      texte=texte+str(question)+"////"
   return texte


@app.route('/addqcm', methods=['GET','POST'])
def addQCM():
   nom='nom'
   theme='theme'
   nombreQuestion=23
   questions='1,2,3,4,5,6'
   return ctrl.addQCM(nom, theme, nombreQuestion, questions)

@app.route('/addquestion', methods=['GET','POST'])
def addQuestion():
   question='question'
   reponse=['rep1', 'rep2', 'rep3', 'rep4']
   index=1
   theme='theme'
   return ctrl.addQuestion(question, reponse, index, theme)


# run the app

app.run()
