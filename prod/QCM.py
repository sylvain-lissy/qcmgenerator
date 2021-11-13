class QCM(object):

    def __init__(self, theme, nombreQuestions=10, nom=None, listeQuestions=None):
        self._theme=theme

        self._nombreQuestions=nombreQuestions

        if (nom==None):
            self._nom=theme
        else:
            self._nom= nom

        self._listeQuestions = listeQuestions
        #self._listeQuestions= self.findQuestions(theme, nombreQuestions)


    #def findQuestions(self, theme, nombreQuestions):
        #return []


    @property
    def theme(self):
        return self._theme
    @property
    def nombreQuestions(self):
        return self._nombreQuestions
    @property
    def listeQuestions(self):
        return self._listeQuestions
    @property
    def nom(self):
        return self._nom

    @theme.setter
    def theme(self, theme):
        self._theme=str(theme)
        
    @nombreQuestions.setter
    def nombreQuestions(self, nombreQuestions):
        self._nombreQuestions=nombreQuestions

    @listeQuestions.setter
    def listeQuestion(self, listeQuestions):
        self._listeQuestions=listeQuestions
        
    @nom.setter
    def nom(self, nom):
        self._nom=nom

# inutile en fait
#    def __equals__(self, qcm):
#        if(self.__nom!=qcm.nom): return false
#        if(self.__theme!=qcm.theme): return false
#        if(self.__nombreQuestions!=qcm.nombreQuestions): return false
#        if(len(self.__listeQuestions)!=len(qcm.listeQuestions)): return false
#        if(self.__listeQuestions.sort()!=qcm.listeQuestions.sort()): return false
        

    def __str__(self):
        return self._nom+":"+self._theme+":"+str(self._nombreQuestions)+":"+self.questionToString()

    def addQuestion(self, idQuestion):
        self._listeQuestions.append(idQuestion)

    def questionToString(self):
        string=""
        for i in self._listeQuestions:
            if string=="":
                string=str(i)
            else:
                string=string+","+str(i)
        return string
        

