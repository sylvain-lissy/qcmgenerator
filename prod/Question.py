class Question(object):
    id=0    

    def __init__(self, question, reponses, index, themes):
        self._themes= themes
        self._index=index
        self._question=question
        self._reponses=reponses
        self.__class__.id=self.__class__.id+1

    
    @property
    def question(self):
        return self._question

    @property
    def index(self):
        return self._index

    @property
    def reponses(self):
        return self._reponses

    @property
    def themes(self):
        return self._themes

    
    @question.setter
    def question(self, question):
        self._question=question

    @index.setter
    def index(self, index):
        self._index=index

    @reponses.setter
    def reponses(self, reponses):
        self._reponses=reponses

    @themes.setter
    def themes(self, themes):
        self._themes = themes
        

    def __str__(self):
        return self._question+":"+self.reponsesToString()+":"+str(self._index)+":"+self.themesToString()

    def reponsesToString(self):
        string=""
        for i in self._reponses:
            if string=="":
                string=str(i)
            else:
                string=string+","+str(i)
        return string
 
    def themesToString(self):
        string=""
        for i in self._themes:
            if string=="":
                string=str(i)
            else:
                string=string+","+str(i)
        return string

