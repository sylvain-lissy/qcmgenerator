import mariadb
import json

config = {
    'host': 'mariadb-service',
    'port': 3306,
    'user': 'root',
    'password': 'pwd',
    'database': 'data'
}

#_____________________________________________GET_____________________________________________________
def getAllQCMs():
    request = "select * from qcm;"
    description = connectAndExecuteRequest(request)
    return extractAllQCMData(description)

def getQCMs(theme, nbQuestions = 10):
    request = "select * from qcm where theme = '{}';".format(theme)
# TODO ne renvoyer que le premier qui a le theme et le nombre de questions requis
    description = connectAndExecuteRequest(request)
    return extractQCMData(description)

def getQCMbyName(name):
    request = "select * from qcm where nom = '{}';".format(name)
    description = connectAndExecuteRequest(request)
    return extractQCMData(description)

def connectAndExecuteRequest(request):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute(request)
    
    description=cur
    conn.close
    return description



def getQuestions(id):
    request = "select id, question, rep1, rep2, rep3, rep4, numero, themes from question where id = {}".format(id)
    description = connectAndExecuteRequest(request)
    return extractQuestionsData(description)


#__________________________________________ ADD _______________________________________________

def addQuestion(question, reponse, numero, theme):
   conn = mariadb.connect(**config)
   cur = conn.cursor()
   cur.execute("SELECT MAX(id) FROM question;")
   for elem in cur:
      maxIndex=elem[0]
   index = 1 + maxIndex
   a=str(index)
   b=question
   c=reponse[0]
   d=reponse[1]
   e=reponse[2]
   f=reponse[3]
   g=numero
   h=theme
   try:
      cur.execute("insert into question values('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}');".format(a, b, c, d, e, f, g, h))
      conn.commit()
   except:
      conn.rollback()
   conn.close
   return "insert into question values('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}');".format(a, b, c, d, e, f, g, h)

def addQCM(nom, theme, nombreQuestion, questions):
   conn = mariadb.connect(**config)
   cur = conn.cursor()
   cur.execute("SELECT MAX(id) FROM qcm;")
   for elem in cur:
      maxIndex=elem[0]
   index = 1 + maxIndex

   # we must verify the given name is not already in the database
   # otherwise [as the id(index) is unique] we set it as "nomindex"
   cur.execute("SELECT EXISTS(SELECT * FROM qcm WHERE nom= '{}');".format(nom))
   for elem in cur:
      existence=elem[0]==1
      # true if elem[0] equals 1(true)
      # and false if elem[0] equals 0(false)
   if (existence): # name already exists
       nom=nom+str(index)
      
   try:
      cur.execute("insert into qcm values({}, '{}', '{}', {}, '{}');".format(index, nom, theme, nombreQuestion, questions))
      conn.commit()
   except:
      conn.rollback() # annulation des changements dans le cas où ça a foiré pour garder l'intégrité de la bdd
   conn.close
   return "insert into qcm values({}, '{}', '{}', {}, '{}');".format(index, nom, theme, nombreQuestion, questions)


#____________________________________request into json ________________________


def extractQuestionsData(questionCur):
    texte=""
    for elem in questionCur:
         texte=texte+"{}".format(elem[0])
         texte=texte+" : {}".format(elem[1])
         texte=texte+" : {}".format(elem[2])
         texte=texte+" : {}".format(elem[3])
         texte=texte+" : {}".format(elem[4])
         texte=texte+" : {}".format(elem[5])
         texte=texte+" : {}".format(elem[6])
         texte=texte+" : {}".format(elem[7])
    return texte

def extractQCMData(description):
    texte=""
    # return the results!
    
    for elem in description:
         texte=""+str(elem[0])
         texte=texte+':'+elem[1]
         texte=texte+':'+elem[2]
         texte=texte+':'+str(elem[3])
         texte=texte+':'+elem[4]
    return texte


def extractAllQCMData(description):
    texte=""
    # return the results!
    
    for elem in description:
         texte=""+str(elem[0])
         texte=texte+':'+elem[1]
         texte=texte+':'+elem[2]
         texte=texte+':'+str(elem[3])
         texte=texte+':'+elem[4]
         texte=texte+"\n"
    return texte
