import unittest

from src.ui.app import *


class AppTest(unittest.TestCase):

    # testing if index is calling or not
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # testing if search is calling or not
    def test_search(self):
        tester = app.test_client(self)
        response = tester.get('/#search', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # testing if gallery is calling or not
    def test_gallery(self):
        tester = app.test_client(self)
        response = tester.get('/#gallery', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # testing if team is calling or not
    def test_team(self):
        tester = app.test_client(self)
        response = tester.get('/#team', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # testing if citation is calling or not
    def test_citation(self):
        tester = app.test_client(self)
        response = tester.get('/#citation', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # testing if animal names is calling or not
    def test_animal_names(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'All', response.data)
        self.assertIn(b'PANDA', response.data)
        self.assertIn(b'TIGER', response.data)
        self.assertIn(b'LION', response.data)

    # testing if team data is calling or not
    def test_team_data(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertIn(b'Jinal', response.data)
        self.assertIn(b'Akhil', response.data)
        self.assertIn(b'Ankit', response.data)


if __name__ == "__main__":
    unittest.main()
