import unittest

from src.ui.user_info import *


class UserInfoTest(unittest.TestCase):
    def testing(self):
        expected_dict = {'Jinal': ['Leader'], 'Akhil': ['Python Developer'], 'Ankit': ['WebScrapper'],
                      'Chirag': ['Data Engineer'],
                      'Chaitali': ['ML Developer'], 'Ravi': ['Data Modeler'], 'Suchith': ['Data Modeler'],
                      'Celeste': ['Data Engineer'], 'Misha': ['Data Analyst'], 'Krutika': ['Data Engineer'],
                      'Prakshi': ['Data Engineer'], 'Prateek': ['UI Developer']}
        actual_dictionary = user_details()
        self.assertAlmostEqual(len(actual_dictionary), 12)
        self.assertAlmostEqual(len(actual_dictionary.keys()), 12)
        self.assertAlmostEqual(len(actual_dictionary.values()), 12)
        self.assertAlmostEqual(actual_dictionary.get('Jinal'),['Leader'])
        self.assertDictEqual(actual_dictionary, expected_dict)


if __name__ == "__main__":
    unittest.main()
