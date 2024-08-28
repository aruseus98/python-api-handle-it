import unittest
import json
from application.application import Application
from machine.machine import Machine

class TestApplication(unittest.TestCase):
    def test_liste_application_ok(self):
        contenu_liste = Application.liste()
        self.assertEqual(contenu_liste,'Liste des applications')

    def test_add_application(self):
        add_app = Application.add(('ma_super_liste',1))
        self.assertEqual(add_app,'Application ajoutée')

if __name__ == "__main__":
    unittest.main()
