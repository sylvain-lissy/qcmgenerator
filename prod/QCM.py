class QCM:

    def __init__(self, theme, nombreQuestions=10, nom=None):
        self.__theme=theme
        self.__nombreQuestions=10
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

test=QCM("bonjour")
print(test)
