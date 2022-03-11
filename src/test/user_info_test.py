import unittest

from src.ui.user_info import user_details


class UserInfoTest(unittest.TestCase):
    # diclaring variables (actual and expected from test)
    global actual_dictionary, expected_dictionary
    actual_dictionary = user_details()
    expected_dictionary = {'Jinal': ['Leader'], 'Akhil': ['Python Developer'], 'Ankit': ['WebScrapper'],
                           'Chirag': ['Data Engineer'],
                           'Chaitali': ['ML Developer'], 'Ravi': ['Data Modeler'], 'Suchith': ['Data Modeler'],
                           'Celeste': ['Data Engineer'], 'Misha': ['Data Analyst'],
                           'Krutika': ['Data Engineer'],
                           'Prakshi': ['Data Engineer'], 'Prateek': ['UI Developer']}

    # testing length of dictionary
    def test_len_of_dictionary(self):
        self.assertAlmostEqual(len(actual_dictionary), 12)

    # testing if there is none keys exist
    def test_none_keys(self):
        self.assertIsNotNone(actual_dictionary.keys())
        self.assertAlmostEqual(len(actual_dictionary.keys()), 12)

    # testing if there is none values exist
    def test_none_values(self):
        self.assertIsNotNone(actual_dictionary.values())
        self.assertAlmostEqual(len(actual_dictionary.values()), 12)


    # testing dictionary data
    def test_dictionary_data(self):
        self.assertDictEqual(actual_dictionary, expected_dictionary)


if __name__ == "__main__":
    unittest.main()