from user import User
import unittest
class TestUser(unittest.TestCase):
    def setUp(self):
        self.myUser= User("Philip", "12345678")
    def test__init__(self):
        self.assertEqual(self.myUser.username, "Philip")
        self.assertEqual(self.myUser.password,"12345678")
    def tearDown(self):
        User.users = []
    def test_save_user(self):
        self.myUser.saveUser()
        test_user = User("Philip", "0727856217")
        test_user.saveUser()
        self.assertEqual(len(User.users),2)
    def test_display_users(self):
        self.assertEqual(User.displayUsers(),User.users)
        


    

if __name__ == "__main__":
    unittest.main()

