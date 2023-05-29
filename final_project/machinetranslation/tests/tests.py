"""
Provides the unit test cases for translator
"""
import unittest
import json

from translator import english_to_french, french_to_english


class TestEnglishtofrench(unittest.TestCase):
    '''Tests English to French function'''

    def test_english_to_french(self):
        '''Tests hello and snake translations'''
        result = english_to_french('Hello').get('translations')[0].get('translation')
        self.assertEqual(result, 'Bonjour')

    def test_english_to_french_null(self):
        '''Tests null'''
        with self.assertRaises(ValueError) as cm:
            english_to_french(None)
        self.assertEqual(str(cm.exception), 'text must be provided')

    def test_french_to_english(self):
        '''Tests Bonjour translations'''
        result = french_to_english('Bonjour').get('translations')[0].get('translation')
        self.assertEqual(result, 'Hello')

    def test_french_to_english_null(self):
        '''Tests null'''
        with self.assertRaises(ValueError) as cm:
            french_to_english(None)
        self.assertEqual(str(cm.exception), 'text must be provided')
unittest.main()
