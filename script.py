

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/МАСИВ ЛІТЕР\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#

chars = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
         'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ФІЛЬТРАЦІЯ ТЕКСТУ\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#


def Char_filter(text):       # функція фільтрації без пробілів
    A = []
    text = text.lower()     # перевід в нижній регістр

    for ch in text:     # фільтрація зайвих символів
        if ch in chars:
            A.append(ch)

    text = ''.join(A)
    text = text.replace('ъ', 'ь')   # заміна 'ъ' на 'ь'
    text = text.replace('ё', 'е')   # заміна 'ё' на 'е'

    return text


def Char_with_space_filter(text):       # функція фільтрації з пробілами
    A = []
    text = text.lower()     # перевід в нижній регістр

    for ch in text:     # фільтрація зайвих символів
        if ch in chars or ch == ' ':
            A.append(ch)

    text = ''.join(A)
    text = text.split()     # фільтрація зайвих пробілів
    text = ' '.join(text)
    text = text.replace('ъ', 'ь')   # заміна 'ъ' на 'ь'
    text = text.replace('ё', 'е')   # заміна 'ё' на 'е'

    return text


# відкриття файла з текстом і його зчитування
f = open(".\\duna.txt", "r", encoding='UTF-8')
duna_text = f.read()
f.close()

# відкриття/створення файла і запис в нього відфільтрованого тексту
f = open(".\\Filtered txt\\filtered.txt", "w")
f.write(Char_filter(duna_text))
f.close()

# відкриття/створення файла і запис в нього відфільтрованого тексту з пробілами
f = open(".\\Filtered txt\\filtered_with_space.txt", "w")
f.write(Char_with_space_filter(duna_text))
f.close()
