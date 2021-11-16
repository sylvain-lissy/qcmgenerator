import mariadb
import json

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'pwd',
    'database': 'data'
}

#_____________________________________________GET_____________________________________________________
def getQCMs(theme, nbQuestions = 10):
    conn = mariadb.connect(**config)
    cur = conn.cursor()
    cur.execute("select * from qcm where theme = '{}';".format(theme)) 
# TODO ne renvoyer que le premier qui a le theme et le nombre de questions requis

    description=cur
    conn.close

    texte=""
    # return the results!
    
    for elem in description:
         texte=""+str(elem[0])
         texte=texte+':'+elem[1]
         texte=texte+':'+elem[2]
         texte=texte+':'+str(elem[3])
         texte=texte+':'+elem[4]
    return texte


def getQuestions(id):
    # connection for MariaDB
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
   
    # execute a SQL statement
    cur.execute("select id, question, rep1, rep2, rep3, rep4, numero, themes from question where id = {}".format(id))
    description=cur
    conn.close

    # return the results!
    return extractQuestionsData(description)

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
   return "insert into question values('{}', '{}', '{}', '{}', '{}', '{}', {}, '{}');".format(a, b, c, d, e, f, g, h))

def addQCM(nom, theme, nombreQuestion, questions):
   conn = mariadb.connect(**config)
   cur = conn.cursor()
   cur.execute("SELECT MAX(id) FROM qcm;")
   for elem in cur:
      maxIndex=elem[0]
   index = 1 + maxIndex
   try:
      cur.execute("insert into qcm values({}, '{}', '{}', {}, '{}');".format(index, nom, theme, nombreQuestion, questions))
      conn.commit()
   except:
      conn.rollback()
   conn.close
   return "insert into qcm values({}, '{}', '{}', {}, '{}');".format(index, nom, theme, nombreQuestion, questions)




