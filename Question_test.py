from prod.Question import Question
import unittest

class Question_test(unittest.TestCase):


    def test_init(self):
        test= Question("ça va?", ["oui", "non"], 0, ["bien être", "coucou"])
        
        self.assertEqual(test.themes,["bien être", "coucou"])
        self.assertEqual(test.index,0)
        self.assertEqual(test.reponses,["oui", "non"])
        self.assertEqual(test.question,"ça va?")

        
if __name__ == '__main__':
    unittest.main()



