from QCM import *
from Question import *
import interactBDD as bdd

def getQCM(theme, nbQuestions = 10):
   json = bdd.getQCMs(theme, nbQuestions)
   #print(json)
   array = json.split(':')
   #print(array)
   listeQuestions=array[4].split(',')
   qcm = QCM(theme, nbQuestions, array[1], listeQuestions)
   return qcm #object qcm


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


#qcm=getQCM('monsieur beaugosse', 2)
#listeQuestions=getQuestions(qcm)

#for question in listeQuestions:
#   print(question)
