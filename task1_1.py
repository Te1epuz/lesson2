# Вывести последнюю букву в слове
word = 'Архангельск'
print('последняя буква',word[-1])

# Вывести количество букв а в слове
word = 'Архангельск'
print('количество буквэ',len(word))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vovels_list = ['у', 'е', 'о', 'а', 'ы', 'я', 'и', 'ю']
sum = 0
for letter in word.lower():

    if letter in vovels_list:
        sum += 1

print('гласных',sum)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print ('слов в предложении',len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print('Усреднённая длина слов',len(sentence.replace(' ', ''))/len(sentence.split()))