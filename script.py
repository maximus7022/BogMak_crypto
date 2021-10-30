import os       # для видалення файлів

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
text = Char_filter(duna_text)
f.write(text)
f.close()

# відкриття/створення файла і запис в нього відфільтрованого тексту з пробілами
f = open(".\\Filtered txt\\filtered_with_space.txt", "w")
text_with_space = Char_with_space_filter(duna_text)
f.write(text_with_space)
f.close()

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/МОНОГРАМИ\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#


def Monogram_freq(text, i):         # функція підрахунку частот монограм
    if ' ' in text and i == 0:      # перевірка чи є пробіли в тексті
        chars.append(' ')
    freq = text.count(chars[i]) / len(text)     # підрахунок
    res_str = chars[i] + "  -->  " + str(freq) + "\n"
    return res_str


# перевірка чи існує вже файл щоб при повторному виконанні програми файл перезаписувався заново
if os.path.exists(".\\Mono&Bigrams\\monograms.txt"):
    os.remove(".\\Mono&Bigrams\\monograms.txt")

# запис монограм без пробілу і їх частот в файл
f = open(".\\Mono&Bigrams\\monograms.txt", "a")
for i in range(0, len(chars)):
    f.write(Monogram_freq(text, i))
f.close()

# перевірка чи існує вже файл щоб при повторному виконанні програми файл перезаписувався заново
if os.path.exists(".\\Mono&Bigrams\\monograms_with_space.txt"):
    os.remove(".\\Mono&Bigrams\\monograms_with_space.txt")

# запис монограм з пробілом і їх частот в файл
f = open(".\\Mono&Bigrams\\monograms_with_space.txt", "a")
for i in range(0, len(chars)+1):
    f.write(Monogram_freq(text_with_space, i))
f.close()
