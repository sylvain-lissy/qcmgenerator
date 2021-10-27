from prod.QCM import QCM
import unittest

class QCM_test(unittest.TestCase):


    def test_init(self):
        test=QCM("bonjour")
        test2=QCM("bonjour2",20)
        test3=QCM("bonjour3",30,"camembert")
        
        self.assertEqual(test.theme,"bonjour")
        self.assertEqual(test.nom,"bonjour")
        self.assertEqual(len(test.listeQuestions),0)
        self.assertEqual(test.nombreQuestions,10)

        self.assertEqual(test2.nombreQuestions,20)

        self.assertEqual(test3.theme,"bonjour3")
        self.assertEqual(test3.nom,"camembert")

    def test_addquestion(self):
        test3=QCM("bonjour3",30,"camembert")
        test3.addQuestion(5)
        test3.addQuestion(7)
        test3.addQuestion(9)
        self.assertEqual(test3.listeQuestions,[5,7,9])

    def test_setters(self):
        test=QCM("bonjour")
        test.theme="theme"
        test.nom="nom"
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



