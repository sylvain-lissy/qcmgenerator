class QCM:

    def __init__(self, theme, nombreQuestions=10, nom=None):
        self.__theme=theme
        
        self.__nombreQuestions=nombreQuestions
        
        if (nom==None):
            self.__nom=theme
        else:
            self.__nom= nom
            
        self.__listeQuestions= self.findQuestions(theme, nombreQuestions)


    def findQuestions(self, theme, nombreQuestions):
        return []


    @property
    def theme(self):
        return self.__theme
    @property
    def nombreQuestions(self):
        return self.__nombreQuestions
    @property
    def listeQuestions(self):
        return self.__listeQuestions
    @property
    def nom(self):
        return self.__nom

    @theme.setter
    def setTheme(self, theme):
        self.__theme=theme
        
    @nombreQuestions.setter
    def setNombreQuestions(self, nombreQuestions):
        self.__nombreQuestions=nombreQuestions
        
    @listeQuestions.setter
    def setListeQuestions(self, listeQuestions):
        self.__listeQuestions=listeQuestions
        
    @nom.setter
    def setNom(self, nom):
        self.__nom=nom


    def __str__(self):
        return self.__nom+":"+self.__theme+":"+str(self.__nombreQuestions)+":"+self.questionToString()

    def addQuestion(self, idQuestion):
        self.__listeQuestions.append(idQuestion)

    def questionToString(self):
        string=""
        for i in self.__listeQuestions:
            if string=="":
                string=str(i)
            else:
                string=string+","+str(i)
        return string
        

test=QCM("bonjour")
test2=QCM("bonjour2",20)
test3=QCM("bonjour3",30,"camembert")
print(test)
print(test2)
print(test3)
test3.addQuestion(5)
test3.addQuestion(7)
test3.addQuestion(9)
print(test3)
