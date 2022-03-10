import unittest

from src.ui.user_info import *


class UserInfoTest(unittest.TestCase):
    def testing(self):
        dictionary = {'Jinal': ['Leader'], 'Akhil': ['Python Developer'], 'Ankit': ['WebScrapper'],
                      'Chirag': ['Data Engineer'],
                      'Chaitali': ['ML Developer'], 'Ravi': ['Data Modeler'], 'Suchith': ['Data Modeler'],
                      'Celeste': ['Data Engineer'], 'Misha': ['Data Analyst'], 'Krutika': ['Data Engineer'],
                      'Prakshi': ['Data Engineer'], 'Prateek': ['UI Developer']}
        self.assertAlmostEqual(len(user_details()), 12)
        self.assertIsNotNone(user_details().keys())
        self.assertIsNotNone(user_details().values())
        self.assertDictEqual(user_details(), dictionary)


if __name__ == "__main__":
    unittest.main()
