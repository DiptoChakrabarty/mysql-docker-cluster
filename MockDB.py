from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode
from mock import patch
import utils

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
    
