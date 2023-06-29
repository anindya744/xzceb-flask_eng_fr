from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function for converting text from english to french"""
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Function for converting text from french to english"""
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
