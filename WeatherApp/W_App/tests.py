from django.test import TestCase
from models import City
from models import Meta
from apps import WAppConfig

import unittest

class TempUnitTest(unittest.TestCase):

    def test_City(self): 
        
        self.assertRaises(ValueError, City, None)

    def test_Meta(self): 

        self.assertRaises(ValueError, IndexError, None)

    def test_WAppConfig(self):

        self.assertRaises(ValueError, IndexError, None)
    
unittest.main()