from prod.QCM import QCM
import unittest

class QCM_test(unittest.TestCase):


    def test_init(self):
        test=QCM("bonjour",30,"camembert")
        
        self.assertEqual(test.theme,"bonjour")
        self.assertEqual(test.nom,"camembert")
        self.assertEqual(len(test.listeQuestions),0)
        self.assertEqual(test.nombreQuestions,30)
        


    def test_addquestion(self):
        test3=QCM("bonjour3",30,"camembert")
        test3.addQuestion(15)
        test3.addQuestion(17)
        test3.addQuestion(19)
        self.assertEqual(test3.listeQuestions,[15,17,19])

    def test_setters(self):
        test=QCM("bonjour")
        test.theme="theme"
        test.nom="nom"
        self.assertEqual(test.nombreQuestions,10)
        test.nombreQuestions=24
        test.listeQuestion=[11,12,13]
        
        self.assertEqual(test.theme,"theme")
        self.assertEqual(test.nom,"nom")
        self.assertEqual(test.nombreQuestions,24)
        self.assertEqual(test.listeQuestions,[11,12,13])
        
    def test_str(self):
        test=QCM("bonjour")
        test.theme="theme"
        test.nom="nom"
        test.nombreQuestions=24
        test.listeQuestion=[11,12,13]

        self.assertEqual(str(test), "nom:theme:24:11,12,13")

        
if __name__ == '__main__':
    unittest.main()



