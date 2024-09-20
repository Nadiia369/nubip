import os
from translation_package.gtrans_module import TransLate

# Читання конфігураційного файлу
def read_config():
    with open('Rzhevska/config.txt', 'r') as config_file:
        config = {}
        for line in config_file:
            key, value = line.strip().split(':')
            config[key] = value
        return config

# Основна програма
def main():
    config = read_config()

    # Перевірка наявності текстового файлу
    if not os.path.exists(config['filename']):
        print("Файл не знайдено.")
        return

    with open(config['filename'], 'r', encoding='utf-8') as file:
        text = file.read()

    # Переклад тексту
    translated_text = TransLate(text, 'auto', config['dest_lang'])

    # Вивід результатів
    if config['output'] == 'file':
        output_file = config['filename'].split('.')[0] + f"_{config['dest_lang']}.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated_text)
        print("Ok")
    else:
        print(f"Переклад на {config['dest_lang']}:")
        print(translated_text)

if __name__ == "__main__":
    main()
