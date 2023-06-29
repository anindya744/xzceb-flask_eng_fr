import unittest

from unittest.mock import patch

from translator import english_to_french, french_to_english

 

class TranslatorTestCase(unittest.TestCase):

    @patch('deep_translator.MyMemoryTranslator.translate')

    def test_english_to_french(self, mock_translate):

        mock_translate.return_value = 'Bonjour'

        english_text = 'Hello'

        expected_result = 'Bonjour'

        result = english_to_french(english_text)

        self.assertEqual(result, expected_result)

        mock_translate.assert_called_once_with(english_text)

 

    @patch('deep_translator.MyMemoryTranslator.translate')

    def test_french_to_english(self, mock_translate):

        mock_translate.return_value = 'Hello'

        french_text = 'Bonjour'

        expected_result = 'Hello'

        result = french_to_english(french_text)

        self.assertEqual(result, expected_result)

        mock_translate.assert_called_once_with(french_text)

 

    def test_english_to_french_notEqual(self):

        english_text = 'Hello'

        result = english_to_french(english_text)

        self.assertNotEqual(result, english_text)

 

    def test_french_to_english_notEqual(self):

        french_text = 'Bonjour'

        result = french_to_english(french_text)

        self.assertNotEqual(result, french_text)

 

if __name__ == '__main__':

    unittest.main()