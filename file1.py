from deep_translator import GoogleTranslator as gt
import langdetect
text = "змінювати погляд на звичайні речі"
print(text)
tr = gt(source='auto', target='en').translate(text)
print(langdetect.detect(text))
print(gt().get_supported_languages(as_dict=True))
print(tr)