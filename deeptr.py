from translation_package.deeptrans_module import TransLate, LangDetect, CodeLang, LanguageList

# Демонстрація роботи функцій
text = "Добрий день"
print(TransLate(text, 'auto', 'en'))
print(LangDetect(text, 'all'))
print(CodeLang('uk'))
LanguageList('screen', text)
