from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode, Error
from mock import patch
import utils
import main
import MySQLOperation


class MockDB(TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n Setup Class \n")
        pass
    
    @classmethod
    def tearDownClass(cls):
        print("\n Tear down \n")
        pass
    
    def setUp(self):
        print("\n Set Up \n")
        pass
    
    def tearDown(self):
        print("\n Tear Down \n")
        pass
    
    @patch('main.mysql.connector.connect', spec_set=True, autospec=True)
    def test_insert_user(self, mock_connect):
        username = "dummy"
        password = "dummy"

        mock_connect.side_effect = Error(
            errno=errorcode.ER_ACCESS_DENIED_ERROR
        )
        with self.assertRaise(False):
            with MySQLOperation(username, password):
                pass

        with self.assertEqual(True):
            with MySQLOperation(username, password):
                pass