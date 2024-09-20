from translation_package.gtrans_module import TransLate, LangDetect, CodeLang, LanguageList

# Демонстрація роботи функцій
text = "Добрий день"
print(TransLate(text, 'uk', 'en'))
print(LangDetect(text, 'all'))
print(CodeLang('Ukrainian'))
LanguageList('screen', text)
