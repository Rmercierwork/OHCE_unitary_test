import datetime
import unittest
import datetime

from main import OHCE

class TestOHCE(unittest.TestCase):
    def setUp(self):
        self.ohce = OHCE()
        #self.ohce._now = datetime.datetime.now()

    def test_greeting(self):
        # Test pour l'heure du matin
        self.ohce.set_time("2023-02-26 08:00:00")
        self.assertEqual(self.ohce.greeting(), "Bonjour, vous vous levez tôt")
        # Test pour l'heure de midi
        self.ohce.set_time("2023-02-26 12:00:00")
        self.assertEqual(self.ohce.greeting(), "Bonjour")
        # Test pour l'heure de l'après-midi
        self.ohce.set_time("2023-02-26 17:00:00")
        self.assertEqual(self.ohce.greeting(), "Bonsoir, ne travaillez pas trop longtemps")
        # Test pour l'heure du soir
        self.ohce.set_time("2023-02-26 23:00:00")
        self.assertEqual(self.ohce.greeting(), "Vous êtes toujours réveillé ? Pensez à aller dormir")

    def test_is_palindrome(self):
        # Test avec un palindrome
        self.assertTrue(self.ohce.is_palindrome("ressasser"))
        # Test avec un non-palindrome
        self.assertFalse(self.ohce.is_palindrome("Bonjour"))

    def test_reverse_text(self):
        # Test avec un texte simple
        self.assertEqual(self.ohce.reverse_text("hello"), "olleh")
        # Test avec un texte comprenant des espaces
        self.assertEqual(self.ohce.reverse_text("hello world"), "dlrow olleh")

    def test_goodbye(self):
        # Test pour l'heure du matin
        self.ohce.set_time("2023-02-26 08:00:00")
        self.assertEqual(self.ohce.goodbye(), "Bonne journée")
        # Test pour l'heure de midi
        self.ohce.set_time("2023-02-26 12:00:00")
        self.assertEqual(self.ohce.goodbye(), "Bonne après-midi")
        # Test pour l'heure de l'après-midi
        self.ohce.set_time("2023-02-26 16:00:00")
        self.assertEqual(self.ohce.goodbye(), "Bonne soirée")
        # Test pour l'heure du soir
        self.ohce.set_time("2023-02-26 23:00:00")
        self.assertEqual(self.ohce.goodbye(), "Bonne nuit. Vous allez enfin dormir :)")

if __name__ == 'main':
    unittest.main()