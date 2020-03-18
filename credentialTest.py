from credential import Credentials
import unittest
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.myCred = Credentials("facebook", "Philip Njogu", "nyakinyua")

    def test_Init_(self):
        self.assertEqual(self.myCred.account, "facebook")
        self.assertEqual(self.myCred.user_name, "Philip Njogu")
        self.assertEqual(self.myCred.pass_word, "nyakinyua")
    def tearDown(self):
        Credentials.creden_list = []
    def test_save_credentials(self):
        self.myCred.saveCred()
        test_cred = Credentials("facebook", "Philip Njogu", "nyakinyua")
        test_cred.saveCred()
        self.assertEqual(len(Credentials.creden_list),2)

    def test_displayCredentials(self):
        self.assertEqual(Credentials.displayCredentials(), Credentials.creden_list)
    
   
    
if __name__ == "__main__":
    unittest.main()
