from QCM import *
from Question import *
import interactBDD as bdd


# use that function if u want to return a qcm
# in order to play a qcm
def getQCM(theme, nbQuestions = 10):
   json = bdd.getQCMs(theme, nbQuestions)
   qcm = constructQCMobject(json)
   return qcm #object qcm


def getAllQCMs():
   json = bdd.getAllQCMs(theme, nbQuestions)
   return json

def getQuestions(qcm):
   listeQuestions=[] # list of question's object
   #print(qcm.listeQuestions)
   for index in qcm.listeQuestions:
      #print(index)
      question = bdd.getQuestions(index)
      #print(question)
      array= question.split(':')
      # question reponses index theme
      listeQuestions.append(Question(array[1], array[2:6], array[6], [array[7]])) 
   return listeQuestions

def addQCM(nom, theme, nombreQuestion, questions):
   return bdd.addQCM(nom, theme, nombreQuestion, questions)

def addQuestion(question, reponse, index, theme):
   #question = Question(question, reponse, index, theme)
   return bdd.addQuestion(question, reponse, index, theme)

# i assume the number of reponsesDonnees is equal to len(listeQuestions)
def correctQCM(qcmName, reponsesDonnees):
   qcm = getQCMbyName(qcmName) # get the qcm we just achieved
   questions = getQuestions(qcm)
   correction = ""
   score=0
   for i in range (0,len(qcm.listeQuestions)):
      wasCorrect = questions[i].index==reponsesDonnees[i] # we compare them
      if (wasCorrect):
         score+=1
         correction = correction + "Félicitation, la réponse est correcte. {} : {}\n".format(questions[i].question, questions[i].reponses[index-1])
      else:
         correction = correction + "Désolé, cette question là n'a pas été réussie... {} : {}\n".format(questions[i].question, questions[i].reponses[index-1])
   correction = correction + "Vous avez obtenu un score de {} sur {}".format(score, len(qcm.listeQuestions))
   return correction

# we want a precise qcm to be returned
# in order to verify the answers given are correct or not
def getQCMbyName(name):
   json = bdd.getQCMbyName(name)
   qcm = constructQCMobject(json)
   return qcm

# returns a qcm object with the given json
def constructQCMobject(json):
   array = json.split(':')
   listeQuestions=array[4].split(',')
   qcm = QCM(theme, nbQuestions, name)
   for question in listeQuestions:
      qcm.addQuestion(int(question))
   return qcm

#qcm=getQCM('monsieur beaugosse', 2)
#listeQuestions=getQuestions(qcm)

#for question in listeQuestions:
#   print(question)


